# Replace the "ANSWER HERE" for your answer

def is_leap_year() -> bool:
    input1 : int = int(input('Ingrese un año: '))
    if (input1 % 100 == 0) and (input1 % 400 == 0):
        print (f'El año {input1} es bisiesto')
        return True
    elif input1 % 4 == 0:
        if (input1 % 100 == 0):
            print (f'El año {input1} no es bisiesto')
            return False
        else:
            print(f'El año {input1} es bisiesto')
            return True
    else:
        print(f'El año {input1} no es bisiesto')
        return False
    

    

