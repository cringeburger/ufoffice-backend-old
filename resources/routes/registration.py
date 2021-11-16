from flask import request
from json import loads
from resources import DB
from resources import app
from resources.queries import registration


@app.post('/registration')
async def login_user():
    try:
        await DB.connect()

        data = request.data.decode('utf8')
        output = await registration(
            loads(data)['login'],
            loads(data)['password']
            # ...
        )
        
        await DB.close()

        return output

    except Exception as e:
        print(e)
