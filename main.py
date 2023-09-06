# write your code here
person ={
'name':'dana',
'age':'16',
'hobbies':['table tennis','playing video games','sleeping']
}

print(f" my name {person['name']} , {person['age'] }")

person['age']= 0
person['country'] = 'kuwait'
print(person)
print(len(person))

person['hobbies'].append('designed')

def check_hobbies(person):
    if len(person)>= 3:
        print('wow youre amazing')

    else:
        print("try harder")    

check_hobbies(person)