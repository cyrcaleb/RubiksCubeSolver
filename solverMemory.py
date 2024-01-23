from ctypes import sizeof
import numpy as np

#   Cube Map: -> 
#   Centers piecies will always be in the same orientation
#             W W W
#             W w W
#             W W W

#   G G G     R R R     B B B     O O O
#   G g G     R r R     B b B     O o O
#   G G G     R R R     B B B     O O O

#             Y Y Y
#             Y y Y
#             Y Y Y

#   Moves: (Each face)
#       R, R', R2
#       L, L', L2
#       U, U', U2
#       D, D', D2
#       F, F', F2
#       B, B', B2
    

import json

def printCubeMap(cMap):
    print("-----------------------------------------------")
    # White Face
    whiteFace = "\t\t"
    for i in range(3):
        for j in range(3):
            whiteFace += colors[cMap[0][i][j]] + " "
        whiteFace += "\n\t\t"
    print(whiteFace)
    
    # Green, Red, Blue, and Orange Faces
    centerFaces = ""
    for i in range(3):
        for j in range(1,5):
            for k in range(3):
                centerFaces += colors[cMap[j][i][k]] + " "
            centerFaces += "\t\t"
        centerFaces += "\n"
    print(centerFaces)

    # Yellow Face
    yellowFace = "\t\t"
    for i in range(3):
        for j in range(3):
            yellowFace += colors[cMap[5][i][j]] + " "
        yellowFace += "\n\t\t"
    print(yellowFace)
    print("-----------------------------------------------")

def rotateSingle(matrix):
    n = len(matrix)
    #Reverse the matrix
    left = 0
    right = n - 1
    while left < right:
        matrix[left], matrix[right] = matrix[right], matrix[left]
        left += 1
        right -= 1
    #Transpose the previous matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    

def rotateF(cMap, times):
    # if times == 1:
    #     print("F")
    # elif times == 2:
    #     print("F2")
    # elif times == 3:
    #     print("F'")
    # else:
    #     print("Invalid time entered for F")

    for i in range(times):
        temp = cMap[0][2].copy()
        
        # White
        cMap[0][2][0] = cMap[1][2][2]
        cMap[0][2][1] = cMap[1][1][2]
        cMap[0][2][2] = cMap[1][0][2]

        # Green
        cMap[1][0][2] = cMap[5][0][0]
        cMap[1][1][2] = cMap[5][0][1]
        cMap[1][2][2] = cMap[5][0][2]

        # Yellow
        cMap[5][0][0] = cMap[3][2][0]
        cMap[5][0][1] = cMap[3][1][0]
        cMap[5][0][2] = cMap[3][0][0]

        # Blue
        cMap[3][0][0] = temp[0]
        cMap[3][1][0] = temp[1]
        cMap[3][2][0] = temp[2]

        # Red
        rotateSingle(cMap[2])

def rotateB(cMap, times):
    # if times == 1:
    #     print("B")
    # elif times == 2:
    #     print("B2")
    # elif times == 3:
    #     print("B'")
    # else:
    #     print("Invalid time entered for B")

    for i in range(times):
        temp = cMap[0][0].copy()
        
        # White
        cMap[0][0][0] = cMap[3][0][2]
        cMap[0][0][1] = cMap[3][1][2]
        cMap[0][0][2] = cMap[3][2][2]

        # Blue
        cMap[3][0][2] = cMap[5][2][2]
        cMap[3][1][2] = cMap[5][2][1]
        cMap[3][2][2] = cMap[5][2][0]

        # Yellow
        cMap[5][2][0] = cMap[1][0][0]
        cMap[5][2][1] = cMap[1][1][0]
        cMap[5][2][2] = cMap[1][2][0]

        # Green
        cMap[1][0][0] = temp[2]
        cMap[1][1][0] = temp[1]
        cMap[1][2][0] = temp[0]

        # Red
        rotateSingle(cMap[4])

def rotateR(cMap, times):
    # if times == 1:
    #     print("R")
    # elif times == 2:
    #     print("R2")
    # elif times == 3:
    #     print("R'")
    # else:
    #     print("Invalid time entered for R")

    for i in range(times):
        temp = [cMap[0][0][2], cMap[0][1][2], cMap[0][2][2]]
        
        # White
        cMap[0][0][2] = cMap[2][0][2]
        cMap[0][1][2] = cMap[2][1][2]
        cMap[0][2][2] = cMap[2][2][2]

        # Red
        cMap[2][0][2] = cMap[5][0][2]
        cMap[2][1][2] = cMap[5][1][2]
        cMap[2][2][2] = cMap[5][2][2]

        # Yellow
        cMap[5][0][2] = cMap[4][2][0]
        cMap[5][1][2] = cMap[4][1][0]
        cMap[5][2][2] = cMap[4][0][0]

        # Orange
        cMap[4][0][0] = temp[2]
        cMap[4][1][0] = temp[1]
        cMap[4][2][0] = temp[0]

        # Blue
        rotateSingle(cMap[3])

def rotateL(cMap, times):
    # if times == 1:
    #     print("L")
    # elif times == 2:
    #     print("L2")
    # elif times == 3:
    #     print("L'")
    # else:
    #     print("Invalid time entered for L")

    for i in range(times):
        temp = [cMap[0][0][0], cMap[0][1][0], cMap[0][2][0]]
        
        # White
        cMap[0][0][0] = cMap[4][2][2]
        cMap[0][1][0] = cMap[4][1][2]
        cMap[0][2][0] = cMap[4][0][2]

        # Orange
        cMap[4][2][2] = cMap[5][0][0]
        cMap[4][1][2] = cMap[5][1][0]
        cMap[4][0][2] = cMap[5][2][0]

        # Yellow
        cMap[5][0][0] = cMap[2][0][0]
        cMap[5][1][0] = cMap[2][1][0]
        cMap[5][2][0] = cMap[2][2][0]

        # Red
        cMap[2][0][0] = temp[0]
        cMap[2][1][0] = temp[1]
        cMap[2][2][0] = temp[2]


        # Green
        rotateSingle(cMap[1])


def rotateU(cMap, times):
    # if times == 1:
    #     print("U")
    # elif times == 2:
    #     print("U2")
    # elif times == 3:
    #     print("U'")
    # else:
    #     print("Invalid time entered for U")

    for i in range(times):
        temp = [cMap[4][0][0], cMap[4][0][1], cMap[4][0][2]]
        
        # Orange
        cMap[4][0][0] = cMap[1][0][0]
        cMap[4][0][1] = cMap[1][0][1]
        cMap[4][0][2] = cMap[1][0][2]
        
        # Green
        cMap[1][0][0] = cMap[2][0][0]
        cMap[1][0][1] = cMap[2][0][1]
        cMap[1][0][2] = cMap[2][0][2]

        # Red
        cMap[2][0][0] = cMap[3][0][0]
        cMap[2][0][1] = cMap[3][0][1]
        cMap[2][0][2] = cMap[3][0][2]

        # Green
        cMap[3][0][0] = temp[0]
        cMap[3][0][1] = temp[1]
        cMap[3][0][2] = temp[2]

        # White
        rotateSingle(cMap[0])

def rotateD(cMap, times):
    # if times == 1:
    #     print("D")
    # elif times == 2:
    #     print("D2")
    # elif times == 3:
    #     print("D'")
    # else:
    #     print("Invalid time entered for D")

    for i in range(times):
        temp = [cMap[2][2][0], cMap[2][2][1], cMap[2][2][2]]
        
        # Red
        cMap[2][2][0] = cMap[1][2][0]
        cMap[2][2][1] = cMap[1][2][1]
        cMap[2][2][2] = cMap[1][2][2]
        
        # Green
        cMap[1][2][0] = cMap[4][2][0]
        cMap[1][2][1] = cMap[4][2][1]
        cMap[1][2][2] = cMap[4][2][2]

        # Orange
        cMap[4][2][0] = cMap[3][2][0]
        cMap[4][2][1] = cMap[3][2][1]
        cMap[4][2][2] = cMap[3][2][2]

        # Blue
        cMap[3][2][0] = temp[0]
        cMap[3][2][1] = temp[1]
        cMap[3][2][2] = temp[2]

        # Yellow
        rotateSingle(cMap[5])


W = np.uint8(0)
G = np.uint8(1)
R = np.uint8(2)
B = np.uint8(3)
O = np.uint8(4)
Y = np.uint8(5)
   

solvedCube = [
    [
        [W, W, W],
        [W, W, W],
        [W, W, W]
    ],
    [
        [G, G, G],
        [G, G, G],
        [G, G, G]
    ],
    [
        [R, R, R],
        [R, R, R],
        [R, R, R]
    ],
    [
        [B, B, B],
        [B, B, B],
        [B, B, B]
    ],
    [
        [O, O, O],
        [O, O, O],
        [O, O, O]
    ],
    [
        [Y, Y, Y],
        [Y, Y, Y],
        [Y, Y, Y]
    ],
]

scrambledCube = [
    [
        [W, W, W],
        [W, W, W],
        [W, W, W]
    ],
    [
        [G, G, G],
        [G, G, G],
        [G, G, G]
    ],
    [
        [R, R, R],
        [R, R, R],
        [R, R, R]
    ],
    [
        [B, B, B],
        [B, B, B],
        [B, B, B]
    ],
    [
        [O, O, O],
        [O, O, O],
        [O, O, O]
    ],
    [
        [Y, Y, Y],
        [Y, Y, Y],
        [Y, Y, Y]
    ],
]

fSet = {"F", "F2", "F'"}
bSet = {"B", "B2", "B'"}
dSet = {"D", "D2", "D'"}
lSet = {"L", "L2", "L'"}
rSet = {"R", "R2", "R'"}
uSet = {"U", "U2", "U'"}

colors = ["W", "G", "R", "B", "O", "Y"]


def setScramble(cMap):
    print("Set scramble by doing the faces in the following order: White, Green, Red, Blue, Orange, Yellow")
    w,g,r,b,o,y = 9,9,9,9,9,9
    
    for k in range(6):
        print("\tRotate cube to correct side and enter values for this face  \n\t\tIf white, ensure the center color on top is orange, \n\t\tIf yellow ensure the center color on top is red, \n\t\tFor all other colors, ensure the center color on top is white")
        for i in range(3):
            j = 0
            while j < 3:
                print("\n\tEnter color (W,G,R,B,O,Y) for index: ", i, ", ", j)
                letter = input()
                if letter == "W":
                    w-=1
                elif letter == "G":
                    g-=1
                elif letter == "R":
                    r-=1
                elif letter == "B":
                    b-=1
                elif letter == "O":
                    o-=1
                elif letter == "Y":
                    y-=1
                else:
                    print("Invalid input given, try again\n")
                    continue

                cMap[k][i][j] = letter
                j+=1

    if (w or g or r or b or o or y):
        print("\nIMPOSSIBLE CASE GIVEN, Program Exited!")
        exit()
    
    print("Finding Solution")

def tupleize(cube):
    return tuple(tuple(tuple(row) for row in face) for face in cube)

def detupleize(cube_tuple):
    return [[[col for col in row] for row in face] for face in cube_tuple]


def applyMove(moveNum, cMap):
    temp = cMap.copy()

    if moveNum == 0:
        rotateF(temp,1)
    elif moveNum == 1:
        rotateF(temp,2)
    elif moveNum == 2:
        rotateF(temp,3)
    elif moveNum == 3:
        rotateB(temp,1)
    elif moveNum == 4:
        rotateB(temp,2)
    elif moveNum == 5:
        rotateB(temp,3)
    elif moveNum == 6:
        rotateD(temp,1)
    elif moveNum == 7:
        rotateD(temp,2)
    elif moveNum == 8:
        rotateD(temp,3)
    elif moveNum == 9:
        rotateL(temp,1)
    elif moveNum == 10:
        rotateL(temp,2)
    elif moveNum == 11:
        rotateL(temp,3)
    elif moveNum == 12:
        rotateR(temp,1)
    elif moveNum == 13:
        rotateR(temp,2)
    elif moveNum == 14:
        rotateR(temp,3)
    elif moveNum == 15:
        rotateU(temp,1)
    elif moveNum == 16:
        rotateU(temp,2)
    elif moveNum == 17:
        rotateU(temp,3)
    
    return temp

def getMoveName(moveNum, isSolvedSide):
    if isSolvedSide and (moveNum % 3) == 0:
        moveNum += 2
    elif isSolvedSide and (moveNum % 3) == 2:
        moveNum -= 2

    moves = ["F", "F2", "F'", "B", "B2", "B'", "D", "D2", "D'", "L", "L2", "L'", "R", "R2", "R'", "U", "U2", "U'"]

    return moves[moveNum]

def testAdd(moveList, nextMove):
    if len(moveList) == 0:
        return True
    
    if (moveList[-1] in fSet and nextMove in fSet) or (moveList[-1] in rSet and nextMove in rSet) or (moveList[-1] in lSet and nextMove in lSet) or (moveList[-1] in bSet and nextMove in bSet) or (moveList[-1] in uSet and nextMove in uSet) or (moveList[-1] in dSet and nextMove in dSet):
        return False
    
    return True


solvedStates = dict()
def solveScramble(scrambledCube):
    scrambledStates = dict()
    scrambledStates[tupleize(scrambledCube)] = []
    moveCount = 0
    while True:
        print("Scrambled States:", len(scrambledStates))
        # check if found first for memory purposes
        for scramble in list(scrambledStates.keys()):
            if str(scramble) in solvedStates:
                print(scrambledStates[scramble] + solvedStates[str(scramble)][::-1])
                return
        
        # if not found reduce solvedStates "significant time increase for significant memory decrease (exp)"
        # print(len(solvedStates))
        # for scramble in list(solvedStates.keys()):
        #     moveList = solvedStates[scramble]
        #     if len(moveList) == moveCount:
        #         del solvedStates[scramble]
        # print(len(solvedStates))
        # moveCount += 1

        
        for scramble in list(scrambledStates.keys()):
            for i in range(18):
                moveName = getMoveName(i, False)
                if not testAdd(scrambledStates[scramble], moveName):
                    continue
                nextScramble = applyMove(i, detupleize(scramble))
                if tupleize(nextScramble) not in scrambledStates:
                    scrambledStates[tupleize(nextScramble)] = scrambledStates[scramble] + [moveName]
            del scrambledStates[scramble]


def scrambleSolve():
    solvedStates[tupleize(solvedCube)] = []
    while True:
        print(len(solvedStates))
        if(len(solvedStates) > 8801060): 
            # Inside the scrambleSolve function before writing to the file
            with open('solvedStates2.json', 'w') as file:
                # Convert tuple keys to strings using a dictionary comprehension
                solved_states_str_keys = {str(key): value for key, value in solvedStates.items()}
                json.dump(solved_states_str_keys, file)
                return
        for scramble in list(solvedStates.keys()):
            for i in range(18):
                moveName = getMoveName(i, True)
                if not testAdd(solvedStates[scramble], moveName):
                    continue
                nextScramble = applyMove(i, detupleize(scramble))
                if tupleize(nextScramble) not in solvedStates:
                    solvedStates[tupleize(nextScramble)] = solvedStates[scramble] + [moveName]


def evalScramble(nextScramble):
    nextTotal = 0
    
    for k in range(6):
        for i in range(3):
            for j in range(3):
                if nextScramble[k][i][j] == solvedCube[k][i][j]:
                    nextTotal += 1
    
    print(nextTotal)




def loadJSON():
    global solvedStates
    # Open the JSON file for reading
    with open('solvedStates.json', 'r') as file:
        print("Started Loading json")
        # Load the content of the file into a dictionary variable
        solvedStates = json.load(file)
        print(len(solvedStates))
        print("Done Loading json")


#----------------------------------
        
# scrambleSolve()


# setScramble(scrambledCube)

loadJSON()

# rotateR(scrambledCube,2)
# rotateU(scrambledCube,3)
# rotateB(scrambledCube,2)
# rotateL(scrambledCube,1)
# rotateD(scrambledCube,3)
# rotateF(scrambledCube,2)
# rotateR(scrambledCube,3)
# rotateF(scrambledCube,3)
# rotateU(scrambledCube,1)
# rotateB(scrambledCube,2)
# rotateL(scrambledCube,3)
# rotateD(scrambledCube,1)

# superflip
evalScramble(scrambledCube)
rotateU(scrambledCube, 1); evalScramble(scrambledCube);
rotateR(scrambledCube, 2); evalScramble(scrambledCube);
rotateF(scrambledCube, 1); evalScramble(scrambledCube);
rotateB(scrambledCube, 1); evalScramble(scrambledCube);
rotateR(scrambledCube, 1); evalScramble(scrambledCube);
rotateB(scrambledCube, 2); evalScramble(scrambledCube);
rotateR(scrambledCube, 1); evalScramble(scrambledCube);
rotateU(scrambledCube, 2); evalScramble(scrambledCube);
rotateL(scrambledCube, 1); evalScramble(scrambledCube);
rotateB(scrambledCube, 2); evalScramble(scrambledCube);
rotateR(scrambledCube, 1); evalScramble(scrambledCube);
rotateU(scrambledCube, 3); evalScramble(scrambledCube);
rotateD(scrambledCube, 3); evalScramble(scrambledCube);
rotateR(scrambledCube, 2); evalScramble(scrambledCube);
rotateF(scrambledCube, 1); evalScramble(scrambledCube);
rotateR(scrambledCube, 3); evalScramble(scrambledCube);
rotateL(scrambledCube, 1); evalScramble(scrambledCube);
rotateB(scrambledCube, 2); evalScramble(scrambledCube);
rotateU(scrambledCube, 2); evalScramble(scrambledCube);
rotateF(scrambledCube, 2); evalScramble(scrambledCube);






printCubeMap(scrambledCube)

# old
# solveScramble(scrambledCube, solvedCube)

# new
solveScramble(scrambledCube)