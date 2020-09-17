def one_1(x)
    can_travel= print('You can travel (N)orth.')
    direction = input('Direction: ')
    while direction!='n':
        can_travel= print('You can travel (N)orth.')
        direction = input('Direction: ')
    else: 
        return one_2(direction)


def one_2(x):
    print('You can travel: (N)orth or (E)ast or (S)outh.')
    direction=input('Direction: ')
    if direction=='n':
        return one_3(direction)
    elif direction=='e':
        return two_2(direction)
    elif direction=='s':
        return one_1(direction)


def one_3(x):
    print('You can travel: (E)ast or (S)outh.')
    direction=input('Direction: ')
    if direction=='e':
        return two_3(direction)
    elif direction=='s':
        return one_two(direction)

def two_1(x)
    print('You can travel: (N)orth.')
    direction=input('Direction: ')
    
    else :
        return one_2(direction)
    

def two_2(x)
    print('You can travel: (S)outh or (W)est.')
    direction=input('Direction: ')
    if direction=='s'
        return two_1


while direction!=input_travel:
    print('Not a valid direction!')
    
    input_travel= input('You can travel (N)orth.')
    direction = input('Direction: ')
else: 
    one_1(direction)
