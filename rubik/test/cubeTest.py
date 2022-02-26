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
        
    def test_cube_H004_ShouldConvertRotatedCubeToString(self):
        cubeString = 'gbygbygbyrrrrrrrrrwgbwgbwgbooooooooowygwygwygywbywbywb'
        testCube = rubik.Cube()
        testCube.convertString(cubeString)
        testCube.faceClockwise(0)
        cubeString = testCube.convertCube()
        assertString = 'gggbbbyyyrrrrrrrrrwgbwgbwgbooooooooowygwygwygywbywbywb'
        self.assertEqual(cubeString, assertString)
        