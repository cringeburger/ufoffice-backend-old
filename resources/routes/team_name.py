from flask import request
from resources import DB
from resources import app
from resources.queries import get_team_name


@app.get('/team_name')
async def teams():
    try:
        await DB.connect()

        output = await get_team_name(request.args['user_id'])

        await DB.close()

        return output

    except Exception as e:
        print(e)
