from resources import DB
from resources.services import json_serializable
import json


#
# ------- Получение задач юзеров -------
#
async def get_user_tasks(org_id=1):

    users = await DB.conn.fetch(
        f'''
            select
                us.user_fio,
                pr.profession_name,
                us.user_id
            from
                ufoffice.users us
            join ufoffice.professions pr
                on pr.profession_id = us.profession_id
            join ufoffice.team_participants team
                on team.team_id = {org_id}
                and team.user_id = us.user_id;
        '''
    )
    
    result = json_serializable(f'tasks_team_{org_id}')

    for item in users:
        result.add_features('name', str(item['user_fio']))
        result.add_features('proffesion', str(item['profession_name']))
        result.add_features('id', str(item['user_id']))
        
        result.add_feature_list('tasks')

        tasks = await DB.conn.fetch(
            f'''
                select
                    ts.task_name,
                    to_char(ts.end_dt, 'dd.mm.yyyy') end_dt,
                    ts.ach_pts,
                    ts.task_desc,
                    tsnm.task_status_sysname,
                    ts.task_id,
                    us.user_id
                from
                    ufoffice.users us
                join ufoffice.user_tasks ust
                    on ust.user_id = us.user_id
                join ufoffice.tasks ts
                    on ts.task_id = ust.task_id
                join ufoffice.task_status tst
                    on tst.task_id = ts.task_id
                join ufoffice.task_status_name tsnm
                    on tsnm.task_status_name_id = tst.task_status_name_id
                where
                    us.user_id = {str(item['user_id'])}
            '''
        )
        for task in tasks:
            result.data[result.t_index]['tasks'].append(
                {
                    'name': task['task_name'],
                    'time': task['end_dt'],
                    'level': task['ach_pts'],
                    'description': task['task_desc'],
                    'status': task['task_status_sysname'],
                    'id': task['task_id'],
                    'user_id': task['user_id']
                }
            )

        result.new_features_tuple()

    return str(json.dumps(result.data[:-1], indent=2))


#
# ------- Обновление статуса задачи -------
#
async def task_status_upd(task_id):

    await DB.conn.fetch(
        f'''
            update ufoffice.task_status
                set task_status_name_id=2
                where task_id = {int(task_id)};
        '''
    )

    return 'success'

#
# ------- Создание задачи -------
#
async def task_crt(
    task_name,
    task_desc,
    end_dt,
    ach_pts,
    user_id
):

    await DB.conn.fetch(
        f'''
            insert into ufoffice.tasks (
                task_name,
                task_desc,
                end_dt,
                ach_pts
            )
                values (
                    '{task_name}',
                    '{task_desc}',
                    '{end_dt}'::date,
                    {int(ach_pts)}
                );
        '''
    )

    await DB.conn.fetch(
        f'''
            insert into ufoffice.user_tasks (
                user_id,
                task_id
            )
                values (
                    {int(user_id)},
                    (select max(task_id) from ufoffice.tasks)
                );
        '''
    )
    
    await DB.conn.fetch(
        f'''
            insert into ufoffice.task_status (
                task_status_name_id,
                task_id
            )
                values (
                    1,
                    (select max(task_id) from ufoffice.tasks)
                );
        '''
    )
    
    return 'success'
