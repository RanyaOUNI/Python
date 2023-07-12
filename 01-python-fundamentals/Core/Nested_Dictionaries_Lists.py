# 1 ------ Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
 'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
 'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0]=15
print(x)

#2
students[0]["last_name"]="Bryant"
print(students)

#3
sports_directory["soccer"][0]="Sergio_Ramos"
print(sports_directory)

#4
z[0]["y"]=30
print(z)

# 2 ------ Iterate Through a List of Dictionary

students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
 ]

 #Function IterateDictionary

def IterateDictionary(list):
    for i in range(0,len(list)):
        print(f"first_name-{list[i]['first_name']}, last_name-{list[i]['last_name']}")

IterateDictionary(students)

# 3 ------ Get Values From a List of Dictionaries

def IterateDictionary2(key,list):
    for i in range(0,len(list)):
        print(f"")



# 4 ------ Iterate Through a Dictionary with List Values