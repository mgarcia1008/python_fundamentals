# basic - print all integer from 0 to 150
for i in range (151):
    print(i)

#Multiples of five - print all the multiples of 5 from 5 to 1,000
for i in range (5,1001,5):
    print(i)

#print integers 1-100. If divisible by 5 print coding if divisible by 10 print coding dojo
for i in range (1,101):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

#Add odd integers 0 to 500,000 and print the final sum 
sum = 0
for i in range (1,500001,2):
    sum += i
print(sum)

#print positive numbers starting at 2018 , counting down by fours
for i in range (2018, 0, -4):
    print(i)

#set three variables starting at lownum go through high num print only int that are multi
lowNum = 0
highNum = 20
mult = 5

for i in range(lowNum,highNum,mult):
    print(i)
