'''

function

'''

                                    # Start of functions lecture
def cal_plus(input1, input2):
        #return input1+input2 another way to get the result
        
        result = input1+input2
        
        return result

#print(cal_plus(1,3))
#print(cal_plus(2,7))
                                    # End of functions lecture

                                    # Start of Argument and Parameters lecture
def cal_plus(input1, input2):
        #return input1+input2 another way to get the result
       # print(input1)   
        #print(input2)
        result = input1+input2
        
        return result

#print(cal_plus(1,3))
#print(cal_plus(2,7))

def cal_plus(input1, input2):
        #return input1+input2 another way to get the result
        #print(input1)   
        #print(input2)
        result = input1+input2
        
        return result

#print(cal_plus(input2=1,input1=3))
#print(cal_plus(2,7))

def cal_plus(input1, input2=0):
        #return input1+input2 another way to get the result
        print(input1)   
        result = input1+input2
        
        return result

#print(cal_plus(input2=1,input1=3))
#print(cal_plus(2,7))
                                    

# If you have an argument and you dont provide default values, you will get an error

                                    # End of Arugment and Parameters lecture
                                
                                    # Start of fruitful function
def cal_plus(input1, input2=0):
        #return input1+input2 
        print(input1)   
        result = input1+input2
        
        return result  # the return statement makes it a fruitful function

#print(cal_plus(input2=1,input1=3))
#print(cal_plus(2,7))

                                    # Start of Example 1
        
def cal_abs(a):
    if type(a) is str:
        return ('wrong datatype')
    elif a >0:
        return a
    else:
        return -a
#print(cal_abs(468))

                                    # End of Example 1
                                    
                                    # Start of Example 2
                                    
def cal_sigma(m,n):
    result = 0
    
    for i in range(n, m+1):
        result = result + i
        # n+ n+1 + n+2 .. +m
    return result
    
#print(cal_sigma(10,3))

def cal_pi(m,n):
    result = 1
    
    for i in range(n, m+1):
        result = result * i
        
    return result
    
#print(cal_pi(10,3))
                                    
                                    # End of Example 2

                                    # Start of Example 3
                                    
def cal_f(m):
    if m ==0:
        return 1
    else:
        return m * cal_f(m-1)
        
        
#print(cal_f(5))
                                    
                                    # End of Example 3
                                    
def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
    
print(cal_p(5,3))