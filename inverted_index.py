import re
import nltk
import collections
from collections import Counter
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import snowball
from nltk.stem import WordNetLemmatizer


class InvIndex:
    def __init__(self):
        self.inv={}


    def InvertedDoc(self,docs):
        sum_docs = []
        stwords = set(stopwords.words('english'))
        stemmer = snowball.SnowballStemmer('english')
        lemmatizer = WordNetLemmatizer()

        for i in docs:
            doc1 = re.sub(r'[^\w\s]','',i)
            #clean words like :?!,
            doc2 = word_tokenize(doc1)
            #split the words
            doc3 = list(set(doc2) - stwords)
            #removing the stopwords
            doc4 = []
            for w in doc3:
                a = stemmer.stem(w)
                b = lemmatizer.lemmatize(a)
                doc4.append(b)
            #phase STEMMING AND LEMITATION

            sum_docs.append(doc4)

        dictionary ={}
        print(sum_docs)
        print(len(sum_docs))

        for i in range(len(sum_docs)):
            count = Counter(sum_docs[i])
            print('sum each word in doc :',i+1,count)

            for key in count.keys():
                if key in dictionary:
                    dictionary[key].append([i+1,count[key]])
                else:
                    dictionary[key] = [[i+1,count[key]]]

        return dictionary

    def InvertedQuery(self,Query_List):
        stwords = set(stopwords.words('english'))
        stemmer = snowball.SnowballStemmer('english')
        lemmatizer = WordNetLemmatizer()

        q1 = re.sub(r'[^\w\s]','',Query_List)
        q2 = word_tokenize(q1)
        q3 = list(set(q2) - stwords)
        q4 =[]
        for i in q3:
            a = stemmer.stem(i)
            b = lemmatizer.lemmatize(a)
            q4.append(b)

        return q4

    def FindMatch(self,docs,query):

        relevant_docs = set()

        for i in query:
            for j in docs[i]:
                relevant_docs.add(j[0])

        retrieved_docs = self.FindRetrievedDocs(docs, query)

        precision = len(retrieved_docs) / len(docs)
        recall = len(retrieved_docs) / len(relevant_docs)

        return retrieved_docs, precision, recall,len(retrieved_docs),len(relevant_docs),len(docs)

    def FindRetrievedDocs(self, docs, query):
        whatreturns = {1: 0, 2: 0, 3: 0, 4: 0}
        list1 = []

        for i in query:
            for j in docs[i]:
                whatreturns[j[0]] += 1

        for key in whatreturns.keys():
            if whatreturns[key] == len(query):
                list1.append(key)

        return list1



















