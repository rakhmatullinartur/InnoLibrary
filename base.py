import pymysql
import datetime
import Book, Article, AV_materials


DB_HOST = "92.53.67.130"
DB_USER = "remote"
DB_PASSWORD = "welding"
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


def general_info(uid):
    data = execute('SELECT first_name , phone_number FROM Users WHERE uid = %(p)s' , uid)
    return data


def create_user(**kwargs):
    try:
        if is_free_login(kwargs.get('login')):
            execute('INSERT INTO Users (first_name, last_name, email, phone_number, login, password) '
                    'VALUES (%(p)s, %(p)s, %(p)s, %(p)s, %(p)s, %(p)s)',
                    kwargs.get('first_name'),
                    kwargs.get('last_name'),
                    kwargs.get('email'),
                    kwargs.get('phone_number'),
                    kwargs.get('login'),
                    kwargs.get('password'), commit=True
                    )
            return {'success': 'true'}
        return {'success': 'false', 'error': 'login is busy'}
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


def is_true_data(login, password):
    data = execute('SELECT * FROM Users WHERE login = %(p)s AND password = %(p)s', login, password)
    if data:
        return True
    return False


def get_doc_info(doc_id, doc_type):
    table = get_table(doc_type)
    data = execute('SELECT * FROM {} WHERE doc_id = %(p)s'.format(table), doc_id)
    obj = create_class_object(doc_type, data[0])
    return obj


def get_user(uid):
    data = execute('SELECT * FROM Users WHERE uid = %(p)s', uid)
    print(data)
    docs = execute('SELECT doc_id, due_date FROM taken_documents WHERE uid = %(p)s', uid)
    documents = []
    print(docs)
    for e in docs:
        documents.append({'doc_id': e[0], 'due_date': e[1]})
    if data:
        data = data[0]
        res = {
             'card_number': data[0],
             'name': data[1],
             'phone_number': data[2],
             'login': data[3],
             'user_type': data[5],
             'documents': documents}
        return res
    return 'not found'


def get_all_users():
    data = execute('SELECT * FROM Users')
    res = []
    if data:
        for user in data:
            res.append({
                'user_id': user[0],
                'first_name': user[1],
                'last_name': user[2],
                'email': user[3],
                'phone_number': user[4],
                'login': user[5],
                'password': user[6],
                'user_type': user[7]
            })
        return res
    return 'not found'


def add_document(**kwargs):
    common =[kwargs.get('title'), ';'.join(kwargs.get('authors')), kwargs.get('price'), kwargs.get('room'), kwargs.get('level')]
    doc_type = kwargs.get('doc_type')
    if doc_type == 'book':
        execute('INSERT INTO Books (title, authors, price, room, level, publisher, edition) '
                'VALUES (%(p)s, %(p)s, %(p)s, %(p)s, %(p)s, %(p)s, %(p)s)',
                *common,
                kwargs.get('publisher'),
                kwargs.get('edition'), commit=True)

    elif doc_type == 'journal arcticle':
        execute('INSERT INTO Journal_Articles (title, authors, price, room, level, journal_title, journal_publisher, journal_issue,'
                ' issue_editor, issue_publication_date) '
                'VALUES (%(p)s, %(p)s, %(p)s, %(p)s, %(p)s, %(p)s, %(p)s, %(p)s, %(p)s, %(p)s)',
                ';'.join(kwargs.get('authors')),
                *common,
                kwargs.get('journal_title'),
                kwargs.get('journal_publisher'),
                kwargs.get('journal_issue'),
                kwargs.get('issue_editor'),
                kwargs.get('issue_publication_date'), commit=True
                )
    elif doc_type == 'AV':
        execute('INSERT INTO AV_materials (title, authors, price, room, level) VALUES '
                '(%(p)s, %(p)s, %(p)s, %(p)s, %(p)s)',
                *common, commit=True)


def delete_document(doc_id, doc_type):
    try:
        execute(f'DELETE FROM {doc_type} WHERE doc_id = %(p)s', doc_id, commit=True)
        return 'OK'
    except Exception as e:
        return str(e)


def checkout(**kwargs):
    doc_type = kwargs.get('doc_type')
    table = get_table(doc_type)
    doc_id = kwargs.get('doc_id')
    execute('UPDATE {} SET checked_out = 1 WHERE doc_id = %(p)s'.format(table), doc_id, commit=True)
    due_date = take_document(doc_id=doc_id, doc_type=doc_type, uid=kwargs.get('uid'))
    data = vars(get_doc_info(doc_id, doc_type))
    data['due_date'] = due_date
    return data


def take_document(**kwargs):
    now = datetime.datetime.now()
    due = str(now + datetime.timedelta(days=14)).split(' ')[:16]
    try:
        execute('INSERT INTO taken_documents (doc_id, doc_type, uid, due_date) VALUES (%(p)s, %(p)s, %(p)s, %(p)s)',
                kwargs.get('doc_id'),
                kwargs.get('doc_type'),
                kwargs.get('uid'),
                due, commit=True)
        return due
    except Exception as e:
        return str(e)


def get_table(doc_type):
    table = ''
    if doc_type == 'book':
        table = 'Books'
    elif doc_type == 'AV':
        table = 'AV_materials'
    elif doc_type == 'article':
        table = 'Journal Arcticles'
    return table


def create_class_object(doc_type, *args):
    obj = None
    if doc_type == 'book':
        obj = Book.Book(*args)
    elif doc_type == 'AV':
        obj = AV_materials.AVmaterial(*args)
    elif doc_type == 'article':
        obj = Article.JournalArticle(*args)
    return obj