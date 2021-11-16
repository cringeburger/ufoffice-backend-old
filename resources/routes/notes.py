from flask import request
from json import loads
from resources import DB
from resources import app
from resources.queries import (
    user_notes,
    create_note,
    update_note,
    delete_note
)


@app.route('/notes', methods=['GET', 'POST', 'PATCH', 'DELETE'])
async def notes():
    try:
        await DB.connect()

        if request.method == 'GET':
            
            user_id = request.args['user_id']
            quantity = request.args['quantity']
            output = await user_notes(user_id, quantity)

            await DB.close()

            return output

        elif request.method == 'POST':
            await DB.connect()

            data = request.data.decode('utf8')
            output = await create_note(
                loads(data)['user_id'],
                loads(data)['header'],
                loads(data)['body']
            )

            await DB.close()

            return output

        elif request.method == 'PATCH':

            data = request.data.decode('utf8')
            output = await update_note(
                loads(data)['note_id'],
                loads(data)['header'],
                loads(data)['body']
            )

            await DB.close()

            return output

        elif request.method == 'DELETE':
            
            data = request.data.decode('utf8')

            output = await delete_note(loads(data)['note_id'])

            await DB.close()

            return output

    except Exception as e:
        print(e)