import os
from database import con,cur

def create_user():
    os.system('clear')
    new_data ='''
        INSERT INTO users (firstname,lastname,ide_number,email) VALUES('cristian',
        'diaz','44423','cris@gmail.com');
    '''
    con.execute(new_data)
    con.commit()
    print('user has created sucessfally')       
create_user()