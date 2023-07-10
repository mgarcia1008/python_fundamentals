#create a function that accepts a number as an input, returna  new list that counts down
#by one from the number
def countdown(num):
    new_list=[]
    for i in range (num,-1, -1):
        new_list.append(i)
    return new_list 
print(countdown (5))

#create a function that will receive a list with two numbers. Print the first value and return the second
def list_return(my_list):
    print(my_list[0])
    return(my_list[1])
print(list_return([1,2]))

#create a function that accepts a list and returns the sume of the first value in the list
#plus the lists length
def first_plus_length(list):
    return(list[0] + len(list))
print(first_plus_length([1,2,3,4,5]))

#function that accepets a list & create a new list containing ont he values from the og list that are 
#greater than it's 2nd value. print how many values it is & return new list. If the list has less than 
#2 elements have the fucntion return False.
def greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list

print(greater_than_second([5,2,3,2,1,4]))
print(greater_than_second([3]))

#function that accepts two integers as parameters size and value. The function should create and
#return a list whose length is equal to the given size and whose values are all the given value
def length_value(size,value):
    list=[]
    for i in range (0, size): 
        list.append(value)
    return list
print(length_value(3,8))
print(length_value(8,3))