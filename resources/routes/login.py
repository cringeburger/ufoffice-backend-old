from flask import request
from json import loads
from resources import DB
from resources import app
from resources.queries import check_user_login


@app.post('/login')
async def login_user():
    try:

        await DB.connect()
        
        data = request.data.decode('utf8')
        output = await check_user_login(loads(data)['username'], loads(data)['password'])

        await DB.close()

        return output

    except Exception as e:
        print(e)
