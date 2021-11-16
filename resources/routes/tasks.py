from flask import request
from json import loads

from resources import DB
from resources import app
from resources.queries import (
    get_user_tasks,
    task_status_upd,
    task_crt
)


@app.route('/tasks', methods=['GET', 'POST', 'PATCH'])
async def tasks():
    try:
        await DB.connect()

        if request.method == 'GET':
            user_id = request.args['team_id']
            output = await get_user_tasks(user_id)

            await DB.close()

            return output

        elif request.method == 'POST':

            data = request.data.decode('utf8')
            output = await task_crt(
                loads(data)['name'],
                loads(data)['desc'],
                loads(data)['data'],
                loads(data)['rating'],
                loads(data)['id']
            )

            await DB.close()

            return output

        elif request.method == 'PATCH':

            data = request.data.decode('utf8')
            output = await task_status_upd(loads(data)['id'])

            await DB.close()

            return output

    except Exception as e:
        print(e)
