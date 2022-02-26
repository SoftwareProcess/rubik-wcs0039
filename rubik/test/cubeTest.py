import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):

    def test_check_H001_ShouldInitSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        testCube = cube.Cube()
        assertCube = [[['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
                     [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
                     [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
                     [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
                     [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
                     [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]]
        self.assertEqual(testCube.cube, assertCube)
