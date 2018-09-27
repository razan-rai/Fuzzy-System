#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:34:39 2018

@author: razan
"""
#Lab 1
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:23:35 2018

@author: razan
"""

class FuzzySet:
    def __init__(self, iterable: any):
        for elem in self.f_set:
            if not isinstance(elem, tuple):
                raise TypeError("No tuples in the fuzzy set")
            if not isinstance(elem[1], float):
                raise ValueError("Probabilities not assigned to elements")

    def union(set1, set2):
        union_is = []
        for element1, member1 in set1:
            for element2, member2 in set2:
                if(element1 == element2):
                    if(member1 > member2):
                        union_is.append(tuple((element1, member1)))
                    else:
                        union_is.append(tuple((element2, member2)))
        return union_is
    
    def intersection(set1, set2):
        intersect = []
        for element1, member1 in set1:
            for element2, member2 in set2:
                if(element1 == element2):
                    if(member1 > member2):
                        intersect.append(tuple((element2, member2)))
                    else:
                        intersect.append(tuple((element1, member1)))
        return intersect
    def complement(sets):
        complemet = []
        for element1, member1 in sets:
            comp = 1.0 - member1
            complemet.append(tuple((element1, comp)))
        return complemet
            
    def height(sets):
        return max(sets,key=lambda item:item[1])[1]
    
    def check_normal(sets):
        if(item for item in sets if 1.0 in item):
            return 'Yes'
        else:
            return 'No'
    
    def alfa_cut(alfa_value, sets):
        alfa_cut = []
        for element1, member1 in sets:
            if(member1 >= alfa_value):
                alfa_cut.append(element1)
        if not alfa_cut:
            return 'Empty'
        else:
            return alfa_cut
    
    def support(sets):
        support = []
        for element1, member1 in sets:
            if(member1 > 0.0):
                support.append(element1)
        if not support:
            return 'Empty'
        else:
            return support
    
    def core(sets):
        core = []
        for element1, member1 in sets:
            if(member1 == 1.0):
                core.append(element1)
        if not core:
            return 'Empty'
        else:
            return core
    
    def boundary(sets):
        boundry = []
        for element1, member1 in sets:
            if(0.0 < member1 < 1.0):
                boundry.append(element1)
        if not boundry:
            return 'Empty'
        else:
            return boundry

    


            
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
    
obj = FuzzySet

# =============================================================================
# fuzzyset1 = [('a', 0.0), ('b', 0.8), ('c', 1.0), ('d', 1.0)]
# fuzzyset2 = [('a', 0.0), ('b', 0.6), ('c', 0.50)]
# =============================================================================

print('Fuzzy set 1:', fuzzyset1)
print('Fuzzy set 2:', fuzzyset2)

#Union of fuzzy set 1 and fuzzy set 2
print('Union of fuzzy set A and B: ', obj.union(fuzzyset1, fuzzyset2))

#Intersection of fuzzy set 1 and fuzzy set 2
print('Intersect of fuzzy set A and B: ', obj.intersection(fuzzyset1, fuzzyset2))

#Complement of Fuzzy sets
print('Complement of fuzzy set A: ', obj.complement(fuzzyset1))
print('Complement of fuzzy set b: ', obj.complement(fuzzyset2))

#Height and check for normal
print('Height of fuzzy set A: ', obj.height(fuzzyset1))
print('Is Fuzzy set A Normal: ', obj.check_normal(fuzzyset1))
print('Height of fuzzy set B: ', obj.height(fuzzyset2))
print('Is Fuzzy set B Normal: ', obj.check_normal(fuzzyset2))

#input for alfa value and computation of alfa cut
alfa_value = float(input('Enter the alfa value:'))
print('Alpha cut of set 1: ', obj.alfa_cut(alfa_value, fuzzyset1))
print('Alpha cut of set 2: ', obj.alfa_cut(alfa_value, fuzzyset2))

#Computing Support of fuzzy sets
print('Support of set 1: ', obj.support(fuzzyset1))
print('Support of set 2: ', obj.support(fuzzyset2))

#Computing Core of fuzzy sets
print('Core of set 1: ', obj.core(fuzzyset1))
print('Core of set 2: ', obj.core(fuzzyset2))

#Computing Boundary of fuzzy sets
print('Boundary of set 1: ', obj.boundary(fuzzyset1))
print('Boundary of set 2: ', obj.boundary(fuzzyset2))

