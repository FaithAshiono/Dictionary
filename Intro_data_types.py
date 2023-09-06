#workin gwith strings
print('My name is Faith Ashiono')

#defining variables
law = ('Happy birthday to me')
print(len
      (law))

#modifying strings
b= 'We are learning data types'
print(b)
print(b.upper())#function should be in bracket

#string concatenation
a='Beautiful'
b= 'day'
c=a+" "+b
print(c)


#list data type
students = ["Micah", "Jackline", 'Rahab', "Brian", "Lorna", "Vincent",
            "Iscah"]
print(students[:4])#first 4
print(students[4:])#last 4

#change list items
students = ["Micah", "Jackline", 'Rahab', "Brian", "Lorna", "Vincent",
            "Iscah"]
students[1]= 'Gustave'
print(students)

#insert items
students = ["Micah", "Jackline", 'Rahab', "Brian", "Lorna", "Vincent",
            "Iscah"]
students.insert(2, 'Caleb')
print(students)

#append items
students = ["Micah", "Jackline", 'Rahab', "Brian", "Lorna", "Vincent",
            "Iscah"]
students.append('Faith')
print(students)

students.remove('Jackline')
print(students)

##TUPLES

mytuple = ("Rahab", "Faith", "Evans", 3.14, 99, "Joshua")

#mytuple[0]= "Jackline"
#print(mytuple)
print(mytuple[2])
print(mytuple[2:])#starts from item index 2 to the last
print(mytuple[:2])#prints the first before index 2
print(mytuple[:])#prints the whole tuple
print(mytuple[:4])#prints the first elements excluding element index 4
print(mytuple[1:4])#prints from element of index 1 to index 3 excluding index 4


##DICTIONARIWS
Bikes = {
    "Brand": "BMW",
    "Model": "GRS",
    "Year": 2000
}

cars = {
    "Brand": "Toyota",
    "Model" :"Landcruiser",
    "Year" : 2020

}

print(cars , Bikes)  


#CONDITIONAL STATEMENTS

x = int(input("What is x?"))

y = int(input("What is y?"))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")   

elif x == y:
    print("x is equal to y")