''' 
lec3

list and set
'''

my_list = [1,2,3,4,5]

print(type(my_list)) #Data Container: List Lecture 

my_nested_list = [1,2,3,my_list]

print(my_nested_list)

my_list[0] = 6
print(my_list)

print(my_list[0])   # Start of Index Lecture

print(my_list[1])

print(my_list[-1])  # End of Index Lecture 

# print(my_list[5]) # due to their not being 6 items, it is out of range

print(my_list[1:3])  # Start of Slice Lecture

print(my_list[3:])

print(my_list[:3])

print(my_list[:])

print(my_list[0:1])  # End of Slice Lecture 

x,y,z = ['a','b','c'] # Start of Unpack Lecture

print(x,y,z) 

print(x) 

print(y)

print(z)              # End of Unpack Lecture

my_list.append(7)     # Start of List Methods Lecture
print(my_list)

my_list.remove(5)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list + [8,9])

my_list.extend([8,9])
print(my_list)

print('2' in my_list)  # comes out either 'true' or 'false'

print(len(my_list))  

print(len(my_nested_list))    # End of List Methods Lecture

print('hello\tworld')       # String is a Sequence of Character Lecture
print('hello\nworld')

print(len('hello world')) #11 Characters 

print('hello world.'[0:5])  # End of String is a Sequence of Charaacters Lecture

my_letters = ['a' , 'a' , 'b' , 'b' , 'c']  # Start of Set Lecture
print(my_letters)
print(set(my_letters))

my_letters_set = set(my_letters)
print(my_letters_set)
print('a' in my_letters_set)
print('d' in my_letters_set)

# print(my_letters_set[0]) you can't do this to get the index
print(list(my_letters_set)[0]) # you can do this to get the index
                                # End of Set Lecture


