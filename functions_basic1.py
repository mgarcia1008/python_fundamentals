#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#print 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#print undefined bc number of days in the week...isn't defined
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#print 5 and not 10 bc once the function is executed in the first return statement it exits the fuction


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#print 5 for the same reason above the print statement will not be executed bc of the return statement above

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#print 5 will print to console when the function is called by x there is no value so null/none will print

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#print 3,5 but the addition on line 37 will not add 3+5 because all line 36 does is print to console doesnt return any value

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#str makes b and c strings not numbers when we pass 2,5 into the return statement it returns string 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#print 100, 10 would be the return/held value

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#print return 7,return 14, 7+14=21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#print 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#print 500 (lines 79-80), 300(I dont think this will print to the console bc its not returned), 500 (line 84 outside of the function),300, 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#print 500 (line91), 500 (line96), 300, 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#print 500 (line103),500 (line108), 300 line 109 function call with variable so the return value is held and changes b to 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#print 1 foo called line 120, move to bar one lime 18 there is function so print 3 gp up to line 116 and print 2 so it's 1,3,2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#print y = foo on line 132 execute line 124 which will print 1, line 126 is calling function def bar so we go to line 129, which prints 3 but return 5 and make print x 5, return 10 which is y so its 1,3,5,10









