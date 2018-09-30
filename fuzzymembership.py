#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:05:57 2018
Lab 2
@author: razan
"""
class FuzzyMembership:
    
    def fuzzysets():
        num_element1 = int(input('Enter number of Elements in the set: '))
        i = 1
        fuzzyset1 = []
        for count in range (0, num_element1):
            element1 = float(input('Enter a element: '))
            i += 1
            fuzzyset1.append(element1)
            
        alfa = float(input('Enter the Alfa value: '))
        beta = float(input('Enter the Beta value: '))
        return fuzzyset1, alfa, beta
    
    def r_function():
        fuzzeyset1, alfa, beta = obj.fuzzysets()
        r_function = []
        for x in fuzzeyset1:
            if(x <= alfa):
                r_function.append(tuple((0, x)))
            elif(alfa < x < beta):
                res = (x - alfa)/(beta - alfa)
                r_function.append(tuple((res, x)))
            elif(beta <= x):
                r_function.append(tuple((1, x)))
            else:
                pass
        print('The R_function is:', r_function)
        
    def l_function():
        fuzzeyset1, alfa, beta = obj.fuzzysets()
        l_function = []
        for x in fuzzeyset1:
            if(x <= alfa):
                l_function.append(tuple((1, x)))
            elif(alfa < x < beta):
                res = (x - alfa)/(beta - alfa)
                l_function.append(tuple((res, x)))
            elif(x >= beta):
                l_function.append(tuple((0, x)))
        print('The L_function is:', l_function)
        
    def trangular():
        fuzzeyset1, alfa, beta = obj.fuzzysets()
        gama = float(input('Enter the Gama value: '))
        t_function = []
        for x in fuzzeyset1:
            if(x <= alfa):
                t_function.append(tuple((0, x)))
            elif(alfa < x < beta):
                res = (x - alfa)/(beta - alfa)
                t_function.append(tuple((res, x)))
            elif(beta < x < gama):
                res2 = (x - beta)/(gama - beta)
                t_function.append(tuple((res2, x)))
            elif(x >= gama):
                t_function.append(tuple((0, x)))
        print('The Trangular Function is:', t_function)
            
        
    def trapezoidal():
        fuzzeyset1, alfa, beta = obj.fuzzysets()
        gama = float(input('Enter the Gama value: '))
        sigma = float(input('Enter the Sigma value: '))
        s_function = []
        for x in fuzzeyset1:
            if(beta <= x <= gama):
                s_function.append(tuple((1, x)))
            elif(alfa < x <= beta):
                res = (x - alfa)/(beta - alfa)
                s_function.append(tuple((res, x)))
            elif(gama < x < sigma):
                res2 = (x - gama)/(sigma - gama)
                s_function.append(tuple((res2, x)))
            elif(x <= alfa):
                s_function.append(tuple((0, x)))
            elif(x >= sigma):
                s_function.append(tuple((0, x)))
        print('The Trapezoidal Function is:', s_function) 
        
    def switcher(choice):
        if(choice <= 4):
            print('The choice is:', choice)
            if(choice == 0):
                obj.r_function()
                return True
            elif(choice == 1):
                obj.l_function()
                return True
            elif(choice == 2):
                obj.trangular()
                return True
            elif(choice == 3):
                obj.trapezoidal()
                return True
            else:
                return False
        else:
            print('Your choice is Out of Range. Please choose from list')
            return True
        
        
obj = FuzzyMembership

running = True
while running:
    print('Fuzzy Membership Function List:')
    print(' R-Function : 0\n L-Function : 1\n Trangular : 2\n Trapezoidal : 3')
    switch = int(input('To calculate, choose the corresponding number:'))
    #switch to the corresponding choice
    status = obj.switcher(switch)
    running = status
