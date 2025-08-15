import os
from database import con,cur
def create_user():
    os.system('clear')
    fname =input('enter your firtsname:')
    lname =input('enter your lastname:')
    ide_num=input('enter your ident. number')
    email=input('enter your email')
    new_data=f'''
        insert into users (firstname, lastname,ide_number,email)
        values('{fname}','{lname}','{ide_num}','{email}')
    '''
    con.execute(new_data)
    con.commit()
    print("user has been created sucessfally")
#create_user()


def list_users():
    os.system('clear')
    users_data_query='''
    select
       firstname,
       lastname,
       email,
       ide_number,

       case when status =1 then 'Active'else'inactive'end as status
    from
        users

    '''
    cur.execute(users_data_query)
    data = cur.fetchall()

    print(data)
list_users()


