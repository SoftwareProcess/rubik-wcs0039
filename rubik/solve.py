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
    U(cubeModel)
    U(cubeModel)
    solution += 'UU' + locateBottomEdge(cubeModel, downColor, backColor) + 'UU'
    U(cubeModel)
    U(cubeModel)
    
    #solve left edge
    u(cubeModel)
    solution += 'u' + locateBottomEdge(cubeModel, downColor, leftColor) + 'U'
    U(cubeModel)
    
    
    #rotating edges from daisy position to solved position   
    F(cubeModel)
    F(cubeModel)
    R(cubeModel)
    R(cubeModel)
    B(cubeModel)
    B(cubeModel) 
    L(cubeModel)
    L(cubeModel)
    solution += 'FFRRBBLL'
    return solution 
    
def locateBottomEdge(cubeModel, downColor, frontColor):
    solution = ''
    #check if front edge is in down of front (true solved position)
    if(cubeModel.down[0][1] == downColor and cubeModel.front[2][1] == frontColor):
        F(cubeModel)
        F(cubeModel)
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
        R(cubeModel)
        R(cubeModel)
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
        D(cubeModel)
        D(cubeModel)
        F(cubeModel)
        F(cubeModel)
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
        F(cubeModel)
        F(cubeModel)
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
        L(cubeModel)
        L(cubeModel)
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
        F(cubeModel)
        F(cubeModel)
        R(cubeModel)
        R(cubeModel)
        d(cubeModel)
        F(cubeModel)
        F(cubeModel)
        solution += 'FFRRdFF'
    #check if front edge is flipped in up of right
    elif(cubeModel.up[1][2] == frontColor and cubeModel.right[0][1] == downColor):
        F(cubeModel)
        F(cubeModel)
        r(cubeModel)
        f(cubeModel)
        solution += 'FFrf'
    #check if front edge is in up of back
    elif(cubeModel.up[0][1] == downColor and cubeModel.back[0][1] == frontColor):
        F(cubeModel)
        F(cubeModel)
        B(cubeModel) 
        B(cubeModel)
        D(cubeModel)
        D(cubeModel)
        F(cubeModel)
        F(cubeModel)
        solution += 'FFBBDDFF' 
    #check if front edge is flipped in up of back
    elif(cubeModel.up[0][1] == frontColor and cubeModel.back[0][1] == downColor):
        F(cubeModel)
        F(cubeModel)
        B(cubeModel) 
        B(cubeModel)
        D(cubeModel)
        D(cubeModel)
        f(cubeModel)
        u(cubeModel)
        R(cubeModel)
        U(cubeModel)
        solution += 'FFBBDDfuRU'
    #check if front edge is in up of left 
    elif(cubeModel.up[1][0] == downColor and cubeModel.left[0][1] == frontColor):
        F(cubeModel)
        F(cubeModel)
        L(cubeModel)
        L(cubeModel)
        D(cubeModel)
        F(cubeModel)
        F(cubeModel)
        solution += 'FFLLDFF'
    #check if front edge is flipped in up of left 
    elif(cubeModel.up[1][0] == frontColor and cubeModel.left[0][1] == downColor):
        F(cubeModel)
        F(cubeModel)
        L(cubeModel)
        L(cubeModel)
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
    D(cubeModel)
    D(cubeModel)
    solution += 'DD' + locateCorner(cubeModel, downColor, backColor, leftColor) + 'DD'
    D(cubeModel)
    D(cubeModel)

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
        U(cubeModel)
        U(cubeModel)
        solution += 'UU' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #Corner in left/front up position
    if(checkCorner((cubeModel.up[2][0], cubeModel.left[0][2], cubeModel.front[0][0]), downColor, frontColor, rightColor)):
        u(cubeModel)
        solution += 'u' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #Corner in front/right down position (solved)
    if(checkCorner((cubeModel.down[0][2], cubeModel.front[2][2], cubeModel.right[2][0]), downColor, frontColor, rightColor)):
        pass
    #Corner in right/back down position
    if(checkCorner((cubeModel.down[2][2], cubeModel.right[2][2], cubeModel.back[2][0]), downColor, frontColor, rightColor)):
        r(cubeModel)
        U(cubeModel)
        U(cubeModel)
        R(cubeModel)
        u(cubeModel)
        solution += 'rUURu' + solveDownCorner(cubeModel, downColor, frontColor, rightColor)
    #Corner in back/left down position
    if(checkCorner((cubeModel.down[2][0], cubeModel.back[2][2], cubeModel.left[2][0]), downColor, frontColor, rightColor)):
        L(cubeModel)
        U(cubeModel)
        U(cubeModel)
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
            if(cubeModel.front[2][0] != color or cubeModel.front[2][2] != color):
                return False
            color = cubeModel.right[1][1]
            if(cubeModel.right[2][0] != color or cubeModel.right[2][2] != color):
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