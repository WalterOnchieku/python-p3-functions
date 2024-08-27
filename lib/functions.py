#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    

def greet(name):
    print(f"Hello, {name}!")
    return
greet("Guido")

    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    return
greet_with_default("Guido")
    

def add(num1, num2):
    return(num1+num2)

def halve(number):
    return(number/2)
