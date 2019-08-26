import pysearch
import collections
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
            for word in doc_content.split(" "):
                if word not in self.index_dict:
                    self.index_dict[word] = {doc_id: 1}
                else:
                    doc_count_dict: dict = self.index_dict[word]
                    if doc_id in doc_count_dict:
                        doc_count_dict[doc_id] = doc_count_dict[doc_id] + 1
                    else:
                        doc_count_dict[doc_id] = 1
                    self.index_dict[word] = doc_count_dict

    def search(self, word):
        if word is None or word not in self.index_dict:
            return None
        word = word.lower()
        res: dict = self.index_dict[word]
        sort_order = sorted(res.items(), key=lambda kv: kv[1], reverse=True)
        return collections.OrderedDict(sort_order)


if __name__ == '__main__':
    inv_search = InvertedSearch()
    docs = [
        pysearch.Document(1, "The big sharks of Belgium drink beer."),
        pysearch.Document(2, "Belgium has great beer. They drink beer all the time."),
        pysearch.Document(3, "belgium chocolates are so cool and i want to have more belgium belgium belgium chocolate")
    ]

    inv_search.index(docs)

    print(inv_search.search("belgium"))
