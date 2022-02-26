class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self):
        #storing the whole cube as list with each face represented as a 3x3 matrix in a 2d list
        #face order: front, right, back, left, up, down
        self.cube = [[['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']],
                     [['', '', ''], ['', '', ''], ['', '', '']]]

    
    def convertString(self, cubeString):
        stringIndex = 0
        for face in self.cube:
            for row in range(len(face)):
                for column in range(len(face[0])):
                    face[row][column] = cubeString[stringIndex]
                    stringIndex += 1

    #creates a new face makes it the clockwise rotation of the original(old) face
    def faceClockwise(self, faceNumber):
        rotatedFace = [['', '', ''], ['', '', ''], ['', '', '']]
        face = self.cube[faceNumber]
        
        row = 0
        for oldColumn in range(len(face[0])):
            column = 0
            for oldRow in range(len(face)): 
                rotatedFace[row][column] = face[oldRow][oldColumn]
                column -= 1
            row -= 1
        
        self.cube[faceNumber] = rotatedFace
        
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