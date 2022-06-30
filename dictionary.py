students={
    'name' : 'sejan',
    'age' : 26,
}
print(students)
print(students['name'])
print(students.keys())
print(students.values())
print(students.get('email','Not Found'))
students['email']='sejan157218@gmail.com';
students['age']='26.5 years';
print(students)
print(students.pop('email'))
students['email']='sejan157218@gmail.com';
print(students)
print(len(students))


for i in students:
    print(i)
    print(students[i])
for i in students.items():
    print(i)
    print(i[1])

