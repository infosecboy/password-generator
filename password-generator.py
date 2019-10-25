#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: socialengineer100
"""
import random
def password_generator(n):
    
    Alph = [chr(x) for x in range(97,123)] + [chr(x) for x in range(65,91)]
    num = [str(x) for x in range(1,100)]
    sym = ['@','#','$','^','8','!',')','(','%',';',':','"','/','?']
    password = ""
    if n == "weak" or n == "WEAK":
        password = password + random.choice(Alph)
        password = password + str(random.choice(num))
        password = password + random.choice(sym)
    elif n =="strong" or n =="STRONG":
        password = password + ''.join(random.choices(Alph,k=5))
        password = password + ''.join(random.choices(num,k=2))
        password = password + ''.join(random.choices(sym,k=4))
    elif n  == "very strong" or n == "VERY STRONG":
        password = password + ''.join(random.choices(Alph,k=random.randint(5,25)))
        password =  password + ''.join(random.choices(num,k=random.randint(5,21)))
        password = password  + ''.join(random.choices(sym,k=random.randint(5,17)))
    else:
        print("Sorry only three choices exist no further more")
        password = ""
    return password


    
            
    
    
    



print("Enter how should be your password \n weak\nstrong\nvery strong")
n = input("Enter strength of password from choices given above: ")
print("Your random password is  "+password_generator(n))

