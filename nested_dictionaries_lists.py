#1 Update values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1a. change value 10 in x to 15
x[1][0] = 15
print(x)

#2b Change the last_name of the first student from Jordan to Bryant
students[0]['last_name'] = 'Bryant'
print(students)

#3c In sports_directory change Messi to Andres
sports_directory['soccer'][0] = 'Andres'
print(sports_directory) 

#4d Change the value 20 in z to 30
z[0]['y'] = 30
#z[0] is the whole line of code so how do I change y I needed to access it but simply putting y

#2 Iterate through a list of dictionaries -Create a function iterateDictionary(some_list) that
#given a list of dictionaries, the function loops through each dictionary in the list and 
#prints each key and the associated value.

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for index in range(len(students)):
    print(students[index])
