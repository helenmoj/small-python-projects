# creating star patterns using turtle module in python.

from turtle import *
import random
speed(speed='fastest')
def draw(n, x, angle):
    #23 loop for number of stars
    for i in range(n):
        colormode(255)
