"""
QUESTION1:

1. A thread is a small sequential flow of control in a program that allows the
program to run a sequence of instructions. Multithreading is a complex
model that allows the execution of multiple sequences of instructions
simultaneously.

2. Concurrency is when a program or application processes more than one
task at the same time, and Parallelism is when an application divides big
tasks into smaller tasks and run them simultaneously. The difference
between them is that concurrency runs and manages multiple programs
at the same time while parallelism does it simultaneously through multiple
processing units.

3. A garbage collector is a built-in memory manager. In Python, for example,
its a process that automatically finds and delete objects that can’t be
reached and/or objects that are no longer wanted to free up memory
space. The process is triggered when an object’s reference count reaches
zero.

4. Its tasks of managing multiple transactions issued by clients of a
database server. It is done through a set of T-SQL statements that are run
together as a single unit in a particular order. The transactions will be
considered complete if the statements are executed successfully and then
it is committed that saves the data permanently.

Example:
    START TRANSACTION
    INSERT INTO TABLE Values(value1, value2, value3)
    commit;

5. An endpoint is a digital point at which an API connects with the software
program, its where the API receives requests for information on it’s
server. Its typically a URL that provides location of specified information
on the server.

6. Normalization is a process of organizing a data in a database through the
creation of tables and finding relationships between them and applying
rules that protect the data and making the database more flexible by
getting rid of redundancy and dependency.

"""

"""
Question 2
An exception is when an error occurs at the time of execution of code, Python generates an exception that must be handled to avoid the program to crash. The exceptions automatically trigger on errors, or they can be triggered by code. 
Some of the common errors are division by zero, trying to access non-existent files, 
value errors etc. 
In Python Error handling is managed by try, except, and finally keywords or we can raise an exception by using the raise exception statement. Raising an exception stops code execution and goes back until the error is handled. 
Debugging is the process of writing code that can help to find what is going in a program. 
It's done by executing code at any prescribed line number, print out variables, continue execution, stop again, execute statements one by one, and repeat such actions until the abnormal behaviour has been tracked down and found the bugs.
"""

"""
Question 5:

Scrum master - this is the person who is responsible for ensuring that 
Scrum is thoroughly understood by an agile team.  They server both the 
development team and the product owner by helping the product owner 
to manage the sprint backlog and ensuring the team understand the 
product owner's requests. 

-The development team - is made up of specialists who carry out the 
required work to deliver a solution at the end of each sprint. This team 
consist of all the skills that are necessary to deliver a project, and 
sometimes that includes a Business Analyst. 

- The product owner is the individual or organization on the receiving end 
of the solution. They are solely responsible for decisions about the product
backlog including the prioritization of items and making sure the team 
understands requirements and deciding when the job is done.
"""

"""
Question 9
BREAKING DOWN THE PROBLEM:
let's assume 10 is the target number which 2 numbers in the array will sum upto.
 if 10 is the target sum, then,
 10 = x + y
also,
y = 10 - x

The solution will look like this:

The function takes in 2 parameters, which is an array and a target sum.
for the number in the length of the number of arrays - any number,
for the number in range of number + any number, length of array,
if array of that number plus the array of the second number is == target sum, then the function will return the sum
of both numbers in a list.

Also, the function will return an empty list if there isn't any number to be summed up.
"""

"""
Question 7:

Python db cursor is used to execute sql statments that will communicate with mysql database. 

Example:
import mysql.connector

context = mysql.connector.connect(
   user='root', password='password', host='localhost', database='mydb'
)
cursor = context.cursor()
"""


def sum_of_two_numbers(arr, target_sum):
    for i in range(len(arr) - 1):
        for d in range(i + 1, len(arr)):
            if arr[i] + arr[d] == target_sum:
                return [arr[i], arr[d]]
    return []


print(sum_of_two_numbers([1, 2], 3))

"""
8. 
- sql to find the maximum number:

select 
       max(purch_amt) max_purchase
       customer_id
from ORDERS
where customer_id between 3002 and 3007
GROUP BY customer_id
having max_purchase > 1000

- 
"""

"""

Question 4:
BREAKING DOWN THE PROBLEM:
The function we take in 2 parameters.
for int that will be in the range of the second paramter, i want that the multiplication
of the number will be equall to the number. then i sort the number.

Then i will go further to iterate through the len of a n number to get the before and after sort

"""


def number_squared(arrays, num):
    for i in range(num):
        arrays[i] = arrays[i] * arrays[i]
    arrays.sort()


arr = [-1, 12, 3, -2, 8]
n = len(arr)

print('before sorting')
for i in range(n):
    print(arr[i], end=" ")
print('\n')

number_squared(arr, n)
print('after sorting')
for i in range(n):
    print(arr[i], end=" ")

"""
QUESTION 6:

TDD is a practice of writing test before writing code. The advantages of 
doing this include helping programmers to analyse and understand 
owner's requests more clearly and making testing new functions much 
easier in latter stages of the development. TDD also leads to development
of a code that is flexible and easier to maintain. The problem with writing 
tests without code is that its time-consuming and can be challenging to 
cover all the code you are going to write and likely wont catch all the 
bugs.
"""

""""
Question 5
"""


def validate_num(arr):
    if arr != int[arr]:
        raise TypeError('expected integers')


import unittest
from unittest import TestCase, main


class TestFunction(TestCase):
    def test(self):
        expected = [1, 2, 3, 4]
        result = validate_num(arr=['a', 'b'])


if __name__ == "__main__":
    main()
