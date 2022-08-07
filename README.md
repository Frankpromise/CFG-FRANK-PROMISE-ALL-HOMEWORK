# THEORY ASSESSMENT

## 1. How does Object Oriented Programming differ from Process Oriented Programming? 
 
a. Procedural programming follows a top-down approach. Object-oriented programming follows a bottom-up approach. 

b. Adding new data and functions to POP is not easy. Adding new data and functions to OOP is more easier. 

c. In procedural programming, overloading is not possible Overloading is possible in object-oriented programming. 

d. In procedural programming, there is no concept of data hiding and inheritance. In object-oriented programming, the concept of data hiding and inheritance is used. 

e. Procedural programming uses the concept of procedure abstraction. Object-oriented programming uses the concept of data abstraction. 

d. Code reusability absent in procedural programming. Code reusability present in object-oriented programming. 


## 2. What's polymorphism in OOP?

Polymorphism is the ability of an object to take on multiple forms. There are certain types of polymorphisms such as Compile Time Polymorphism and Runtime Polymorphism. Polymorphism causes operators and functions in many ways. It does its function through special mechanisms such as late binding or dynamic binding. 


## 3. What's inheritance in OOP? 

Inheritance means deriving a new class from an existing class. A class that inherits the properties is known as child class and the class whose properties are inherited is known as parent class (also called base class, superclass). One of the main advantages of using Inheritance is for code reusability and adding few or no existing features to the existing functionality. The syntax of implementing the inheritance is passing the parent class into child class using parenthesis while declaring the child class. 


## 4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people? 

 a. First thing is to design a class called Votes and create  a dictionary to take in name and vote  Counts for each candidate 

 b. Second is to create  the candidate method that will  ask for input of names of people  to vote for and  then assign each name to the dictionary key. Input from the user will be required three times. 

c.  Next, I would instantiate  another method that presents the three candidates in the dictionary and ask for users to vote for their favourite, then go further to increment the vote by 1 for each chosen candidate key. 

d.   Last, is to create a module that prints out the results of the vote based on the key-value pairs in the dictionary.


## 5. What's the software development cycle? 

SDLC is a process followed for a software project, within a software organization. It consists of a detailed plan describing how to develop, maintain, replace, and alter or enhance specific software. The life cycle defines a methodology for improving the quality of software and the overall development process. 


## 6. What's the difference between agile and waterfall? 

a. Waterfall is a Liner Sequential Life Cycle Model whereas Agile is a continuous iteration of development and testing in the software development process. 

b. Agile methodology is known for its flexibility whereas Waterfall is a structured software development methodology. 

c. Agile follows an incremental approach whereas the Waterfall is a sequential design process. 

d. Agile performs testing concurrently with software development whereas in Waterfall methodology testing comes after the “Build” phase. 

e. Agile allows changes in project development requirement whereas Waterfall has no scope of changing the requirements once the project development starts.


## 7. What is a reduced function used for?

The reduce function is used to apply a particular function passed in its argument to all the list elements mentioned in the sequence passed along. It works like this: 

a. First, two elements of sequence are picked, and the result is obtained. 

b. Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored. 

c. This process continues till no more elements are left in the container. 

d. The final returned result is returned and printed on console. 


## 8. How does merge sort work

Merge sort is a sorting technique based on divide and conquer technique. It is one of the most respected algorithms. It was like this: 

We take in an unsorted number of arrays. We know that merge sort first divides the whole array iteratively into equal halves unless the atomic values are achieved. We further divide these arrays, and we achieve atomic value which can no more be divided. Then the numbers are combined the same way they were broken down to achieve the result. 

 ## 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case? 

 a. To find the squared of numbers:
 
 ```
 def square_of_numbers(n): 
     for i in n: 
     yield(i*i) 
  
nums=square_of_numbers([5,25,30,50]) 
print(next(nums)) 
print(next(nums)) 
print(next(nums)) 
print(next(nums)) 
print(next(nums)) 
 ```
b. Another use case is for memory performance. Let’s compare the memory performance of a normal function with that of Generator, we will see that Generators consume less computation memory than normal functions.

```
import memory_profiler as mem_profile 

brand_name=[“Apple”,”Sony”,”Samsung”] 
price=[“90K”,”40K”,”30K”]
def product_list(n): 
 output=[] 
 for i in range(n): 
     product={“id”:i, 
     “Brand_name”:brand_name[0], 
     “Price”:price[0]} 
     output.append(product) 
 return output 
 
print(“Using Normal function”) 
print(‘Memory (Before): ‘ + str(mem_profile.memory_usage()) + ‘MB’ ) 
list_of_order=product_list(10000000) 
print(‘Memory (After): ‘ + str(mem_profile.memory_usage()) + ‘MB’ )Using Normal function 

# using generators

print(“Using generators”) 
brand_name=[“Apple”,”Sony”,”Samsung”] 
price=[“90K”,”40K”,”30K”] 
def product_list(n): 
 for i in xrange(n): 
 product={ 
 “id”:i, 
 “Brand_name”:brand_name[0], 
 “Price”:price[0] 
 } 
 yield productprint(‘Memory (Before): ‘ + str(mem_profile.memory_usage()) + ‘MB’ )  
list_of_order=product_list(5) 
print(‘Memory (After): ‘ + str(mem_profile.memory_usage()) + ‘MB’ )Using generators 

 
```
 

 

