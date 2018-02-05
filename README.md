# InnoLibrary
Library Management System (LMS) - ITP Project 2nd Semester

#Api server Documentation

[endpoint: (http://localhost:5000/innoLibrary/api)]

## Methods marked with '*' have to be used with private key

_private keys are provided to developers and special people_
_ask for permission: **telegram - @rakhmatullinart**_

**Available methods:**
- signup (*)
- signin (*)
- get_user_info (*)

**Descriptions**
###signup
_required parameters_
* login
* password
* name
* user_type

_sample output:_

**json** {'success': 'True', errors: {}}
###signin
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

    
      
      




