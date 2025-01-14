# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
# Assignment_01
#
# Drew Cragin
# University of Central Florida
#
# January 13, 2024
#
##################################################
"""
def trick(times_out):
    # (a) Pick the number of times you'd like to eat out in a week
    times_out = 5
    
    # (b) Multiply the number by 2
    times_out *= 2
    
    # (c) Add 5
    times_out += 5

    # (d) Multiply the result by 50
    times_out *= 50
    
    # (e) Add 1749 since we have not had a birthday yet
    times_out += 1749
    
    # (f) Add the last digits of the current year, 25 for 2025
    times_out += 25
    
    # (g) Subtract the year I was born, 2001
    times_out -= 2001
    
    # (h) Number returned should be original number followed by age
    print(times_out)
     
"""
Function could also be written as

def trick(times_out):
    return (((times_out * 2) + 5) * 50) + 1749 + 25 - 2001
    
print(trick(5))
"""
