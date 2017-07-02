#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
# -*- coding: utf-8 -*-
"""
Created on 02/Jul/2017 with PyCharm Community Edition
@title:  IMIR - exception
@author: rafaenune - Rafael Nunes - rnunes@cos.ufrj.br

"""

# try:
#     a = 2/0
# except Exception as e:
#     print(e.__doc__)
#     print(e.message)

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
