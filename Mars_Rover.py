# MAKE A TEST CLASS FOR THIS CLASS!!!!!!!!!!

# The purpose of the class below was to be able to track the position of a mars rover, based on the direction and the co-ordinates given.
def Mars_Rover():
    # The purpose of this method was to take the letter, which would be either left or right, and the position, which 
    # is the current position of the rover, and the direction, which would be the N-W-S-E. I made 2 dictionaries for storing
    # all the directions and their impact on the co-ordinate values, for each of the 4 positions on the grid. Then I had an if/elif/else
    # statement to check whether left or right and then report the respective increment or decrement of the x or y.
    def calcCoordVal(letter,position,direction):
        Left = {'N':['x--','y--','x++','y++'],
                'W':['y--','x++','y++','x--'],
                'S':['x++','y++','x--','y--'],
                'E':['y++','x--','y--','x++'] }

        Right = {'N':['x++','y--','x--','y++'],
                 'W':['y++','x++','y--','x--'],
                 'S':['x--','y++','x++','y--'],
                 'E':['y--','x--','y++','x++'] }

        if letter is 'L':
            return (Left[direction][position-1])
        elif letter is 'R':
            return (Right[direction][position-1])
        else:
            return 'Invalid letter'
    
    # The purpose of the class below was to report the final position of the rover, having taken the co-ordinates, direction,
    # and the actual order of the left or right or move. There is a for loop which runs through each and every letter in the instructions
    # given, and for each letter, we first make sure if the position is the last position, then we need to reset the position, so it goes
    # to 1, but before the currentVar, which is just the increment or decrement of variable based on direction and position, is checked 
    # through the previous method. Then, if the position is less than 4, then position is incremented and the appropriate variable 
    # change is taken. Then, if the letter was moving, then we check the incrementing or decrementing and make the change accordingly, 
    # and if the input was invalid, then print the appropriate message. 
    def calculateFinalPos(x,y,direc,instruc):
        # keeps track of the current variable's incrementing or decrementing, which will be used in the Move elif to actually affect the 
        # value of the variable.
        currentVar = ''
        # The position is just the position of the rover as in the 4 directions and where its facing, and if 4 is reached, means we have 
        # gone a full circle, so we start back to 1, so we can get the correct input from the co-ordinate value method.
        position = 1

        for let in instruc:
            if let is not 'M':
                if (position == 4):
                    currentVar = calcCoordVal(let,position,direc)     
                    position == 1
                else:
                    currentVar = calcCoordVal(let,position,direc)     
                    position += 1
            elif let is 'M':
                if (currentVar == 'x--'):
                    x -= 1
                elif (currentVar == 'y--'):
                    y -= 1
                elif (currentVar == 'x++'):
                    x += 1
                elif (currentVar == 'y++'):
                    y += 1
                elif (currentVar == ''):
                    if(direc is 'N'):
                        y += 1
                    elif(direc is 'W'):
                        x -= 1
                    elif(direc is 'S'):
                        y -= 1
                    else:
                        x += 1
                else:
                    print("Something went Wrong in the input!")
            else:
                print("Incorrect letter! Cannot calculate!" +
                "Will print original co-ordinates")

        # returns the final position of the rover, with the co-ordinates and the direction
        coHead = '{} {} {}'.format(x,y,direc)
        return coHead


    # The purpose of the main method was really just to read the input file given line-by-line, and then redirect to the methods above,
    # to the actual work of the calculations.
    def main():
        # Input:

        # test case 1:
        # 1 2 N
        # LMLMLMLMM
        # test case 2:
        # 3 3 E
        # MMRMMRMRRM

        # Output:
        # 1 3 N
        # 5 1 E

        gotDirec = False
        gotInstruc = False
        counter = 0
        
        fileInput = open("rover_input.txt","r")

        # check made to make sure that the file is not empty
        if fileInput is '':
            raise FileNotFoundError

        allLines = fileInput.readlines()
        
        fileInput.close()

        # iterate over each line in the input file, but discard the first line, so the counter
        # is 0 initially, and gets incremented at the end of the loop, since the first line does
        # not have x,y or direc, but just the number of test cases.
        for line in allLines:
            if(counter == 0):
                line.strip()
            else:
                # checks that if the number is odd, then that line will represent the x,y,direc
                # line and that line is split into an array, codi, representing co-ordinate and 
                # direction. 
                if(counter % 2 != 0):
                    answer = line.strip()
                    codi = answer.split()
                    x,y = int(codi[0]),int(codi[1])
                    direc = codi[2]
                    gotDirec = True
                else:
                    instruc = line.strip()
                    gotInstruc = True
            # if we have found the co-ord, direction and the word, then we have found 1 full case,
            # so we print the score found from the placeOnBoard method, which will be given the 
            # respective values. 
            if(gotDirec == True and gotInstruc == True):
                print(calculateFinalPos(x,y,direc,instruc))
                gotDirec = False
                gotInstruc = False
            counter += 1

    main()

Mars_Rover()