class AVmaterial(dict):
    def __init__(self, *args):
        self.doc_id = args[0]
        self.title = args[1]
        self.authors = args[2]
        self.price = args[3]
        self.room = args[4]
        self.level = args[5]
        self.checked_out = args[6]