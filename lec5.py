#import this


                        # Start of White Spacing Formatting
#print(  1+15+
#            4564    )
            
#1 + 2 + \
#12+456                  # End of White Spacing Formatting


                        # Start of is Operator
#a = [1,2,3]  
#b = [1,2,3]

#print(id(a))
#print(id(b))
#print(id([1,2,3]))

#print( a == b )

#print( a is b )

#a = 1
#b = 1 

#print(id(a))
#print(id(b))
#print(id(1))

#print( a == b )

#print( a is b )          # End of is Operator

                        # Start of None Type
#a = None

#print(id(a))
#print(id(None))

#print( a is None )
#print( a == None )       

#x = []
#print( x is None )

#x = ""
#print( x is None )

#x = None
#print( x is None )
                        # End of None Type

                        # Start of Boolean Type
#print( True and False )

#print( not True )

#print( not None )

#print( not '0')         # End of Boolean Type

                        # Start of Basic Comparison Operators
#print( 1 == 2 )

#print( 1 != 2 )

#print( 1 < 2 )          # End of Basic Comparison Operators

                        # Start of if Statement
if 2>1 : 
    print( "2>1" )
    
if 2<1 :
    print( "2>1" )  # Nothing will print out b/c it's false 
    
if 2>1 :                    # nested if statement
    print( "2>1" )
    print( 'another 2>1' )
    if 3>1 :
        print( '3>1' )
    
if 2<1 :                    # if statement with an else statement 
    print( "2>1" )
    print( 'another 2>1' )
    if 3>1 :
        print( '3>1' )
else:
    print( 'else statement' )
    
                        # Lines 91- 108 shows the difference of if and elif statements 
if 2>1 :                # if statement with elif in it
    print( '2>1' )
    
elif 3>1:
    print( '3>1' )
    
if 2>1 :                # Shows what the output is without the el part of elif
    print( '2>1' )
    
if 3>1:
    print( '3>1' )
    
if 2<1 :                # Shows what the output is when the if statement is wrong
    print( '2>1' )
    
elif 3>1:
    print( '3>1' )
#print( 'out of if block' )