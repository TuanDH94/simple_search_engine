import simple_search_engine.ultis as ultis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import _pickle as cPickle

class SearchEngine:
    def __init__(self):
        self.product_matrix = None
        self.product_matrix_accent = None
        self.tfidf_vectorizer = None
        self.svd = None
        self.corpus = []

    def build_model(self, data_path):
        documents = []
        for line in open(data_path, encoding='utf-8', newline='\n'):
            line = line.replace('\n', '')
            self.corpus.append(line)
            line = ultis.preprocess_text(line)
            documents.append(line)

        self.tfidf_vectorizer = TfidfVectorizer(min_df=3)
        self.svd = TruncatedSVD(random_state=123, n_components=10)
        document_tfidf = self.tfidf_vectorizer.fit_transform(documents)

        self.product_matrix = self.svd.fit_transform(document_tfidf)

        return

    def save_model(self):

        file = open('search_model.txt','wb')
        file.write(cPickle.dumps(self.__dict__))
        file.close()
        return

    def load_model(self):
        return

    def ranking(self, vector, candidates, top=5):
        sims = cosine_similarity(vector, candidates)[0]
        idxs = np.argsort(sims)[::-1]
        idxs = idxs[:5]
        return idxs

    def search(self, text, accent=False):
        text = ultis.preprocess_text(text)

        query_tfidf = self.tfidf_vectorizer.transform([text])
        query_vector = self.svd.transform(query_tfidf)

        idxs = self.ranking(query_vector, self.product_matrix)

        product_result = []
        for idx in idxs:
            product_result.append(self.corpus[idx])
        return product_result

    # def text_to_vector(self, text):


if __name__ == '__main__':
    # test search engine
    search_engine = SearchEngine()
    search_engine.build_model('data/product_names.txt')
    search_engine.save_model()

    query_file = 'data/100_query.txt'
    result_file = 'result.txt'
    with open(result_file, 'w+', encoding='utf-8') as f:
        for line in open(query_file, encoding='utf-8', newline='\n'):
            line = line.replace('\r\n', '')
            f.write(line + ':')
            product_results = search_engine.search(line)
            for i, result in enumerate(product_results):
                f.write('\n\t' + str(i) + '.\t' + result)
            f.write('\n------------------------------------\n')
        f.close()