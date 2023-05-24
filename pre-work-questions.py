# Question 1
# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function.
def hello_name(user_name):
     """Display a simple greeting."""
     print("hello, " + user_name.title() + "!")

hello_name('ronnie')

# Question 2
# Write a python function first_odds that prints
# the odd numbers from 1-100 and returns nothing.

def first_odds(odd_numbers):
     """Print odd numbers 1-100 and return nothing."""
     odd_numbers = odd_numbers
     for value in range(1, 101, 2):
         print(value)

# Question 3
# Please write a Python function, max_num_in_list to
# return the max number of a given list.

def max_num_in_list(a_list):
     """Return the max number in a list."""
     max_number = a_list
     if a_list:
          print(max(max_number))

a_list = ['1','2','3','4','5','6','7','8','9']
max_num_in_list(a_list)

# Question 4
# Write a function to return if
# the given year is a leap year
# A leap year is divisible by 4, but not divisible
# by 100, unless it is also divisible by 400.
# The return should be boolean type (True/False)

def is_leap_year(a_year):
     """Return if a given year is a leap year"""
     if a_year % 400 == 0:
          print("This is a leap year!")
     elif a_year % 100 == 0:
          print("This is not a leap year!")
     elif a_year % 4 == 0:
          print("This is a leap year!")
     else:
          print("This is not a leap year!")

a_year = int(input("Enter the date and I will tell you" +
                   " if it is a leap year or not."))
is_leap_year(a_year)

# Question 5
# Write a function that checks to see if all
# numbers in a list are consecutive numbers.
# [1,2,3,4,5] are consecutive numbers,
# [1,2,8,5,7] are not consecutive numbers.
# Return should be boolean type (True/False)

def is_consecutive(numbers):
     """Check if numbers are consecutive or not."""
     for numbers in numbers:
               return 0+1
          
               print(is_consecutive(1,3,5,7,2))
