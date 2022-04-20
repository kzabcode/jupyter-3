def sqft():
    a = int(input('What is the length of the house? '))
    b = int(input('What is the width of the house? '))
    sq = a*b
    return(sq)

def cir():
    a = input('Do you know the radius OR diameter? ')
    if a == 'radius':
        r = float(input('What is the radius? '))
        b = str(3.14*(r*2))
        print('The circumference is ' + b)
    elif a == 'diameter':
        d = float(input('What is the diameter? '))
        c = str(3.14*d)
        print("The circumference is " + c)
    
   