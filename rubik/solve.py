import copy
import rubik.cube as rubik
import rubik.check as check

def _solve(parms):
    result = check._check(parms) #using _.check to validate cube
    if(result['status'] != 'ok'):
        return result
    
    cubeString = parms.get('cube',None)
    cubeModel = rubik.Cube()
    cubeModel.convertString(cubeString)
    if('rotate' in parms and len(parms.get('rotate', None)) > 0):
        rotations = parms.get('rotate', None)   
        
        for rotation in rotations:
            if(rotation not in ['F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd']):
                result['status'] = 'error: invalid rotation'
                return result
            elif(rotation == 'F'):
                F(cubeModel)
            elif(rotation == 'f'):
                f(cubeModel)
            elif(rotation == 'R'):
                R(cubeModel)
            elif(rotation == 'r'):
                r(cubeModel)
            elif(rotation == 'B'):
                B(cubeModel)
            elif(rotation == 'b'):
                b(cubeModel)
            elif(rotation == 'L'):
                L(cubeModel)
            elif(rotation == 'l'):
                l(cubeModel)
            elif(rotation == 'U'):
                U(cubeModel)
            elif(rotation == 'u'):
                u(cubeModel)
            elif(rotation == 'D'):
                D(cubeModel)
            elif(rotation == 'd'):
                d(cubeModel)
        cubeDict = dict()
        cubeDict['cube'] = cubeModel.convertCube() #converting back into string representation
        cubeDict.update(result)
        result = cubeDict
    else:
        #making solution the first key in the dictionary
        solution = solveDownCross(cubeModel)
        solution += solveDownCorners(cubeModel)
        solutionDict = dict()
        solutionDict['solution'] = solution
        solutionDict.update(result)
        result = solutionDict
    return result

def F(cubeModel):
    cubeModel.faceClockwise(0) #rotating front face
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.right[0][0], cubeModel.right[1][0], cubeModel.right[2][0] = copyModel.up[2][0], copyModel.up[2][1], copyModel.up[2][2]
    cubeModel.left[0][2], cubeModel.left[1][2], cubeModel.left[2][2] = copyModel.down[0][0], copyModel.down[0][1], copyModel.down[0][2]
    cubeModel.up[2][0], cubeModel.up[2][1], cubeModel.up[2][2]  = copyModel.left[2][2], copyModel.left[1][2], copyModel.left[0][2]
    cubeModel.down[0][0], cubeModel.down[0][1], cubeModel.down[0][2] = copyModel.right[2][0], copyModel.right[1][0], copyModel.right[0][0]

def f(cubeModel):
    cubeModel.faceCounterclockwise(0) #rotating front face
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.right[0][0], cubeModel.right[1][0], cubeModel.right[2][0] = copyModel.down[0][2], copyModel.down[0][1], copyModel.down[0][0]
    cubeModel.left[0][2], cubeModel.left[1][2], cubeModel.left[2][2] = copyModel.up[2][2], copyModel.up[2][1], copyModel.up[2][0]
    cubeModel.up[2][0], cubeModel.up[2][1], cubeModel.up[2][2]  = copyModel.right[0][0], copyModel.right[1][0], copyModel.right[2][0]
    cubeModel.down[0][0], cubeModel.down[0][1], cubeModel.down[0][2] = copyModel.left[0][2], copyModel.left[1][2], copyModel.left[2][2]

def R(cubeModel):  
    cubeModel.faceClockwise(1)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.front[0][2], cubeModel.front[1][2], cubeModel.front[2][2] = copyModel.down[0][2], copyModel.down[1][2], copyModel.down[2][2]
    cubeModel.back[0][0], cubeModel.back[1][0], cubeModel.back[2][0] = copyModel.up[2][2], copyModel.up[1][2], copyModel.up[0][2]
    cubeModel.up[0][2], cubeModel.up[1][2], cubeModel.up[2][2] = copyModel.front[0][2], copyModel.front[1][2], copyModel.front[2][2]
    cubeModel.down[0][2], cubeModel.down[1][2], cubeModel.down[2][2] = copyModel.back[2][0], copyModel.back[1][0], copyModel.back[0][0]

def r(cubeModel):  
    cubeModel.faceCounterclockwise(1)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.front[0][2], cubeModel.front[1][2], cubeModel.front[2][2] = copyModel.up[0][2], copyModel.up[1][2], copyModel.up[2][2]
    cubeModel.back[0][0], cubeModel.back[1][0], cubeModel.back[2][0] = copyModel.down[2][2], copyModel.down[1][2], copyModel.down[0][2]
    cubeModel.up[0][2], cubeModel.up[1][2], cubeModel.up[2][2] = copyModel.back[2][0], copyModel.back[1][0], copyModel.back[0][0]
    cubeModel.down[0][2], cubeModel.down[1][2], cubeModel.down[2][2] = copyModel.front[0][2], copyModel.front[1][2], copyModel.front[2][2]
  
def B(cubeModel):
    cubeModel.faceClockwise(2)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.right[0][2], cubeModel.right[1][2], cubeModel.right[2][2] = copyModel.down[2][2], copyModel.down[2][1], copyModel.down[2][0]
    cubeModel.left[0][0], cubeModel.left[1][0], cubeModel.left[2][0] = copyModel.up[0][2], copyModel.up[0][1], copyModel.up[0][0]
    cubeModel.up[0][0], cubeModel.up[0][1], cubeModel.up[0][2] = copyModel.right[0][2], copyModel.right[1][2], copyModel.right[2][2]
    cubeModel.down[2][0], cubeModel.down[2][1], cubeModel.down[2][2] = copyModel.left[0][0], copyModel.left[1][0], copyModel.left[2][0]
   
def b(cubeModel):
    cubeModel.faceCounterclockwise(2)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.right[0][2], cubeModel.right[1][2], cubeModel.right[2][2] = copyModel.up[0][0], copyModel.up[0][1], copyModel.up[0][2]
    cubeModel.left[0][0], cubeModel.left[1][0], cubeModel.left[2][0] = copyModel.down[2][0], copyModel.down[2][1], copyModel.down[2][2]
    cubeModel.up[0][0], cubeModel.up[0][1], cubeModel.up[0][2] = copyModel.left[2][0], copyModel.left[1][0], copyModel.left[0][0]
    cubeModel.down[2][0], cubeModel.down[2][1], cubeModel.down[2][2] = copyModel.right[2][2], copyModel.right[1][2], copyModel.right[0][2]

def L(cubeModel):
    cubeModel.faceClockwise(3)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.front[0][0], cubeModel.front[1][0], cubeModel.front[2][0] = copyModel.up[0][0], copyModel.up[1][0], copyModel.up[2][0] 
    cubeModel.back[0][2], cubeModel.back[1][2], cubeModel.back[2][2] = copyModel.down[2][0], copyModel.down[1][0], copyModel.down[0][0]   
    cubeModel.up[0][0], cubeModel.up[1][0], cubeModel.up[2][0] = copyModel.back[2][2], copyModel.back[1][2], copyModel.back[0][2]
    cubeModel.down[0][0], cubeModel.down[1][0], cubeModel.down[2][0] = copyModel.front[0][0], copyModel.front[1][0], copyModel.front[2][0]
    
def l(cubeModel):
    cubeModel.faceCounterclockwise(3)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.front[0][0], cubeModel.front[1][0], cubeModel.front[2][0] = copyModel.down[0][0], copyModel.down[1][0], copyModel.down[2][0]
    cubeModel.back[0][2], cubeModel.back[1][2], cubeModel.back[2][2] = copyModel.up[2][0], copyModel.up[1][0], copyModel.up[0][0]
    cubeModel.up[0][0], cubeModel.up[1][0], cubeModel.up[2][0] = copyModel.front[0][0], copyModel.front[1][0], copyModel.front[2][0]
    cubeModel.down[0][0], cubeModel.down[1][0], cubeModel.down[2][0] = copyModel.back[2][2], copyModel.back[1][2], copyModel.back[0][2]
    
def U(cubeModel):
    cubeModel.faceClockwise(4)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.front[0] = copyModel.right[0]
    cubeModel.right[0] = copyModel.back[0]
    cubeModel.back[0] = copyModel.left[0]
    cubeModel.left[0] = copyModel.front[0]
            
def u(cubeModel):
    cubeModel.faceCounterclockwise(4)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.front[0] = copyModel.left[0]
    cubeModel.right[0] = copyModel.front[0]
    cubeModel.back[0] = copyModel.right[0]
    cubeModel.left[0] = copyModel.back[0]
    
def D(cubeModel):
    cubeModel.faceClockwise(5)
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.front[2] = copyModel.left[2]
    cubeModel.right[2] = copyModel.front[2]
    cubeModel.back[2] = copyModel.right[2]
    cubeModel.left[2] = copyModel.back[2] 
    
def d(cubeModel):
    cubeModel.faceCounterclockwise(5)  
    copyModel = copy.deepcopy(cubeModel)
    cubeModel.front[2] = copyModel.right[2]
    cubeModel.right[2] = copyModel.back[2]
    cubeModel.back[2] = copyModel.left[2]
    cubeModel.left[2] = copyModel.front[2]
    
def doubleRotate(cubeModel, rotation):
    if(rotation == 'F'):
        F(cubeModel)
        F(cubeModel)
    elif(rotation == 'R'):
        R(cubeModel)
        R(cubeModel)
    elif(rotation == 'B'):
        B(cubeModel)
        B(cubeModel)
    elif(rotation == 'L'):
        L(cubeModel)
        L(cubeModel)
    elif(rotation == 'U'):
        U(cubeModel)
        U(cubeModel)
    elif(rotation == 'D'):
        D(cubeModel)
        D(cubeModel)
    
def solveDownCross(cubeModel):
    solution = ''
    if(checkDownCross(cubeModel) == True):
        return solution
    
    downColor = cubeModel.down[1][1]
    frontColor = cubeModel.front[1][1]
    rightColor = cubeModel.right[1][1]
    backColor = cubeModel.back[1][1]
    leftColor = cubeModel.left[1][1]
    
    #clockwise side = right when looking at face straight on (i.e oriented to the front)
    #counter side = left when looking at face sraight on
    #'flipped' cases are cases where the front color is first in the conditional
    
    #solve front edge
    solution += locateBottomEdge(cubeModel, downColor, frontColor)
    
    #solve right edge
    U(cubeModel)
    solution += 'U' + locateBottomEdge(cubeModel, downColor, rightColor) + 'u'
    u(cubeModel)
    
    #solve back edge
    doubleRotate(cubeModel, 'U')
    solution += 'UU' + locateBottomEdge(cubeModel, downColor, backColor) + 'UU'
    doubleRotate(cubeModel, 'U')
    
    #solve left edge
    u(cubeModel)
    solution += 'u' + locateBottomEdge(cubeModel, downColor, leftColor) + 'U'
    U(cubeModel)
    
    
    #rotating edges from daisy position to solved position   
    doubleRotate(cubeModel, 'F')
    doubleRotate(cubeModel, 'R')
    doubleRotate(cubeModel, 'B') 
    doubleRotate(cubeModel, 'L')
    solution += 'FFRRBBLL'
    return solution 
    
#Locates and puts a bottom edge in daisy position
def locateBottomEdge(cubeModel, downColor, frontColor):
    solution = ''
    #check if front edge is in down of front (true solved position)
    if(cubeModel.down[0][1] == downColor and cubeModel.front[2][1] == frontColor):
        doubleRotate(cubeModel, 'F')
        solution += 'FF'
    #check if front edge is flipped in down of front (true solved position)
    elif(cubeModel.down[0][1] == frontColor and  cubeModel.front[2][1] == downColor):
        f(cubeModel)
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        solution += 'fuRU'
    #check if front edge is in down of right
    elif(cubeModel.down[1][2] == downColor and cubeModel.right[2][1] == frontColor):
        u(cubeModel)
        doubleRotate(cubeModel, 'R')
        U(cubeModel)
        solution += 'uRRU'
    #check if front edge is flipped in down of right
    elif(cubeModel.down[1][2] == frontColor and cubeModel.right[2][1] == downColor):
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        f(cubeModel)
        solution += 'uRUf'
    #check if front edge is in down of back
    elif(cubeModel.down[2][1] == downColor and cubeModel.back[2][1] == frontColor):
        doubleRotate(cubeModel, 'D')
        doubleRotate(cubeModel, 'F')
        solution += 'DDFF'
    #check if front edge is flipped in down of back
    elif(cubeModel.down[2][1] == frontColor and cubeModel.back[2][1] == downColor):
        d(cubeModel)
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        f(cubeModel)
        solution += 'duRUf'
    #check if front edge is in down of left
    elif(cubeModel.down[1][0] == downColor and cubeModel.left[2][1] == frontColor):
        D(cubeModel)
        doubleRotate(cubeModel, 'F')
        solution += 'DFF'
    #check if front edge is flipped in down of left
    elif(cubeModel.down[1][0] == frontColor and cubeModel.left[2][1] == downColor):
        D(cubeModel)
        f(cubeModel)
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        solution += 'DfuRU'
    
    #check if front edge is in clockwise of front/counter of right
    elif(cubeModel.front[1][2] == downColor and cubeModel.right[1][0] == frontColor):
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        solution += 'uRU'
    #check if front edge is flipped in clockwise of front/counter of right 
    elif(cubeModel.front[1][2] == frontColor and cubeModel.right[1][0] == downColor):
        f(cubeModel)
        solution += 'f'  
    #check if front edge is in clockwise of right/counter of back
    elif(cubeModel.right[1][2] == downColor and cubeModel.back[1][0] == frontColor):
        u(cubeModel)
        r(cubeModel)
        U(cubeModel)
        F(cubeModel)
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        solution += 'urUFuRU'
    #check if front edge is flipped in clockwise of right/counter of back
    elif(cubeModel.right[1][2] == frontColor and cubeModel.back[1][0] == downColor):    
        u(cubeModel)
        r(cubeModel)
        U(cubeModel)
        solution += 'urU'
    #check if front edge is in clockwise of back/ counter of left
    elif(cubeModel.back[1][2] == downColor and cubeModel.left[1][0] == frontColor):
        U(cubeModel)
        L(cubeModel)
        u(cubeModel)
        solution += 'ULu'
    #check if front edge is flipped in clockwise of back/ counter of left
    elif(cubeModel.back[1][2] == frontColor and cubeModel.left[1][0] == downColor):
        U(cubeModel)
        doubleRotate(cubeModel, 'L')
        u(cubeModel)
        F(cubeModel)
        solution += 'ULLuF'
    #check if front edge is in counter of front/clockwise of left 
    elif(cubeModel.left[1][2] == downColor and cubeModel.front[1][0] == frontColor):
        F(cubeModel)
        solution += 'F'
    #check if front edge is flipped in counter of front/clockwise of left
    elif(cubeModel.left[1][2] == frontColor and cubeModel.front[1][0] == downColor):
        U(cubeModel)
        l(cubeModel)
        u(cubeModel)
        solution += 'Ulu'

    #These up conditions are designed with the assumption that the two remaining top pieces might be solved, and thus avoid removing them
    #check if front edge is in up of front (daisy solved position)
    elif(cubeModel.up[2][1] == downColor and cubeModel.front[0][1] == frontColor):
        pass
    #check if front edge is flipped in up of front (daisy position)
    elif(cubeModel.up[2][1] == frontColor and cubeModel.front[0][1] == downColor):
        F(cubeModel)
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        solution += 'FuRU'
    #check if front edge is in up of right
    elif(cubeModel.up[1][2] == downColor and cubeModel.right[0][1] == frontColor):
        doubleRotate(cubeModel, 'F')
        doubleRotate(cubeModel, 'R')
        d(cubeModel)
        doubleRotate(cubeModel, 'F')
        solution += 'FFRRdFF'
    #check if front edge is flipped in up of right
    elif(cubeModel.up[1][2] == frontColor and cubeModel.right[0][1] == downColor):
        doubleRotate(cubeModel, 'F')
        r(cubeModel)
        f(cubeModel)
        solution += 'FFrf'
    #check if front edge is in up of back
    elif(cubeModel.up[0][1] == downColor and cubeModel.back[0][1] == frontColor):
        doubleRotate(cubeModel, 'F')
        doubleRotate(cubeModel, 'B')
        doubleRotate(cubeModel, 'D')
        doubleRotate(cubeModel, 'F')
        solution += 'FFBBDDFF' 
    #check if front edge is flipped in up of back
    elif(cubeModel.up[0][1] == frontColor and cubeModel.back[0][1] == downColor):
        doubleRotate(cubeModel, 'F')
        doubleRotate(cubeModel, 'B')
        doubleRotate(cubeModel, 'D')
        f(cubeModel)
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        solution += 'FFBBDDfuRU'
    #check if front edge is in up of left 
    elif(cubeModel.up[1][0] == downColor and cubeModel.left[0][1] == frontColor):
        doubleRotate(cubeModel, 'F')
        doubleRotate(cubeModel, 'L')
        D(cubeModel)
        doubleRotate(cubeModel, 'F')
        solution += 'FFLLDFF'
    #check if front edge is flipped in up of left 
    elif(cubeModel.up[1][0] == frontColor and cubeModel.left[0][1] == downColor):
        doubleRotate(cubeModel, 'F')
        doubleRotate(cubeModel, 'L')
        D(cubeModel)
        f(cubeModel)
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        solution += 'FFLLDfuRU'
        
    return solution 

def solveDownCorners(cubeModel):
    solution = ''
    if(checkFirstLayer(cubeModel) == True):
        return solution
    
    downColor = cubeModel.down[1][1]
    frontColor = cubeModel.front[1][1]
    rightColor = cubeModel.right[1][1]
    backColor = cubeModel.back[1][1]
    leftColor = cubeModel.left[1][1]
    
    #Solve front/right corner
    solution += locateCorner(cubeModel, downColor, frontColor, rightColor)
    
    #solve right/back corner 
    d(cubeModel)
    solution += 'd' + locateCorner(cubeModel, downColor, rightColor, backColor) + 'D'
    D(cubeModel) 
    
    #solve back/left corner
    doubleRotate(cubeModel, 'D')
    solution += 'DD' + locateCorner(cubeModel, downColor, backColor, leftColor) + 'DD'
    doubleRotate(cubeModel, 'D')

    #solve left/front corner
    D(cubeModel)
    solution += 'D' + locateCorner(cubeModel, downColor, leftColor, frontColor) + 'd'
    d(cubeModel)
    
    return solution

#Checks if corner is the correct corner
def checkCorner(corner, colorOne, colorTwo, colorThree):
    for square in corner:
        if(square != colorOne and square != colorTwo and square != colorThree):
            return False
        else:
            pass
    return True

def leftTrigger(cubeModel):
    l(cubeModel)
    u(cubeModel)
    L(cubeModel)
    U(cubeModel)
    return 'luLU'
        
def rightTrigger(cubeModel):
    R(cubeModel)
    U(cubeModel)
    r(cubeModel)
    u(cubeModel)
    return 'RUru'
#These trigger functions are the equivalent of perorming a left or right trigger on a face other than the front face
#The first word in the function name indicates which face is being treated is 'front' and the second is which face is being rotated
def rightFrontTrigger(cubeModel):
    f(cubeModel)
    u(cubeModel)
    F(cubeModel)
    U(cubeModel)
    return 'fuFU'

def rightBackTrigger(cubeModel):
    B(cubeModel)
    U(cubeModel)
    b(cubeModel)
    u(cubeModel)
    return 'BUbu'

def backRightTrigger(cubeModel):
    r(cubeModel)
    u(cubeModel)
    R(cubeModel)
    U(cubeModel)
    return 'ruRU'

def backLeftTrigger(cubeModel):
    L(cubeModel)
    U(cubeModel)
    l(cubeModel)
    u(cubeModel)
    return 'LUlu'

def leftBackTrigger(cubeModel):
    b(cubeModel)
    u(cubeModel)
    B(cubeModel)
    U(cubeModel)
    return 'buBU'

#Performs right triggers until corner is solved
def solveDownCorner(cubeModel, downColor, frontColor, rightColor):
    solution = ''
    while(cubeModel.down[0][2] != downColor or cubeModel.front[2][2] != frontColor or cubeModel.right[2][0] != rightColor):
        solution += rightTrigger(cubeModel)
    return solution

#Finds which position given corner is and solves it based on position
#Colors are relative (i.e. frontColor refers to whichever color is front at current time, not original front)
def locateCorner(cubeModel, downColor, frontColor, rightColor):
    solution = ''
    #Corner in front/right up position
    if(checkCorner((cubeModel.up[2][2], cubeModel.front[0][2], cubeModel.right[0][0]), downColor, frontColor, rightColor)):
        solution += solveDownCorner(cubeModel, downColor, frontColor, rightColor)        
    #Corner in right/back up position
    if(checkCorner((cubeModel.up[0][2], cubeModel.right[0][2], cubeModel.back[0][0]), downColor, frontColor, rightColor)):
        U(cubeModel)
        solution += 'U' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #Corner in back/left up position
    if(checkCorner((cubeModel.up[0][0], cubeModel.back[0][2], cubeModel.left[0][0]), downColor, frontColor, rightColor)):
        doubleRotate(cubeModel, 'U')
        solution += 'UU' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #Corner in left/front up position
    if(checkCorner((cubeModel.up[2][0], cubeModel.left[0][2], cubeModel.front[0][0]), downColor, frontColor, rightColor)):
        u(cubeModel)
        solution += 'u' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #Corner in front/right down position (solved position)
    if(checkCorner((cubeModel.down[0][2], cubeModel.front[2][2], cubeModel.right[2][0]), downColor, frontColor, rightColor)):
        solution += solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #Corner in right/back down position
    if(checkCorner((cubeModel.down[2][2], cubeModel.right[2][2], cubeModel.back[2][0]), downColor, frontColor, rightColor)):
        r(cubeModel)
        doubleRotate(cubeModel, 'U')
        R(cubeModel)
        u(cubeModel)
        solution += 'rUURu' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #Corner in back/left down position
    if(checkCorner((cubeModel.down[2][0], cubeModel.back[2][2], cubeModel.left[2][0]), downColor, frontColor, rightColor)):
        L(cubeModel)
        doubleRotate(cubeModel, 'U')
        l(cubeModel)
        solution += 'LUUl' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #corner in left/front down position
    if(checkCorner((cubeModel.down[0][0], cubeModel.left[2][2], cubeModel.front[2][0]), downColor, frontColor, rightColor)):
        solution += leftTrigger(cubeModel)
        u(cubeModel)
        solution += 'u' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    
    return solution
  
def checkDownCross(cubeModel):  
    color = cubeModel.down[1][1] # down center color
    #checking down face cross squares
    if(cubeModel.down[0][1] == color and cubeModel.down[1][0] == color and cubeModel.down[1][2] == color and cubeModel.down[2][1]):
        #checking edge squares on adjacent faces
        if(cubeModel.front[2][1] != cubeModel.front[1][1]):
            return False
        elif(cubeModel.right[2][1] != cubeModel.right[1][1]):
            return False
        elif(cubeModel.back[2][1] != cubeModel.back[1][1]):
            return False
        elif(cubeModel.left[2][1] != cubeModel.left[1][1]):
            return False
        else:
            return True
    else:
        return False
    
def checkFirstLayer(cubeModel):
    if(checkDownCross(cubeModel) == False):
        return False
    else:
        color = cubeModel.down[1][1]
        #checking down corners
        if(cubeModel.down[0][0] == color and cubeModel.down[0][2] == color and cubeModel.down[2][0] == color and cubeModel.down[2][2] == color):
            color = cubeModel.front[1][1]
            if(cubeModel.front[2][0] != color and cubeModel.front[2][2] != color):
                return False
            color = cubeModel.right[1][1]
            if(cubeModel.right[2][0] != color and cubeModel.right[2][2] != color):
                return False
            color = cubeModel.back[1][1]
            if(cubeModel.back[2][0] != color and cubeModel.back[2][2] != color):
                return False
            color = cubeModel.left[1][1]
            if(cubeModel.left[2][0] != color and cubeModel.left[2][2] != color):
                return False
            return True
        else:
            return False
        
#checks if first and second layer are solved
def checkFirstTwoLayers(cubeModel):
    if(checkFirstLayer(cubeModel) == False):
        return False
    else:
        frontColor = cubeModel.front[1][1]
        rightColor = cubeModel.right[1][1]
        backColor = cubeModel.back[1][1]
        leftColor = cubeModel.left[1][1]
        
        if(cubeModel.front[1][2] != frontColor and cubeModel.right[1][0] != rightColor):
            return False
        if(cubeModel.right[1][2] != rightColor and cubeModel.back[1][0] != backColor):
            return False
        if(cubeModel.back[1][2] != backColor and cubeModel.left[1][0] != leftColor):
            return False
        if(cubeModel.left[1][2] != leftColor and cubeModel.left):
            return False
        return True