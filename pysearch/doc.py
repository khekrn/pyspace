class Document():

    def __init__(self, id, text):
        self.id = id
        self.text = text

    def get_document_id(self):
        return self.id

    def get_text(self):
        return self.text

    def __repr__(self):
        doc = {
            "id": self.id,
            "text": self.text
        }
        return str(doc)
