#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:09:06 2018

@author: razan
"""

#WAP to create any two fuzzy set and a fuzzy relation from the fuzzy sets

class FuzzyRelation:
    def chunkIt(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
        return out
        
    def fuzzyrelaion(set1, set2):
        union_is = []
        for element1, member1 in set1:
            for element2, member2 in set2:
                minimum = min(member1, member2)
                union_is.append(minimum)
        return union_is
    
    def alfacut(relation, alfa_cut):
        
        union_is = []
        for element in relation:
            if(element >= alfa_cut):
                union_is.append(1)
            else:
                union_is.append(0)
        return union_is
        
    def strictalfacut(relation, alfa_cut):
        union_is = []
        for element in relation:
            if(element > alfa_cut):
                union_is.append(1)
            else:
                union_is.append(0)
        return union_is
    
    
num_element1 = int(input('Enter number of Elements for fuzzyset 1: '))
i = 1
fuzzyset1 = []
for count in range (0, num_element1):
    fuzzy_set = input('Enter a Fuzzy set: ')
    membership_value = float(input('Enter a membership value: '))

    if 0 <= membership_value <= 1:
        i += 1
        fuzzyset1.append(tuple((fuzzy_set, membership_value)))
    else:
        print("The membership value of a fuzzy set should be between 0 and 1")
        break
    
num_element2 = int(input('Enter number of Elements for fuzzyset 2: '))
i = 1
fuzzyset2 = []
for count in range (0, num_element2):
    fuzzy_set = input('Enter a Fuzzy set: ')
    membership_value = float(input('Enter a membership value: '))

    if 0 <= membership_value <= 1:
        i += 1
        fuzzyset2.append(tuple((fuzzy_set, membership_value)))
    else:
        print("The membership value of a fuzzy set should be between 0 and 1")
        break
    
obj = FuzzyRelation
# =============================================================================
# fuzzyset1 = [('a', 0.2), ('b', 0.3), ('c', 0.4)]
# fuzzyset2 = [('a', 0.4), ('b', 0.5), ('c', 0.6), ('d', 0.8)]
# =============================================================================
#fuzzy  relation ie matrix
fuzzyrelation = obj.fuzzyrelaion(fuzzyset1, fuzzyset2)
print('Fuzzy set 1: ', fuzzyset1)
print('Fuzzy set 2: ',fuzzyset2)
print('The Fuzzy relation is:', fuzzyrelation)
print('matrix form: ', obj.chunkIt(range(len(obj.fuzzyrelaion(fuzzyset1, fuzzyset2))), len(fuzzyset1)))
#alfa cut of fuzzy relation
alfa_cut = float(input('Enter the alfa cut: '))
print('Alfa cut of a fuzzy relation: ', obj.alfacut(fuzzyrelation, alfa_cut))
print('Strict Alfa cut of a fuzzy relation: ', obj.strictalfacut(fuzzyrelation, alfa_cut))
