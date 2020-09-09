#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:37:59 2020

@author: chengyu
"""

from gensim.models import Word2Vec
import re 
 

class W2V(object):
    def __init__(self,w2v_path):
        self.model = Word2Vec.load(w2v_path)

    def get_most_similar(self,phrs,topn=10,words_only=True):
        """
        phrs: keyword you want to get similar words for 
        topn: how many words you want to return 
        model: w2v model 
        words_only: return only list of string, no similarities scores
        """
        if phrs in self.model.wv.vocab:
            # If the entire phrase is in the model's dictionary, get most simiilar
            res = self.model.wv.most_similar(phrs,topn=topn)
        else:
            # If the phrase can't be found in the model's dictionary        
            word_ls = re.split(',| |_|-',phrs)
            #print(word_ls)
            word_ls = [w for w in word_ls if w in self.model.wv.vocab] ## find out words in dictioary
            if len(word_ls) ==0: # None of the words are in the dictionary
                return [] 
            v_ls = [self.model.wv.get_vector(w) for w in word_ls]
            v = sum(v_ls) ## calcualte sum of vector
            res = self.model.wv.similar_by_vector(v,topn=topn)
     
        if words_only:  # if we want to return only words 
            res = [r[0] for r in res]
        
        return res
     
 
if __name__=='__main__':
    w2v_path = '../Data/model_weights/IMF_W2V/imf_160.w2v'
    w2v = W2V(w2v_path)

    res = w2v.get_most_similar('happy',topn=5)
    print(res)