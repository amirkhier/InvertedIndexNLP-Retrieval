import re
import nltk
import collections
from inverted_index import InvIndex
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import snowball
from nltk.stem import WordNetLemmatizer


#opening the docs
file = open('D1.txt')
file1 = open('D2.txt')
file2 = open('D3.txt')
file3 = open('D4.txt')

#reading the docs

string1 = file.read()
string2 = file1.read()
string3 = file2.read()
string4 = file3.read()

docs =[string1,string2,string3,string4]

print(docs)
print(len(docs))


# insert docs to the index
do = InvIndex()
docsNew = do.InvertedDoc(docs)
print(docsNew)
Query = input('Enter Query : ')


# normalization query
q1 = InvIndex()
newq = q1.InvertedQuery(Query)
print(newq)

# retrival the docs that include all the words that occurs in query
match = q1.FindMatch(docsNew,newq)
print('Match in Doc Exists : ' ,match)








