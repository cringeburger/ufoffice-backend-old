from resources import DB
from resources.services import json_serializable


#
# Навыки пользователя
#
async def skills_info(user_id):

    values = await DB.conn.fetch(
        f'''
            select
                sk.skill_img,
                case
                    when sk.skill_name is null then 'Нет навыков'
                    else sk.skill_name
                end as skill_name
            from
                ufoffice.users us
            left join ufoffice.user_skills usk
                on usk.user_id = us.user_id
            left join ufoffice.skills sk
                on sk.skill_id = usk.skill_id
            where
                us.user_id = {user_id};
        '''
    )
    
    result = json_serializable(f'skills_user_{user_id}')
    for item in values:
        result.add_features('skill_img', str(item['skill_img']))
        result.add_features('skill_name', str(item['skill_name']))
        result.new_features_tuple()

    return result.data[:-1]
