'''
Define a value-returning function celsius_to_fahrenheit(temp) that converts the parameter
temp from celsius to fahrenheit (To convert temperatures in degrees Celsius to Fahrenheit,
 multiply by 1.8 (or 9/5) and add 32.)
'''


celsius = 0

def main():
    celsius_to_fahrenheit()
    

def celsius_to_fahrenheit():
    celsius = float(input('input a temp in celsius: '))
    celsius = (celsius * 1.8) + 32
    return celsius
    #print(celsius,'in Fahreheitis: ', format(celsius,'.2f'))
main()

'''
Define a value-returning function max(x, y, z) that takes three integers and returns the largest of them
'''


def main():
    max_return(4, 5, 100)

def max_return(x,y,z):
    if x > y:
        if x > z:
            print(x)
        else:
            print(z)
    elif y > z:
        print(y)
    else:
        print(z)
main()


'''
Define a void function called digit_sum(num) that adds up all the digits of a number and prints it on the screen.
'''


def main():
    digit_sum(num)


num = float(input('enter a number and ill tell you what they add up to'))
def digit_sum(num):

    total = 0
    while num != 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    print('Your total is:', total)
main()








