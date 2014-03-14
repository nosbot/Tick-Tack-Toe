import random

def getBoo():
        while True:
            cin = raw_input('(Y or N):\n').lower()
            if cin.startswith('y'):
                return True
                break
            if cin.startswith('n'):
                return False
                break

while True:
    box = [0,1,2,3,4,5,6,7,8,9]
    usedbox = []
    remaining = [1,2,3,4,5,6,7,8,9]
    amountofPlayers = 0
    win = False

    def grid():
        grid = (''' ''' + str(box[1]) + ''' | ''' + str(box[2]) + ''' | ''' + str(box[3]) + '''
===========
 ''' + str(box[4]) + ''' | ''' + str(box[5]) + ''' | ''' + str(box[6]) + '''
===========
 ''' + str(box[7]) + ''' | ''' + str(box[8]) + ''' | ''' + str(box[9]))
        print grid

    print ("LETS PLAY TIC-TAC-TOE!")
    while True:
        print ("1 Player or 2 Players?")
        try:
            singormult = int(raw_input('(1 or 2)\n'))
            if singormult == 1:
                amountofPlayers = 1
                break
            if singormult == 2:
                amountofPlayers = 2
                break
        except ValueError:
            print("That's not a number!")
    while True:
        xoxo=raw_input("X or O?\n").upper()
        p1 = xoxo
        if p1 == 'X':
            p2 = 'O'
            cpu = 'O'
            break
        if p1 == 'O':
            p2 = 'X'
            cpu = 'X'
            break
    if amountofPlayers == 2:
        while True:
            while True:
                grid()
                try:
                     p1turn = int(raw_input("P1 turn:\n"))
                     if p1turn in remaining:
                        box[p1turn] = p1
                        remaining.remove(p1turn)
                        break
                except ValueError:
                    print("That's not a number!")
                else:
                    print('Taken!')
            if (box[1] == box[2] == box[3] == p1
                or box[1] == box[4] == box[7] == p1
                or box[1] == box[5] == box[9] == p1
                or box[2] == box[5] == box[8] == p1
                or box[3] == box[5] == box[7] == p1
                or box[3] == box[6] == box[9] == p1
                or box[4] == box[5] == box[6] == p1
                or box[7] == box[8] == box[9] == p1):
                grid()
                print 'P1 Wins'
                break
            if len(remaining) < 1:
                if win == False:
                     grid()
                     print('Its a Tie!')
                     break 
            while True:
                grid()
                try:
                     p2turn = int(raw_input("P2 turn:\n"))
                     if p2turn in remaining:
                        box[p2turn] = p2
                        remaining.remove(p2turn)
                        break
                except ValueError:
                    print("That's not a number!")
                else:
                    print('Taken!')
            if (box[1] == box[2] == box[3] == p2
                or box[1] == box[4] == box[7] == p2
                or box[1] == box[5] == box[9] == p2
                or box[2] == box[5] == box[8] == p2
                or box[3] == box[5] == box[7] == p2
                or box[3] == box[6] == box[9] == p2
                or box[4] == box[5] == box[6] == p2
                or box[7] == box[8] == box[9] == p2):
                grid()
                print 'P2 Wins'
                break
            if len(remaining) < 1:
                if win == False:
                     grid()
                     print('Its a Tie!')
                     break 
    if amountofPlayers == 1:
        while True:
            if xoxo == 'O':
                box[1] = 'X'
                remaining.remove(1)
            win = False
            firstmove = True
            while True:
                while True:
                    grid()
                    try:
                        p1turn = int(raw_input("Your turn:\n"))
                        if p1turn in remaining:
                            box[p1turn] = p1
                            remaining.remove(p1turn)
                            break
                    except ValueError:
                        print "That's not a number.\n"
                    else:
                        print('Taken!\n')
                if (box[1] == box[2] == box[3] == p1
                    or box[1] == box[4] == box[7] == p1
                    or box[1] == box[5] == box[9] == p1
                    or box[2] == box[5] == box[8] == p1
                    or box[3] == box[5] == box[7] == p1
                    or box[3] == box[6] == box[9] == p1
                    or box[4] == box[5] == box[6] == p1
                    or box[7] == box[8] == box[9] == p1):
                    grid()
                    print 'P1 Wins'
                    win = True
                    break
                if len(remaining) < 1:
                    if win == False:
                        grid()
                        print('Its a Tie!')
                        break 
                cup = random.choice(remaining)
                if box[5] == p1:
                    if firstmove == True:
                        cup = random.choice([1,3,7,9])
                        firstmove = False
                cpumove = cup
                if (box[2] == box[3] or
                    box[4] == box[7] or
                    box[5] == box[9]):
                    if type(box[1]) == int:
                        cpumove = 1
                if (box[1] == box[3] or
                    box[5] == box[8]):
                    if type(box[2]) == int:
                        cpumove = 2
                if (box[1] == box[2] or
                    box[5] == box[7] or
                    box[6] == box[9]):
                    if type(box[3]) == int:
                        cpumove = 3
                if (box[1] == box[7] or
                    box[5] == box[6]):
                    if type(box[4]) == int:
                        cpumove = 4
                if (box[1] == box[9] or
                    box[2] == box[8] or
                    box[3] == box[7] or
                    box[4] == box[6]):
                    if type(box[5]) == int:
                        cpumove = 5
                if (box[3] == box[9] or
                    box[4] == box[5]):
                    if type(box[6]) == int:
                        cpumove = 6
                if (box[1] == box[4] or
                    box[3] == box[5] or
                    box[8] == box[9]):
                    if type(box[7]) == int:
                        cpumove = 7
                if (box[2] == box[5] or
                    box[7] == box[9]):
                    if type(box[8]) == int:
                        cpumove = 8
                if (box[1] == box[5] or
                    box[3] == box[6] or
                    box[7] == box[8]):
                    if type(box[9]) == int:
                        cpumove = 9
                if (box[2] == box[3] == cpu or
                    box[4] == box[7] == cpu or
                    box[5] == box[9] == cpu):
                    if type(box[1]) == int:
                        cpumove = 1
                if (box[1] == box[3] == cpu or
                    box[5] == box[8] == cpu):
                    if type(box[2]) == int:
                        cpumove = 2
                if (box[1] == box[2] == cpu or
                    box[5] == box[7] == cpu or
                    box[6] == box[9] == cpu):
                    if type(box[3]) == int:
                        cpumove = 3
                if (box[1] == box[7] == cpu or
                    box[5] == box[6] == cpu):
                    if type(box[4]) == int:
                        cpumove = 4
                if (box[1] == box[9] == cpu or
                    box[2] == box[8] == cpu or
                    box[3] == box[7] == cpu or
                    box[4] == box[6] == cpu):
                    if type(box[5]) == int:
                        cpumove = 5
                if (box[3] == box[9] == cpu or
                    box[4] == box[5] == cpu):
                    if type(box[6]) == int:
                        cpumove = 6
                if (box[1] == box[4] == cpu or
                    box[3] == box[5] == cpu or
                    box[8] == box[9] == cpu):
                    if type(box[7]) == int:
                        cpumove = 7
                if (box[2] == box[5] == cpu or
                    box[7] == box[9] == cpu):
                    if type(box[8]) == int:
                        cpumove = 8
                if (box[1] == box[5] == cpu or
                    box[3] == box[6] == cpu or
                    box[7] == box[8] == cpu):
                    if type(box[9]) == int:
                        cpumove = 9
                if len(remaining) == 1:
                    cpumove = remaining[0]
                if type(box[5]) == int:
                    if firstmove == True:
                        cpumove = 5
                        firstmove = False
                if (box[1] == box[9] == p1 or
                box[3] == box[7] == p1):
                    if firstmove == True:
                        cup = random.choice([2,4,6,8])
                        cpumove = cup
                        firstmove = False
                if box[1] == cpu:
                    if type(box[9]) == int:
                        cpumove = 9
                box[cpumove] = cpu
                print cpumove
                remaining.remove(cpumove)
                if (box[1] == box[2] == box[3] == cpu
                    or box[1] == box[4] == box[7] == cpu
                    or box[1] == box[5] == box[9] == cpu
                    or box[2] == box[5] == box[8] == cpu
                    or box[3] == box[5] == box[7] == cpu
                    or box[3] == box[6] == box[9] == cpu
                    or box[4] == box[5] == box[6] == cpu
                    or box[7] == box[8] == box[9] == cpu):
                    grid()
                    print 'CPU Wins'
                    win = True
                    break
                if len(remaining) < 1:
                    if win == False:
                        grid()
                        print('Its a Tie!')
                        break
            break
    print("Play again?")
    if getBoo() == False:
        break
