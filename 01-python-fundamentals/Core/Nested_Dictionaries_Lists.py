
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

students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
 ]

def IterateDictionary2(key_name,list):
    
     for student in list:
        print(f"{student[key_name]}")
        
        
IterateDictionary2('first_name',students)


# 4 ------ Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#printInfo(dojo)

def printInfo(dict):
    
    for key,value in dict.items():
        print(f"{len(value)} {key}")
        for i in range(0,len(value)):
            print(value[i])

printInfo(dojo)






