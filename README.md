# InnoLibrary
Library Management System (LMS) - ITP Project 2nd Semester

#Api server Documentation

[endpoint: (http://localhost:5000/innoLibrary/api)]

## Methods marked with '*' have to be used with private key

_private keys are provided to developers and special people_
_ask for permission: **telegram - @rakhmatullinart**_

**Available methods:**
**Available methods:**
- sign_up (*)
- sign_in (*)
- get_document(*)
- take_document(*)
- add_document(*)
- delete_document(*)
- create_user
- identify_request(*)
- is_free_login
- is_true_data
- get_book_info
- take_book
- get_user(*)
- add_document
- delete_document
- set_name
- set_phone_number
- add_fine_for_book
- set_address
- check_out_book
- return_book
- search_for_a_book
- renew_book
- get_user_info(*)
- initUI
- userLogIn
- userSignUp
- placeBooks
- showBook
- closeBook
- general_info
- get_doc_info
- get_all_users
- get_all_documents
- checkout
- permit_to_checkout
- are_copies
- checkout_by_author
- get_table
- get_user_obj
- get_taken_books
- create_class_object





**Descriptions**
###sign_up
_required parameters_
* login
* password
* name
* user_type

_sample output:_

**json** {'success': 'True', errors: {}}
###sign_in
_required parameters_
* login
* password
### add_document
headers = {'application/json'}

format json

_required parameters_

obligatory to pass following:
* doc_type - type of a document - string
* title - string
* authors - array of strings
* price - string
* room - string
* level - string

parameter passing depending on type of document
* search for in database for corresponding fields

####example of python request
<addr> import requests

test_book = {'doc_type': 'book', 'title': 'ITP', 'authors': ['Victor Rivera'] .....}

requests.post(url='www.someurl/endpoint/add_document', data=json.dumps(test_book), headers=headers)
</addr>

###sign_up
_*Create a new user account*_

_required parameters_
* login
* password
* name
* user_type

###sign_in
_*Log in to user account*_

_required parameters_
* login
* password

###get_document
_*Get book info from database using its id*_

_required parameters_
* doc_id
* data

###take_document
_*Assign one copy of document to specified user in the database*_

_required parameters_
* private_key

###add_document
_*Add new document to the database*_

_required parameters_
* data
* private_key

###delete_document
_*Delete document from database*_

_required parameters_
* data
* private_key

###create_user
_*Create a new user account*_

_required parameters_
* login
* user_type
* password

###identify_request
_*Identify a request*_

_required parameters_
* key

###is_free_login
_*Check availability of given login*_

_required parameters_
* login

###is_true_data
_*Check if given data is correct*_

_required parameters_
* login
* password

###get_book_info
_*Get information about given book using its id*_

_required parameters_
* doc_id

###take_book
_*Assign specified book to user*_

_required parameters_
* doc_id

###get_user
_*Get user account using id*_

_required parameters_
* uid

###add_document
_*Add new document*_

_required parameters_
* common
* doc_type

###initUI
_*Initialize User Id*_

_required parameters_
* login
* password

###delete_document
_*Delete document*_

_required parameters_
* doc_id
* doc_type

###set_name
_*Set name of the user*_

_required parameters_
* self
* new_name

###set_phone_number
_*Set phone number of the user*_

_required parameters_
* self
* new_phone_number

###add_fine_for_book
_*Add a fine for a certain book*_

_required parameters_
* self
* book_name

###set_address
_*Set address of the user*_

_required parameters_
* self
* new_address

###check_out_book
_*Check out the book*_

_required parameters_
* self
* bok

###return_book
_*Return a book from user to library*_

_required parameters_
* self
* bok

####search_for_a_book
_*Search for a book in a library system*_

_required parameters_
* self
* list_of_all_books
* looking_for

###renew_book
_*Special feature to renew the book*_

_required parameters_
* self
* name_of_book

###userLogIn
_*Prints login text*_

###userSignUp
_*Sign up for a user*_

###placeBooks
_*Put books on a certain place*_

_required parameters_
* name
* position

###showBook
_*Show book*_

###create_class_object
_*Creates an object of a certain class*_

_required parameters_
* doc_type
* mas

###get_taken_books
_*Show books taken by certain user*_

_required parameters_
* uid

###get_user_obj
_*Get object of class "user"*_

_required parameters_
* uid

###get_table
_*Get table of documents of a given type*_

_required parameters_
* doc_type

###checkout_by_author
_*Check out document by a given author*_

_required parameters_
* authors

###are_copies
_*Checks if two given books are copies*_

_required parameters_
* doc1
* doc2

###permit_to_checkout
_*Checks if the book is able to be checked out*_

_required parameters_
* books
* wanted_book_id

###checkout
_*Check out a book*_

_required parameters_
* kwargs
* doc_type
* table
* doc_id
* obj

###get_all_documents
_*Get all documents*_

###get_all_users
_*Get all users*_

###get_doc_info
_*Get information about given document*_

_required parameters_
* doc_id
* doc_type

###general_info
_*Get name and phone of a given user*_

_required parameters_
* uid
