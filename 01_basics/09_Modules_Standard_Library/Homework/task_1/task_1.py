'''Imports practice

Make a directory with 2 modules;
 make a function in one of them; then import this function in the other module and use that in your script of choice.'''

from tools import custom_function as cf

cf(5, 6.0, 'a', first=1, second='b', third=3.14)