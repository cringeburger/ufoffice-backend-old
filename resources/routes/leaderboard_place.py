from flask import request
from resources import DB
from resources import app
from resources.queries import get_leaderboard_place


@app.get('/user_rating')
async def user_rating():
    try:
        await DB.connect()

        user_id = request.args['user_id']
        output = await get_leaderboard_place(user_id)
        
        await DB.close()

        return output

    except Exception as e:
        print(e)
