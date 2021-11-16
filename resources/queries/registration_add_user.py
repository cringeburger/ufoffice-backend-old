from resources.services import hash_pass
from resources import DB


async def registration(
    username,
    password,
    user_sex,
    user_birthday,
    user_fio, 
    user_mail,
    user_vk,
    user_tg,
    user_image,
    org_id,
    user_role_id=None,
):
    try:

        data = await DB.conn.fetch(
            '''select 
                u.username
            from
                ufoffice.users u;
            '''
            )

        for item in data:
            if username.lower() == item['username']:
                return 'wrong'
        

        await DB.conn.fetch(
            f'''
            insert into ufoffice.users(
                    username,
                    password,
                    user_sex,
                    user_birthday,
                    user_fio, 
                    user_mail,
                    user_vk,
                    user_tg,
                    user_role_id,
                    user_rating,
                    user_image)
                values (
                    '{username}',
                    '{hash_pass.pass_hash(password)}',
                    '{user_sex}',
                    date'{user_birthday}',
                    '{user_fio}', 
                    '{user_mail}',
                    '{user_vk}',
                    '{user_tg}',
                    {user_role_id},
                    0,
                    '{user_image}'
                );
            '''
        )

        user_id = await DB.conn.fetch(
            '''select 
                max(u.user_id)
            from
                ufoffice.users u;
            '''
            )

        await DB.conn.fetch(
            f'''
            insert into ufoffice.org_participants(user_id, org_id)
                values(
                    {user_id},
                    {org_id}
                );
            '''
        )
        return 'success'

    except Exception as e:
        print('Exceprion: ', e)
