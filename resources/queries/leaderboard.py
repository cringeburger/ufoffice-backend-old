from resources.services import json_serializable
from resources import DB
import json


#
# Таблица лидеров
#
async def get_leaderboard(user_id):

    data = await DB.conn.fetch(
        f'''
            with org as (
                select
                    org.org_id
                from
                    ufoffice.users us
                join ufoffice.org_participants opt
                    on opt.user_id = us.user_id
                join ufoffice.organizations org
                    on org.org_id = opt.org_id
                where
                    us.user_id = {int(user_id)}
            ),
            users as (
                select
                    *
                from
                    ufoffice.users us
                join ufoffice.org_participants opt
                    on us.user_id = opt.user_id
            )
            select
                row_number() over() as rn,
                t.* 
            from (
                select 
                    user_fio,
                    user_rating
                from
                    users
                order by
                    user_rating desc
            ) t;
        '''
        )

    result = json_serializable(f'leaderboard_user_{user_id}')
    
    for item in data:
        result.add_features('name', str(item['user_fio']))
        result.add_features('rating', str(item['user_rating']))
        result.add_features('position', str(item['rn']))

        result.new_features_tuple()

    return json.dumps(result.data[:-1], indent=2)


#
# Инормация по юзеру в топе
#
async def get_leaderboard_place(user_id):
        
    data = await DB.conn.fetch(
        f'''
            with org as (
                select
                    org.org_id
                from
                    ufoffice.users us
                join ufoffice.org_participants opt
                    on opt.user_id = us.user_id
                join ufoffice.organizations org
                    on org.org_id = opt.org_id
                where
                    us.user_id = {int(user_id)}
            ),
            users as (
                select
                    us.*,
                    opt.org_id
                from
                    ufoffice.users us
                join ufoffice.org_participants opt
                    on us.user_id = opt.user_id
            )
            select
            	*
            from (
	            select
	                row_number() over() as rn,
	                t.* 
	            from (
	                select 
	                    user_fio,
	                    user_rating,
	                    user_id
	                from
	                    users
	                order by
	                    user_rating desc
	            ) t
			) t2
			where
				user_id = {int(user_id)};
        '''
        )

    result = json_serializable(f'leaderboard_user_{user_id}')
    
    for item in data:
        result.add_features('name', str(item['user_fio']))
        result.add_features('rating', str(item['user_rating']))
        result.add_features('position', str(item['rn']))

    return json.dumps(result.data[0], indent=2)