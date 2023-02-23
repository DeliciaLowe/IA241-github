'''
lecture 6

for loop
range function

'''
                        # Start of for loop lecture
#for num in [1,2,3]:
    #print(num)
    #print(num+1)
    
#for c in 'this is lec6'.split():
    #print(c)
    
#for num in [1,2,3]:
    #if num >1:
        #print(num)
        
#for word in 'this is lec6'.split() :
    #print(word)
    #for c in word:
        #print(c)
                        # End of for loop lecture
                        
                        # Start of range() function lecture
#for i in range(5):
    #print(i)
    
#for i in range(1,5):
    #print(i)
    
#for i in range(1,5,2):
    #print(i)
                        # End of range( function lecture)

                        # Start of Breakpoint lecture
                        # right click the line # to add breakpoint
                        # then click debugging mode (where the output code is)
                        # pulls up a window that helps us understand the code
                        # hit the step over then step into
#for i in range(1,5,2):
    #print(i)
    
#for i in range(1,5):
    #print(i)
                        # End of Breakpoint lecture
                        
                        # Start of Algorithm lecture
num_list = [123,434,43243,23432,4324]

possible_max_num = num_list[0]

for num in num_list:
    if num > possible_max_num:
        possible_max_num = num

print(possible_max_num)    
                        # End of Algorithm lecture