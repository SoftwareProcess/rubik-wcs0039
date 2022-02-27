import copy
import rubik.cube as rubik
import rubik.check as check

def _solve(parms):
    result = check._check(parms) #using _.check to validate cube
    if(result['status'] != 'ok'):
        return result
    if('rotate' in parms):
        if('rotate' == ''):
            rotations = 'F'
        else:
            rotations = parms.get('rotate', None)
    else:
        rotations = 'F'
        
    cubeString = parms.get('cube',None)
    cubeModel = rubik.Cube()
    cubeModel.convertString(cubeString)
    for rotation in rotations:
        if(rotation not in ['F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd']):
            result['status'] = 'error: invalid rotation'
            return result
        elif(rotation == 'F'):
            F(cubeModel)
    
    result['cube'] = cubeModel.convertCube() #converting back into string representation
                             
    return result

def F(cubeModel):
    cubeModel.faceClockwise(0) #rotating front face
    cube = cubeModel.cube 
    copyModel = copy.copy(cubeModel)
    copyCube = copyModel.cube
    cube.right[0][0] = copyCube.up[2][0], cube.right[1][0] = copyCube.up[2][1], cube.right[2][0] = copyCube.up[2][2]
    cube.left[0][2] = copyCube.down[0][0], cube.left[1][2] = copyCube.down[0][1], cube.left[2][2] = copyCube.down[0][2]
    cube.up[2][0] = copyCube.left[0][2], cube.up[2][1] = copyCube.left[1][2], cube.up[2][2] = copyCube.left[2][2]
    cube.down[0][0] = copyCube.right[0][0], cubeCube.down[0][1] = copy.right[1][0], cube.down[0][2] = copyCube.right[2][0]
    
    
    
    