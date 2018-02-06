class Book(dict):
    def __init__(self , *args):
        self.doc_id = args[0]
        self.title = args[1]
        self.authors = args[2]
        self.publisher = args[3]
        self.edition = args[4]
        self.price = args[5]
        self.room = args[6]
        self.level = args[7]
        self.checked_out = args[8]