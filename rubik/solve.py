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
    cube = rubik.Cube()
    cube.convertString(cubeString)
    for rotation in rotations:
        if(rotation not in ['F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd']):
            result['status'] = 'error: invalid rotation'
            return result
        elif(rotation == 'F'):
            pass
    
    result['cube'] = cube.convertCube()
                             
    return result

def F(cube):
    pass