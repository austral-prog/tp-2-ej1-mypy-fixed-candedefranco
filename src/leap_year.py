# Replace the "ANSWER HERE" for your answer

def is_leap_year() -> None:
    input1 : int = int(input('Ingrese un año: '))
    if (input1 % 100 == 0) and (input1 % 400 == 0):
        print (f'El año {input1} es bisiesto')
    elif input1 % 4 == 0:
        if (input1 % 100 == 0):
            print (f'El año {input1} no es bisiesto')
        else:
            print (f'El año {input1} es bisiesto')
    else:
        print (f'El año {input1} no es bisiesto')
    

