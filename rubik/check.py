#import rubik.cube as rubik

def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)       
    if(encodedCube == None):
        result['status'] = 'error: cube is missing'
    else:
        result['status'] = 'ok'
    
    if(isinstance(encodedCube, str) == False):
        result['status'] = 'error: cube is not a string'
        return result
        
    if(len(encodedCube) != 54):
        result['status'] = 'error: cube is not the right length'
        return result
    
    for char in encodedCube:
        if(char.isalpha() == False and char.isdecimal() == False):
            result['status'] = 'error: invalid character'
            return result
    
    colors = [] #list to store characters
    for char in encodedCube:
        if(char not in colors):
            colors.append(char)
    if(len(colors) > 6):
        result['status'] = 'error: too many colors'
        return result
    
    if(len(colors) < 6):
        result['status'] = 'error: too few colors'
        return result
    
    for color in colors:
        num = encodedCube.count(color)
        if(num != 9):
            result['status'] = 'error: colors are not equal'
    
    centers = [encodedCube[4], encodedCube[13], encodedCube[22], encodedCube[31], encodedCube[40], encodedCube[49]]
    if(len(set(centers)) != len(centers)):
        result['status'] = 'error: centers are not a unique color'
    
    return result