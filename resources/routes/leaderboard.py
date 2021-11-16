from flask import request
from resources import DB
from resources import app
from resources.queries import get_leaderboard


@app.get('/leaderboard')
async def leaderboard_fnc():
    try:
        await DB.connect()

        user_id = request.args['user_id']
        output = await get_leaderboard(user_id)
        
        await DB.close()

        return output

    except Exception as e:
        print(e)
