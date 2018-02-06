class JournalArticle(dict):
    def __init__(self, *args):
        self.doc_id = args[0]
        self.authors = args[1]
        self.title = args[2]
        self.journal_title = args[3]
        self.journal_publisher = args[4]
        self.journal_issue = args[5]
        self.issue_editor = args[6]
        self.issue_publication_date = args[7]
        self.price = args[8]
        self.room = args[9]
        self.level = args[10]
        self.checked_out = args[11]