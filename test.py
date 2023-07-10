# declare a class and give it name Shoe
class Shoe:		
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
        self.price = 69.99
        self.in_stock = True
        skater_shoe = Shoe()
        dress_shoe = Shoe()
        print(skater_shoe.type)
        print(dress_shoe.type)

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

drawers = ['documents', 'envelopes', 'pens']
drawers[1] = 'sparkley gel pens'
print(drawers)
drawers.append('stamps')
print(drawers)

top_contents = drawers[0]
print(top_contents)

'''my_list = [1, 85, 32,10,8, 100]
my_list.reverse
print(my_list)'''

for greeting in 'hello':
    print(greeting)

#could also do this
word = 'hello'
for greeting in word:
    print(greeting)

my_list = ['abc', '123', 'xyz']
for example in range (len(my_list)):
    print(example, my_list[example])

countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

for integer in range(len(countries)):
    print("Index", integer)
    # Challenge 2: print the index here
    print("Country:", countries[integer])
    # Challenge 3: print the country here
 
# Looping over values only...
for country in countries:
    print("Country", country)
    # Challenge 4: print the country here

#for loop
for count in range(0,5):
    print("looping =", count)

#while loop
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

#else statement
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

def add (a,b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

print(sum1)
print(sum2)
print(sum3)

def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list

a = [2,4,10,16]
b = multiply(a,5)
print(b)

capitals = {"Washington":"Olympia",
            "California":"Sacramento",
            "Idaho":"Boise",
            "Illinois":"Springfield",
            "Texas":"Austin",
            "Oklahoma":"Oklahoma City",
            "Virginia":"Richmond"
            }
for key, val in capitals.items():
    print(key, '=', val)

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}
print(resume_data["skills"][1])
print(users[2]["first"])















