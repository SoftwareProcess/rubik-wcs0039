import unittest
import rubik.cube as rubik

class CubeTest(unittest.TestCase):

    def test_cube_H001_ShouldInitSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        testCube = rubik.Cube()
        assertCube = [[['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
                     [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
                     [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
                     [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
                     [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
                     [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]]
        testCube.convertString(cubeString)
        self.assertEqual(testCube.cube, assertCube)
        
    def test_cube_H002_ShouldClockwiseRotateFrontFace(self):
        cubeString = 'gbygbygbyrrrrrrrrrwgbwgbwgbooooooooowygwygwygywbywbywb'
        #       cube = [[['g', 'b', 'y'], ['g', 'b', 'y', ['g', 'b', 'y'],
        #              [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
        #              [['w', 'g', 'b'], ['w', 'g', 'b'], ['w', 'g', 'b']],
        #              [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
        #              [['w', 'y', 'g'], ['w', 'y', 'g'], ['w', 'y', 'g']],
        #              [['y', 'w', 'b'], ['y', 'w', 'b'], ['y', 'w', 'b']]]
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        assertFace = [['g', 'g', 'g'], ['b','b','b'], ['y', 'y', 'y']]
        testCube.faceClockwise(0)
        self.assertEqual(testCube.cube[0], assertFace)
        
    def test_cube_H003_ShouldCounterclockwiseRotateFrontFace(self):
        cubeString = 'gbygbygbyrrrrrrrrrwgbwgbwgbooooooooowygwygwygywbywbywb'
        #       cube = [[['g', 'b', 'y'], ['g', 'b', 'y', ['g', 'b', 'y'],
        #              [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
        #              [['w', 'g', 'b'], ['w', 'g', 'b'], ['w', 'g', 'b']],
        #              [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
        #              [['w', 'y', 'g'], ['w', 'y', 'g'], ['w', 'y', 'g']],
        #              [['y', 'w', 'b'], ['y', 'w', 'b'], ['y', 'w', 'b']]]
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        assertFace = [['y', 'y', 'y'], ['b','b','b'], ['g', 'g', 'g']]
        testCube.faceCounterclockwise(0)
        self.assertEqual(testCube.cube[0], assertFace)
        
    def test_cube_H004_ShouldClockwiseRotateScrambledFrontFace(self):
        cubeString = 'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy'
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        assertFace = [['o', 'g', 'g'], ['r','b','y'], ['b', 'o', 'o']]
        testCube.faceClockwise(0)
        self.assertEqual(testCube.cube[0], assertFace)
        
    def test_cube_H005_ShouldCounterclockwiseRotateScrambledFrontFace(self):
        cubeString = 'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy'
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        assertFace = [['o', 'o', 'b'], ['y','b','r'], ['g', 'g', 'o']]
        testCube.faceCounterclockwise(0)
        self.assertEqual(testCube.cube[0], assertFace)
        
    def test_cube_H006_ShouldConvertRotatedCubeToString(self):
        cubeString = 'gbygbygbyrrrrrrrrrwgbwgbwgbooooooooowygwygwygywbywbywb'
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        testCube.faceClockwise(0)
        cubeString = testCube.convertCube()
        assertString = 'gggbbbyyyrrrrrrrrrwgbwgbwgbooooooooowygwygwygywbywbywb'
        self.assertEqual(cubeString, assertString)
    
    def test_cube_H007_ShouldTurnSolvedCubeFacesRight(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        testCube.turnCubeRight()
        cubeString = testCube.convertCube()
        assertString = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        self.assertEqual(cubeString, assertString)
    
    def test_cube_H008_ShouldTurnScrambledCubeFacesRight(self):
        cubeString = 'wbwogygbybybrywgrryyrgbbwgwyrgwwwrwoboobrgoyoyorroggob'
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        testCube.turnCubeRight()
        cubeString = testCube.convertCube()
        assertString = 'yrgwwwrwowbwogygbybybrywgrryyrgbbwgwogoorybbogryooobgr'
        self.assertEqual(cubeString, assertString) 
        
    def test_cube_H009_ShouldTurnSolvedCubeFacesLeft(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        testCube.turnCubeLeft()
        cubeString = testCube.convertCube()
        assertString = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        self.assertEqual(cubeString, assertString)      