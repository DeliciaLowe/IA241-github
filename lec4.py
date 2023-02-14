'''
lec4
dict and tuple
'''

my_tuple = 'a','b','c','d','e'  # Start of Tuples Lecture

print(my_tuple)

#my_tuple = ('a')
#print(type(my_tuple))

print(my_tuple[0:2])

#my_tuple [0] = 'f'
#print(my_tuple[0])             # End of Tuples Lecture
                                # Start of Dictionary Lecture
my_car = {
    'color': 'red',
    'maker':'toyota',
    'year': 2015
}                               # End of Dictionary Lecture

print(my_car['color'])          # Start of Dictionary Methods Lecture
print(my_car['year'])

print(my_car.items())
print(my_car.keys())

print(my_car.get('color'))
print(my_car['color'])

my_car['model'] = 'venza'

print(my_car)               

my_car['year'] = 2020

print(my_car)

print( len(my_car)    )
print( 'color' in my_car)
print( 'red' in my_car)
print( 'red' in my_car.values())    # End of Dictionary Method Lecture
