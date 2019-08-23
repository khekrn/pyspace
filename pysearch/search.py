import pysearch

import string


class InvertedSearch(pysearch.Indexer):

    def __init__(self):
        self.index_dict = dict()
        self.translator = str.maketrans('', '', string.punctuation)

    def index(self, documents):
        for doc in documents:
            doc_id = doc.get_document_id()
            doc_content = doc.get_text()
            doc_content = doc_content.translate(self.translator).lower()
            temp_dict = dict()
            for word in doc_content.split(" "):
                if word not in temp_dict:
                    temp_dict[word] = 1
                else:
                    temp_dict[word] = temp_dict[word] + 1
            for key, value in temp_dict.items():
                if key not in self.index_dict:
                    self.index_dict[key] = [(doc_id, value)]
                else:
                    arr = self.index_dict[key]
                    arr.append((doc_id, value))
                    self.index_dict[key] = arr

    def search(self, word):
        if word is None or word not in self.index_dict:
            return None
        word = word.lower()
        res: list = self.index_dict[word]
        res.sort(key=lambda x: x[1], reverse=True)
        return res


if __name__ == '__main__':
    inv_search = InvertedSearch()
    docs = [
        pysearch.Document(1, "The big sharks of Belgium drink beer."),
        pysearch.Document(2, "Belgium has great beer. They drink beer all the time.")
    ]

    inv_search.index(docs)

    print(inv_search.search("beer"))
