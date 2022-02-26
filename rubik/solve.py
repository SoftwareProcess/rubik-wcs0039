import rubik.cube as rubik
import rubik.check as check

def _solve(parms):
    result = check._check(parms) #using _.check to validate cube
    if(result.get('status') != 'ok'):
        return result 
    rotations = parms.get('rotate', None)
    for rotation in rotations: #validating rotations
        if(rotation not in ['F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd']):
            result['status'] = 'error: invalid rotation'
        
    cubeString = parms.get('cube',None)
    
                         
    return result