from random import *
import os

your_pas=input("Enter the password")
pw=""
pwd=['a','b','c','d','e','f','g''h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
while pw!=your_pas:
    pw=""
    for letter in range(len(your_pas)):
        guess=pwd[randint(0,25)]
        pw=str(guess)+str(pw)
        print(pw)
print(f"your password is:{pw}")