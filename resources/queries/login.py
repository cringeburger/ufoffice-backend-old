from resources.services import hash_pass, json_serializable
from resources import DB


async def check_user_login(login, password):

    try:
        
        data = await DB.conn.fetch(
            '''
                select 
                    u.username, 
                    u.user_password, 
                    u.user_id,
                    ur.user_role_sysname
                from 
                    ufoffice.users u
                join ufoffice.user_roles ur
                    on ur.user_role_id = u.user_role_id
            '''
            )

        for item in data:
            if login.lower() == item['username'] and hash_pass.hash_check(item['user_password'], password) == True:
                result = json_serializable('rsp')
                result.add_features('login', str(item['username']))
                result.add_features('token', str(item['user_id']))
                result.add_features('role', str(item['user_role_sysname']))
                
                return result.data[0]	
        
        return 'wrong'
    
    except Exception as e:
        print('Exceprion: ', e)
