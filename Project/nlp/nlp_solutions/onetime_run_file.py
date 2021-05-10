import sklearn.externals
import joblib
import pandas as pd
import os,sys
sys.path.append(os.path.normpath(os.getcwd()))

from config import onetime_file
from nlp.nlp_solutions.nlplearn import *

if __name__ == "__main__":
    
    metadata = pd.read_csv('data/metadata_prep.csv')

    #Metadata based collobarative filtering      
    
    documents = metadata['overview'].fillna('')
    cosine_sim = metadata_filtering(documents)
    indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

    #Title search based on Keywords##
    
    documents = list(metadata['title'].fillna(''))
    tfidf_fit, tfidf_matrix = tfidf_fit(documents)
    
    #dump the variables to a text file
    
    i = [cosine_sim,indices,tfidf_fit, tfidf_matrix]
    joblib.dump(i,onetime_file)
    
    
