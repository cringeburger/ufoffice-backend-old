from flask import request
from resources import DB
from resources import app
from resources.queries import team_list


@app.get('/team')
async def team():
    try:
        await DB.connect()
        
        user_id = request.args['user_id']
        output = await team_list(user_id)

        await DB.close()

        return output

    except Exception as e:
        print(e)
