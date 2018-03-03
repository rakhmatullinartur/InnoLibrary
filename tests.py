import requests
import json

url = 'http://127.0.0.1:5000/innoLibrary/api'

# # # test case 1
params = {'uid': 4, 'doc_id': 5, 'doc_type': 'book'}

response = requests.post(url + '/checkout', json=params)
print("------ tc1 ----------\n\n")
print('Patron checked out a book. Librarian got all info about book')
print(response.text)
params = {'id': 4}
response = requests.get(url + '/get_user_info', params=params)
print('Information about user. Also you can see what patron have checked out (by id of a document).\n')
print(response.text)
# print('Information about all documents stored in the library.')
# response = requests.get(url + '/get_documents')
# print('INFORMATION ABOUT all books stored in the library\n\n')
print(json.loads(response.text).get('books'))


#test case2
print('TEST N2\n')
params = {'authors': 'Marmeladkin'}
print('Patron checks out book by author Marmeladkin......\n')
responce = requests.post(url + '/checkout_by_author', params)
print('But gets response.....\n')
if responce.text == 'Json not found':
    print('Library has no book with this author')


#test case 3


print('------------------tc3-------------\n\n')
print('INFORMATION ABOUT ALL USERS\n\n')
response = requests.get(url+'/get_users')
print(response.text)
params = {'uid': 13, 'doc_id': 4, 'doc_type': 'book'}
response = requests.post(url + '/checkout', json=params)
print('USER faculty checked out a book for 4 weeks')
print(response.text)


# test case 4
print('-------------------tc4----------------\n\n')
print('A faculty member tries to check out a best seller\n\n')
params = {'uid': 13, 'doc_id': 1, 'doc_type': 'book'}

response = requests.post(url + '/checkout', json=params)
print('A book is checked out for two weeks (see due-date field)\n')
print(response.text)


#test case5
print('TEST N5\n')
params1 = {'uid': 4, 'doc_id': 6, 'doc_type': 'book'}
params2 = {'uid': 17, 'doc_id': 9, 'doc_type': 'book'}
params3 = {'uid': 14, 'doc_id': 9, 'doc_type': 'book'}
response1 = requests.post(url + '/checkout', json=params1)
print('Patron1 has just checked out 1st copy of book \n')
print(response1.text+'\n')
print('Patron2 has just checked out 2st copy of book \n')
response2 = requests.post(url + '/checkout', json=params2)
print(response2.text)
print('Patron3 has just checked out 3st copy of book ')
response3 = requests.post(url + '/checkout', json=params3)
print(response3.text)



# test case 6
print('------------------ tc6-------------------\n\n')
print('checkout a book ITP by faculty member')
params = {'uid': 13, 'doc_id': 2, 'doc_type': 'book'}
response = requests.post(url + '/checkout', json=params)
print(response.text)
print('\nchecking out a copy of the same book!\n')
params = {'uid': 13, 'doc_id': 4, 'doc_type': 'book'}
response = requests.post(url + '/checkout', json=params)
print(response.text)



print('TEST N7\n')
params1 = {'uid': 4, 'doc_id': 7, 'doc_type': 'book'}
params2 = {'uid': 17, 'doc_id': 8, 'doc_type': 'book'}
print('Patron1 and Patron2 check out copies of one book.......\n')
response1 = requests.post(url + '/checkout', json=params1)
response2 = requests.post(url + '/checkout', json=params2)
print(response1.text + '\n')
print(response2.text + '\n')



# #test case 8
print('--------------------tc8--------------------\n\n')
print('a student is checking out a book that is not a bestseller......')
params = {'uid': 4, 'doc_id': 10, 'doc_type': 'book'}
response = requests.post(url + '/checkout', json=params)
print(response.text)
print('\n\nbook is checked out to a student for three weeks (see due date field)\n\n')


# test case 9
print('-------------------tc9 --------------------\n\n')
print('a student is checking a book that is a bestseller.....')
params = {'uid': 4, 'doc_id': 13, 'doc_type': 'book'}
response = requests.post(url + '/checkout', json=params)
print(response.text)
print('\n\nbook is checked out to a student for two weeks, because it is a bestseller (see due date field)\n\n')


#test case10
print('TEST N10\n')
params1 = {'uid': 17, 'doc_id': 11, 'doc_type': 'book'}
params2 = {'uid': 17, 'doc_id': 12, 'doc_type': 'book'}
response1 = requests.post(url + '/checkout', json=params1)
response2 = requests.post(url + '/checkout', json=params2)
print('Patron checks out usual book ....\n Acsess!! \n')
print(response1.text + '\n')
print('Patron checks out reference book ....\n Oh!! \n')
print(response2.text)
# params = {'doc_type': 'Books', 'doc_id': '1', 'authors': 'brucelee'}
# response = requests.post(url + '/modify_doc', json=params)
# print(response.text)
