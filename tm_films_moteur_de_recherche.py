# -*- coding: utf-8 -*-
"""TM_Films_Moteur de recherche.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ua07H_3emuOkrszu49jsdohu9rqoqihq
"""

########## Monter mon drive sur colab
from google.colab import drive
drive.mount('/content/drive')

#Importation des packages
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
!pip install spacy
!python -m spacy download fr_core_news_md
import spacy
import fr_core_news_md
!pip install -U textblob
!pip install -U textblob-fr

#Enlever les Stop Word
def remove_stop_words(corpus):
    french_stop_words = stopwords.words('french')
    word_tokens = word_tokenize(corpus) 
    filtered_sentence = [] 
    for w in word_tokens: 
        if w not in french_stop_words: 
            filtered_sentence.append(w) 
    return ' '.join(filtered_sentence)

#Stemming
"""
def get_stemmed_text(sentence):
    token_words=word_tokenize(sentence)
    stem_sentence=[]
    porter=PorterStemmer()
    for word in token_words:
        stem_sentence.append(porter.stem(word))
    return ' '.join(stem_sentence)
"""

#Lemmatization (n'est pas fiable)
"""
def get_lemmatized_text(corpus):
    wordnet_lemmatizer = WordNetLemmatizer()    
    token_words=word_tokenize(corpus)
    lem_sentence=[]
    for w in token_words:
        lem_sentence.append(wordnet_lemmatizer.lemmatize(w))
    return ' '.join(lem_sentence)
"""

#Lematization avec fr_core_news_md fiable que WordNetLemmatizer
nlp = fr_core_news_md.load()
def get_lemmatized_text(corpus):
    filtered_sentence = []
    t= nlp(u""+corpus)
    for i in t:
       filtered_sentence.append(i.lemma_)
    return ' '.join(filtered_sentence)

#enlever les ponctuation et les nombres
def get_unpuncuated_text(corpus):
    words = nltk.word_tokenize(corpus)
    words=[word.lower() for word in words if word.isalpha()]
    return ' '.join(words)

#Preprocessing 
def preprocessing(corpus):
  corpus= remove_stop_words(corpus)
  corpus=get_lemmatized_text(corpus)
  corpus =get_unpuncuated_text(corpus)
  return corpus

# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus# sample text for performing tokenization
text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the easternside of South America"# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(text)
token

import re

def nom_prenom(s):
    """Si "s" est une adresse email (chaîne de caractère) de l'université de Savoie,
la fonction renvoie un tuple composé du prénom et du nom de la personne.
Renvoie "None" sinon."""
    s = s.strip()
    m = re.search("^([\\w_-]+)\.([\\w_-]+)" , s)
    if m != None:
        prenom, nom = m.group(1,2)
        return (prenom.capitalize(), nom.capitalize())
    else:
        return None

k=nom_prenom(txt)
print(k)

import urllib.request

import nltk

freq = nltk.FreqDist(m)

for key,val in freq.items():

    print (str(key) + ':' + str(val))

pp=[]
for i in m:
    pp.append(i.lower())

pp

import urllib.request

import nltk

freq = nltk.FreqDist(pp)

for key,val in freq.items():

    print (str(key) + ':' + str(val))

from nltk.corpus import stopwords
clean_tokens = pp
stopwords.words('french')
tokens = pp

sr = stopwords.words('french')

for token in tokens:

    if token in stopwords.words('french'):

        clean_tokens.remove(token)

pp

#Enlever les Stop Word
def remove_stop_words(corpus):
    french_stop_words = stopwords.words('french')
    word_tokens = word_tokenize(corpus) 
    filtered_sentence = [] 
    for w in word_tokens: 
        if w not in french_stop_words: 
            filtered_sentence.append(w) 
    return ' '.join(filtered_sentence)

# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
# sample text for performing tokenization
text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the eastern side of South America"
# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(text)
token

#Enlever les Stop Word
def remove_stop_words(corpus):
    french_stop_words = stopwords.words('french')
    word_tokens = word_tokenize(corpus) 
    filtered_sentence = [] 
    for w in word_tokens: 
        if w not in french_stop_words: 
            filtered_sentence.append(w) 
    return ' '.join(filtered_sentence)
remove_stop_words(m)

#Enlever les Stop Word
def remove_stop_words(corpus):
    french_stop_words = stopwords.words('french')
    word_tokens = word_tokenize(corpus) 
    filtered_sentence = [] 
    for w in word_tokens: 
        if w not in french_stop_words: 
            filtered_sentence.append(w) 
    return ' '.join(filtered_sentence)
remove_stop_words(m)

#Preprocessing sur les description
desc_clean=[]
for i in desc:
  desc_clean.append(preprocessing(i))

#Preprocessing sur les avis
def clean_Avis(a):
   c=[]
   for i in a:
      x=i.replace("\n","")
      for j in range(20):
          if "  " in x:
               x=x.replace("  ","")
      c.append(x)
   for k in range(0,len(c)):
        if c[k] == "":
          c[k]=None
          
   return c 
clean_avis=clean_Avis(avis)

"""Recherche par titre"""

#Grouper les avis (une fct qui retourne les avis d'un film donné ordonné par score)
def grouper_par_score(t):
  d={"Titre":titreR,"Avis":clean_avis,"Score":rating}
  a= pd.DataFrame(d) 
  a= a[a["Titre"] == t]
  a=a.dropna(axis=0)
  a=a.sort_values(by=['Score'], ascending=False)
  return a

#Recherche par titre (une fct qui retourne toute les infos d'un film donné)
def recherche_par_titre(t):
  for i in titre:
    if i == t:
      print("Titre :"+t)
      print("Genre :"+genre[titre.index(i)])
      print("Description :"+desc[titre.index(i)])
      print("Avis :")
      print(grouper_par_score(t))

recherche_par_titre("Titans")

#Analyser les sentiments des avis
def analyser_avis():
  from textblob import TextBlob
  from textblob import Blobber
  from textblob_fr import PatternTagger, PatternAnalyzer
  tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
  res=[]
  for i in avis:
      text = tb(u""+i)
      res.append(text.sentiment[0])
  ress=[]
  for i in range(0,len(res)):
      res[i]=round(res[i],2)
      if res[i] > 0:
        ress.append(str("Positive de "+ str(int(res[i]*100))+ "%"))
      elif res[i] == 0:
        ress.append(str("Neutre"))
      else :
        ress.append(str("Négative de "+ str(int(res[i]*100*-1))+ "%"))
  return [res,ress]

#Grouper les avis (une fct qui retourne les avis d'un film donné ordonné par analyse de sens) 
def grouper_par_avis(t):
  av=analyser_avis()
  d={"Titre":titreR , "Avis":clean_avis , "Sentiment": av[1] , "ordre": av[0]}
  a= pd.DataFrame(d) 
  a= a[a["Titre"] == t]
  a=a.dropna(axis=0)
  a=a.sort_values(by=["ordre"], ascending=False)
  a=a.drop(["ordre"], axis='columns')
  return a

#Recherche par titre (une fct qui retourne toute les infos d'un film donné)
def recherche_par_titre_AS(t):
  for i in titre:
    if i == t:
      print("Titre :"+t)
      print("Genre :"+genre[titre.index(i)])
      print("Description :"+desc[titre.index(i)])
      print("Avis :")
      print(grouper_par_avis(t))

recherche_par_titre_AS("Titans")

"""Recherche par description  en utilisant cosine"""

#L'indice de similarité cosine (avec le resultat de TfIdf) 
#une fct qui retourne toute les infos des dix films similaires à une description donnée
def tf_idf(query, description):
    query=preprocessing(query)
    desc_clean=[]
    for i in description:
       desc_clean.append(preprocessing(i))
    import numpy as np
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_desc = tfidf_vectorizer.fit_transform(desc_clean)
    q = tfidf_vectorizer.transform([query])
    cs = cosine_similarity(q, tfidf_desc)
    res= cs[0]
    result_list = [] #index
    sim = [] #similarité
    nb = 10
    while nb > 0:
        index = np.argmax(res)
        result_list.append(index)
        sim.append(res[index])
        res[index] = 0
        nb =nb - 1

    print("les 10 films similaires à votre query est:")
    for i,j in zip(result_list,sim):
            print("Titre :"+titre[i])
            s=int(j*100)
            print("score de similarité :"+str(s)+"%")
            print("Genre :"+genre[i])
            print("Description :"+desc[i])

tf_idf(desc[0],desc)

#L'indice de similarité cosine (avec le resultat de TF) 
#une fct qui retourne toute les infos des dix films similaires à une description donnée
def tf(query, description):
    import numpy as np
    query=preprocessing(query)
    desc_clean=[]
    for i in description:
       desc_clean.append(preprocessing(i))
    tf_vectorizer = CountVectorizer(binary=False, ngram_range=(1, 2))
    tf_desc = tf_vectorizer.fit_transform(desc_clean)
    q = tf_vectorizer.transform([query])
    cs = cosine_similarity(q, tf_desc)
    res= cs[0]
    result_list = [] #index
    sim = [] #similarité
    nb = 10
    while nb > 0:
        index = np.argmax(res)
        result_list.append(index)
        sim.append(res[index])
        res[index] = 0
        nb =nb - 1

    print("les 10 films similaires à votre query est:")
    for i,j in zip(result_list,sim):
            print("Titre :"+titre[i])
            s=int(j*100)
            print("score de similarité :"+str(s)+"%")
            print("Genre :"+genre[i])
            print("Description :"+desc[i])

tf(desc[0],desc)

"""Recherche par description en utilisant un algo supervisé

Avec TF (CountVectorizer)
"""

#Générer la matrice des poids des descriptions pour appliquer les algos
tf_vectorizer = CountVectorizer(binary=False)
tf_desc = tf_vectorizer.fit_transform(desc_clean)

#Générer les deux échantillons d'entrainement et de test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(tf_desc, genre, train_size = 0.75, random_state=40)

#Appliquer LogisticRegression sur la matrice de poids en modifiant le parametre de régularisation C pour un bon score d'Accuracy
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
for c in [0.01, 0.05, 0.25, 0.5, 1]:
    lr = LogisticRegression(C=c)
    lr.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" % (c, accuracy_score(y_test, lr.predict(X_test))))

#Appliquer SVC sur la matrice de poids en modifiant le parametre de régularisation C pour un bon score d'Accuracy
from sklearn.svm import LinearSVC
for c in [0.01, 0.05, 0.25, 0.5, 1]:
    svm = LinearSVC(C=c)
    svm.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" % (c, accuracy_score(y_test, svm.predict(X_test))))

#Appliquer l'arbre de décision sur la matrice de poids 
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
tr = DecisionTreeClassifier(criterion = "gini", random_state = 100,max_depth=3, min_samples_leaf=5)
tr.fit(X_train, y_train)
print ("Accuracy : %s" % accuracy_score(y_test, tr.predict(X_test)))

#Appliquer KNN sur la matrice de poids en modifiant le parametre K pour un bon score d'Accuracy
from sklearn.neighbors import KNeighborsClassifier
k_epoch=range(1,400,10)
for k in k_epoch:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    print ("Accuracy for K=%s: %s" % (k, accuracy_score(y_test, knn.predict(X_test))))

#quantifier les label pour appliquer naive_bayes
label=[]
for i in genre:
  if i == "Action" :
    label.append(1)
  if i == "Aventure" :
    label.append(2)
  if i == "Comedie" :
    label.append(3)
  if i == "Drame" :
    label.append(4)
  if i == "Medical" :
    label.append(5)  
  if i == "Police" :
    label.append(6)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(tf_desc, label, train_size = 0.75, random_state=40)

#Appliquer naive_bayes sur la matrice de poids 
from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train, y_train)
print ("Accuracy : %s" % accuracy_score(y_test, naive_bayes.predict(X_test)))

"""Avec TfIdf (TfidfVectorizer)"""

#Générer la matrice des poids des descriptions pour appliquer les algos
tfidf_vectorizer = TfidfVectorizer(binary=False)
tfidf_desc = tfidf_vectorizer.fit_transform(desc_clean)

#Générer les deux échantillons d'entrainement et de test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(tfidf_desc, genre, train_size = 0.75, random_state=40)

#Appliquer LogisticRegression sur la matrice de poids en modifiant le parametre de régularisation C pour un bon score d'Accuracy
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
for c in [0.01, 0.05, 0.25, 0.5, 1]:
    lr = LogisticRegression(C=c)
    lr.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" % (c, accuracy_score(y_test, lr.predict(X_test))))

#Appliquer SVC sur la matrice de poids en modifiant le parametre de régularisation C pour un bon score d'Accuracy
from sklearn.svm import LinearSVC
for c in [0.01, 0.05, 0.25, 0.5, 1]:
    svm = LinearSVC(C=c)
    svm.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" % (c, accuracy_score(y_test, svm.predict(X_test))))

#Appliquer l'arbre de décision sur la matrice de poids
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
tr = DecisionTreeClassifier(criterion = "gini", random_state = 100,max_depth=3, min_samples_leaf=5)
tr.fit(X_train, y_train)
print ("Accuracy : %s" % accuracy_score(y_test, tr.predict(X_test)))

#Appliquer KNN sur la matrice de poids en modifiant le parametre K pour un bon score d'Accuracy
from sklearn.neighbors import KNeighborsClassifier
k_epoch=range(1,400,10)
for k in k_epoch:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    print ("Accuracy for K=%s: %s" % (k, accuracy_score(y_test, knn.predict(X_test))))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(tf_desc, label, train_size = 0.75, random_state=40)

#Appliquer naive_bayes sur la matrice de poids
from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train, y_train)
print ("Accuracy : %s" % accuracy_score(y_test, naive_bayes.predict(X_test)))

#Meilleur cas l'indice de similarité cosine avec TfIdf
tf_idf(desc[0],desc)

"""Recherche par genre"""

#fct qui génére un score(moyenne des avis) d'un film donné en se basant sur l'analyse de sentiment des avis
def scorer_film(tit):
  res=[]
  sc=0
  from textblob import TextBlob
  from textblob import Blobber
  from textblob_fr import PatternTagger, PatternAnalyzer
  tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
  for i in range(0,len(titreR)):
       if titreR[i] == tit:
           text = tb(u""+avis[i])
           res.append(text.sentiment[0])
       elif len(res) != 0.0:
           sc = sum(res)/len(res)
  return round(sc,2)

#fct qui retourne les film d'un genre donné ordonné par un score d'analyse de sentiment
def scorer_par_genre(g):
  import pandas as pd
  film=[]
  score=[]
  for i in range(0,len(genre)):
    if (genre[i] == g) and (scorer_film(titre[i]) !=0.0) :
         film.append(titre[i])
         score.append(int(scorer_film(titre[i])*100))
  d={"Titre":film,"Score":score}
  df=pd.DataFrame(d)
  df=df.dropna(axis=0)
  df=df.sort_values(by=['Score'], ascending=False)
  df=df.iloc[0:10,]
  df=df.reset_index(drop=True)
  return df

scorer_par_genre("Action")

"""Recherche générale"""

#Le film le plus similaire a une description donnée si la requete entrante est une discription ou une partie de cette dérnière
def sim_desc(query):
  query=preprocessing(query)
  import numpy as np
  tfidf_vectorizer = TfidfVectorizer()
  tfidf_desc = tfidf_vectorizer.fit_transform(desc_clean)
  q = tfidf_vectorizer.transform([query])
  cs = cosine_similarity(q, tfidf_desc)
  ind=np.argmax(cs[0])
  print("Titre  : "+titre[ind])
  print("Description  : "+desc[ind])

sim_desc("guerre problème")

#Les bon films ordonés par analyse de sentiment des avis
def positive_film():
  res=[]
  ress=[]
  for i in titre:
    res.append(i)
    ress.append(int(scorer_film(i)*100))
  d={"Titre":res,"Score":ress}
  df=pd.DataFrame(d)
  df=df.dropna(axis=0)
  df=df.sort_values(by=['Score'], ascending=False)
  df=df.iloc[0:10,]
  df=df.reset_index(drop=True)
  df=df.drop_duplicates()
  return df

#Les mauvais films ordonés par analyse de sentiment des avis
def negative_film():
  res=[]
  ress=[]
  for i in titre:
    res.append(i)
    ress.append(int(scorer_film(i)*100))
  d={"Titre":res,"Score":ress}
  df=pd.DataFrame(d)
  df=df.dropna(axis=0)
  df=df.sort_values(by=['Score'])
  df=df.iloc[0:10,]
  df=df.reset_index(drop=True)
  df=df.drop_duplicates()
  return df

#fct qui retourne:
######Le titre si la requete entrante est un nom d'un film
######Les différentes films d'un genre donné grouper par analyse des avis si  la requete entrante est un genre
######Le film le plus similaire a une description donnée si la requete entrante est une discription ou une partie de cette dérnière
######Les bon films ordonés par analyse de sentiment des avis si la requete entrante est un avis positif 
######Les mauvais films ordonés par analyse de sentiment des avis si la requete entrante est un avis négatif
def recherche_generale(requete):
  from textblob import TextBlob
  from textblob import Blobber
  from textblob_fr import PatternTagger, PatternAnalyzer
  tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
  text = tb(u""+requete)
  res=text.sentiment
  if res[1] == 0.0 :
    for i in titre:
      if i == requete :
#        print("recherche par titre")
        return recherche_par_titre_AS(requete)
    for i in list(set(genre)):
      if i == requete :
#        print("recherche par genre")
        return  scorer_par_genre(requete) 
  elif (res[0] < 0.3 and res[0] > 0) or (res[0] > -0.3 and res[0] < 0) :
#    print("recherche par description")
    return sim_desc(requete)
  elif res[0] > 0.3 :
#    print("Positivité")
    return positive_film()
  elif (res[0] < int(-1*0.3)) :
#    print("Négativité")
    return negative_film()

desc[0]

recherche_generale("bon film")