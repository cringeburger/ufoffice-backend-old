from resources import DB
from resources.services import json_serializable


#
# Получение заметок пользователя
#
async def user_notes(user_id, quantity):

    quantity = 'all' if quantity == 100000 else quantity

    values = await DB.conn.fetch(
        f'''
            select
                nt.note_header,
                nt.note_body,
                nt.note_id
            from
                ufoffice.notes nt
            where
                nt.user_id = {user_id}
            limit {quantity};

        '''
    )
    
    result = json_serializable(f'notes_user_{user_id}')

    for item in values:

        result.add_features('id', str(item['note_id']))
        result.add_features('header', str(item['note_header']))
        result.add_features('body', str(item['note_body']))
        result.new_features_tuple()

    return str(result.data[:-1])


#
# Создание заметки
#
async def create_note(user_id, header, body):

    await DB.conn.fetch(
        f'''
            insert into ufoffice.notes (note_header, note_body, user_id)
                values ('{header}', '{body}', {user_id});
        '''
    )

    return 'success'


#
# Обновление заметки
#
async def update_note(note_id, header, body):

    await DB.conn.fetch(
        f'''
            update ufoffice.notes
                set
                    note_body = '{body}',
                    updated_dttm = now(),
                    note_header = '{header}'
                where note_id = {note_id};
        '''
    )
    
    return 'success'


#
# Удаление заметки
#
async def delete_note(note_id):

    await DB.conn.fetch(
        f'''
            delete from ufoffice.notes
            where note_id = {note_id};
        '''
    )
    
    return 'success'