#The program asks the user to input an intager value
#The program evaluates the value provided by the user and grades it accordingly
#The values provided must be between 0 and 100
#caution!!! if you provide other values other than ints the program will provide errors

marks=int(input("Please enter Students marks to Grade:"))

if marks >= 0:
    if marks >= 0 and marks <=20:
        print('The grade is E')
    elif marks >= 21 and marks <= 45:
        print('The grade is D')
    elif marks >= 46 and marks <= 55:
        print('The grade is C')
    elif marks >= 56 and marks <= 80:
        print('The grade is B') 
    elif marks >=81 and marks <=100:
        print('The grade is A')
    else:
        print('The value you entered is invalid')  
else:
    print('The value you entered is invalid')
print('Done. Thank you')                                             