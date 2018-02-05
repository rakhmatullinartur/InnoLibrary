import pymysql

DB_HOST = "92.53.67.130"
DB_USER = "remote"
DB_PASSWORD = "conass"
DB_NAME = "book_saver"

paramstyle = "%s"


def connect():
    return pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, use_unicode=True, charset="utf8")


def execute(sql, *args, commit=False):
    db = connect()
    cur = db.cursor()
    print(args)
    print(sql % {"p": paramstyle})
    cur.execute(sql % {"p": paramstyle}, args)
    if commit:
        db.commit()
        db.close()
    else:
        ans = cur.fetchall()
        db.close()
        return ans


def create_user(*args):
    try:

        execute('INSERT INTO Users (login, password, user_type) VALUES (%(p)s, %(p)s, %(p)s)', *args, commit=True)
        return 'Success'
    except Exception as e:
        return str(e)


def identify_request(key):
    data = execute('SELECT * FROM private_keys WHERE token = %(p)s', key)
    if data:
        return True
    return False


def is_free_login(login):
    # login = 'test' () == False
    data = execute('SELECT * FROM Users WHERE login = %(p)s', login)
    if data:
        return False
    return True
