""" Sources 

https://scikit-learn.org/stable/modules/feature_extraction.html

https://programminghistorian.org/en/lessons/counting-frequencies

https://www.freecodecamp.org/news/how-to-process-textual-data-using-tf-idf-in-python-cd2bbc0a94a3/

https://towardsdatascience.com/tf-term-frequency-idf-inverse-document-frequency-from-scratch-in-python-6c2b61b78558
 """



# Example 1.

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

data = ['this is sample 1', 'how about sample two', 'make three samples']
vectorizer = CountVectorizer()

transformed_data = vectorizer.fit_transform(data)

print (zip(vectorizer.get_feature_names(), np.ravel(transformed_data.sum(axis=0))))

""" [(u'about', 1),
 (u'how', 1),
 (u'is', 1),
 (u'make', 1),
 (u'sample', 2),
 (u'samples', 1),
 (u'this', 1),
 (u'three', 1),
 (u'two', 1)] """

# Example 2 :
vectorizer = CountVectorizer()
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
X = vectorizer.fit_transform(corpus)

analyze = vectorizer.build_analyzer()
analyze("This is a text document to analyze.") == (
    ['this', 'is', 'text', 'document', 'to', 'analyze'])


vectorizer.get_feature_names() == (
    ['and', 'document', 'first', 'is', 'one',
     'second', 'the', 'third', 'this'])


vectorizer.get_feature_names() == (
    ['and', 'document', 'first', 'is', 'one',
     'second', 'the', 'third', 'this'])


print(X.toarray())

