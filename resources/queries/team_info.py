from resources import DB
from resources.services import json_serializable
from resources.queries import skills_info
import json


#
# Список участников в команде
#
async def team_list(user_id):

    values = await DB.conn.fetch(
        f'''
            select
                us.user_fio,
                pr.profession_name,
                us.user_image,
                us.user_mail,
                us.user_phone,
                us.user_vk,
                us.user_tg,
                us.user_facebook,
                (select
                    t.task_name
                from
                    ufoffice.tasks t
                join ufoffice.user_tasks ut
                    on ut.user_id = us.user_id
                    and ut.task_id = t.task_id
                where
                    t.end_dt > now()
                limit 1) curr_task,
                (select
                    t.end_dt
                from
                    ufoffice.tasks t
                join ufoffice.user_tasks ut
                    on ut.user_id = us.user_id
                    and ut.task_id = t.task_id
                where
                    t.end_dt > now()
                limit 1) end_dt,
                (row_number() over())-1 as position_usr,
                us.user_rating,
                us.user_id,
                team.team_name
            from
                ufoffice.users us
            join ufoffice.team_participants team_p
                on team_p.user_id = 3
            join ufoffice.teams team
                on team.team_id = team_p.team_id
            join ufoffice.professions pr
                on pr.profession_id = us.profession_id
            where
                us.user_id in (
                    select
                        team_p1.user_id
                    from
                        ufoffice.team_participants team_p1
                    where 
                        team_p1.team_id = team.team_id
                )
            order by
                (row_number() over())-1;
        '''
    )
    
    result = json_serializable(f'skills_user_{user_id}')

    for item in values:

        result.add_features('name', str(item['user_fio']))
        result.add_features('proffesion', str(item['profession_name']))
        result.add_features('img', str(item['user_image']))
        result.add_features('mail', str(item['user_mail']))
        result.add_features('phone', str(item['user_phone']))
        result.add_features('tg', str(item['user_vk']))
        result.add_features('vk', str(item['user_tg']))
        result.add_features('fb', str(item['user_facebook']))
        result.add_features('work', str(item['curr_task']))
        result.add_features('ttd', str(item['end_dt']))
        result.add_features('position', str(item['position_usr']))
        result.add_features('rating', str(item['user_rating']))
        result.add_features('id', str(item['user_id']))
        result.add_features('teamName', str(item['team_name']))

        result.add_feature_list('skills')
        result.data[result.t_index]['skills'].extend(await skills_info(item['user_id']))
        result.new_features_tuple()

    return json.dumps(result.data[:-1], indent=2)


#
# Название команды
#
async def get_team_name(user_id):

    result = await DB.conn.fetch(
        f'''
            select
                team.team_name
            from
                ufoffice.users us
            join ufoffice.team_participants opt
                on opt.user_id = us.user_id
            join ufoffice.teams team
                on team.team_id = opt.team_id
            where
                us.user_id = {user_id};
        '''
    )

    return str(result[0]['team_name'])
