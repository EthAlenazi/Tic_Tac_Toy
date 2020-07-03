name = input( "Enter you name :" )


def star():
    print( star() + "*1 =" + num1 * 1 )
    print( num1 * 2  )
    print( num1 * 3)
    print( num1 * 4 )
    print( num1 * 5)
    print( num1 * 6 )
    print( num1 * 5 )
    print( num1 * 6 )
    print( num1 * 7 )
    print( num1 * 8 )
    print( num1 * 9 )
    print( num1 * 10  )
    print( num1 * 11)
    print( num1 * 12 )


print( "welcome to our program " + name + "\n " )
print( "do you want to get Multiplication table ? " )
print( "Enter 1 if ur answer yes , otherwise 2 to exit program " )
answer = int( input( "u r answer is : \n" ) )
if answer == 1:
    num1 = int( input( "Enter the number you want to get Multiplication table ? \n" ) )
    print( " ----------------------- " )
    star( )

else:
    print( "thank u " )
