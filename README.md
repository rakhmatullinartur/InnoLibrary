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

    
      
      




