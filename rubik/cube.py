import copy

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self):
        #storing the whole cube as list with each face represented as a 3x3 matrix in a 2d list
        #face order: front, right, back, left, up, down i.e. cube[0] = front, cube[1] = right, etc.
        self.cube = [[['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']]]
        self.front = self.cube[0]
        self.right = self.cube[1]
        self.back = self.cube[2]
        self.left = self.cube[3]
        self.up = self.cube[4]
        self.down = self.cube[5]

    
    #converts the string representation of the cube into the cube model
    def convertString(self, cubeString):
        stringIndex = 0
        for face in self.cube:
            for row in range(len(face)):
                for column in range(len(face[0])):
                    face[row][column] = cubeString[stringIndex]
                    stringIndex += 1
                    
    #takes the current cube model and returns its string representation
    def convertCube(self):
        cubeString = ''
        for face in self.cube:
            for row in range(len(face)):
                for column in range(len(face[0])):
                    cubeString += face[row][column]
        
        return cubeString

    #creates a new face makes it the clockwise rotation of the original(old) face
    def faceClockwise(self, faceNumber):
        rotatedFace = [['', '', ''], ['', '', ''], ['', '', '']]
        face = self.cube[faceNumber]
        
        row = 0
        for oldColumn in range(len(face[0])):
            column = 2
            for oldRow in range(len(face)): 
                rotatedFace[row][column] = face[oldRow][oldColumn]
                column -= 1
            row += 1
        
        self.cube[faceNumber] = rotatedFace
        self.front = self.cube[0]
        self.right = self.cube[1]
        self.back = self.cube[2]
        self.left = self.cube[3]
        self.up = self.cube[4]
        self.down = self.cube[5]
        
    #creates a new face makes it the clockwise rotation of the original(old) face
    def faceCounterclockwise(self, faceNumber):
        rotatedFace = [['', '', ''], ['', '', ''], ['', '', '']]
        face = self.cube[faceNumber]
        
        row = 0
        for oldColumn in range(len(face[0]) - 1, -1, -1):
            column= 0
            for oldRow in range(len(face)):
                rotatedFace[row][column] = face[oldRow][oldColumn]
                column+= 1
            row += 1
        
        self.cube[faceNumber] = rotatedFace
        self.front = self.cube[0]
        self.right = self.cube[1]
        self.back = self.cube[2]
        self.left = self.cube[3]
        self.up = self.cube[4]
        self.down = self.cube[5]
        
    #turns the faces of the cube rightward (i.e. the front face becomes the right face)
    def turnCubeRight(self):
        self.faceCounterclockwise(4)
        self.faceClockwise(5)        
        cubeCopy = copy.deepcopy(self)
        self.cube[0] = cubeCopy.cube[3]
        self.cube[1] = cubeCopy.cube[0]
        self.cube[2] = cubeCopy.cube[1]
        self.cube[3] = cubeCopy.cube[2]
        self.front = self.cube[0]
        self.right = self.cube[1]
        self.back = self.cube[2]
        self.left = self.cube[3]
        
    #turns the faces of the cube leftward (i.e. the right face becomes the front face)
    def turnCubeLeft(self):
        self.faceClockwise(4)
        self.faceCounterclockwise(5)
        cubeCopy = copy.deepcopy(self)
        self.cube[0] = cubeCopy.cube[1]
        self.cube[1] = cubeCopy.cube[2]
        self.cube[2] = cubeCopy.cube[3]
        self.cube[3] = cubeCopy.cube[0]
        self.front = self.cube[0]
        self.right = self.cube[1]
        self.back = self.cube[2]
        # self.left = self.cube[3] 