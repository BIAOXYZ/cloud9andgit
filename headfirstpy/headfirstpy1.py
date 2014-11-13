# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 17:38:41 2014

@author: Administrator
"""

print "====================Page 34===================="
movies = ["The Holy Grail",
          "The Life of Brain",
          "The Meaning of Life"]
print "movies[1]"
print movies[0]
print movies[1]
print movies

print "====================Page 37===================="
cast=["Cleese",'Palin', 'Jones', "Idle"]
print cast   
print (cast)    # it seems that print(argument) = print argument
print (len(cast))  # len()
print (cast[1])

print "\n"

cast.append("Gilliam") # append()
print (cast)
cast.pop()    # pop()
print (cast)
cast.extend(["Gilliam","Chapman"]) # extend()
print (cast)

print "\n"

cast.remove("Chapman") # remove()
print (cast)
cast.insert(0,"Chapman") # insert()
print(cast)

print "====================Page 40===================="
movies.insert(1, "1975") # note the difference of 1975 and "1975"
print (movies)
movies.insert(3, 1979)
print (movies)
movies.insert(5, 1983) # It is equal to movies.append(1983)
print (movies)

print "\n"

movies = ["The Holy Grail", 1975,
          "The Life of Brain", 1979,
          "The Meaning of Life", 1983]
print (movies)