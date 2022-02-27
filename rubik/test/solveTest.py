import unittest
import rubik.solve as solve
import rubik.cube as rubik

class SolveTest(unittest.TestCase):

    def test_solve_H001_ShouldReturnOkOnValidCubeFRotate(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'F'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_solve_H002_ShouldReturnOkOnEmptyRotate(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': ''}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_solve_H003_ShouldReturnOkOnNoRotate(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_solve_S001_ShouldReturnErrorOnInvalidCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'F'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is not the right length')
        
    def test_solveS002_ShouldReturnErrorOnInvalidRotation(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'w'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: invalid rotation')
        
    def test_solveH004_ShouldReturnFRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'F'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbbbbbbbbyrryrryrrgggggggggoowoowoowyyyyyyooorrrwwwwww')
        # cube = [[['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
        #        [['y', 'r', 'r'], ['y', 'r', 'r'], ['y', 'r', 'r']],
        #        [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        #        [['o', 'o', 'w'], ['o', 'o', 'w'], ['o', 'o', 'w']],
        #        [['y', 'y', 'y'], ['y', 'y', 'y'], ['o', 'o', 'o']],
        #        [['r', 'r', 'r'], ['w', 'w', 'w'], ['w', 'w', 'w']]]
        
    def test_solveH005_ShouldReturnfRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'f'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbbbbbbbbwrrwrrwrrgggggggggooyooyooyyyyyyyrrrooowwwwww')
        
    def test_solveH006_ShouldReturnRRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'R'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbwbbwbbwrrrrrrrrryggyggyggoooooooooyybyybyybwwgwwgwwg')
        
    def test_solveH007_ShouldReturnrRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'r'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbybbybbyrrrrrrrrrwggwggwggoooooooooyygyygyygwwbwwbwwb')
        
    def test_solveH008_ShouldReturnBRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'B'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbbbbbbbbrrwrrwrrwgggggggggyooyooyoorrryyyyyywwwwwwooo')
        
    def test_solveH009_ShouldReturnbRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'b'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbbbbbbbbrryrryrrygggggggggwoowoowoooooyyyyyywwwwwwrrr')
        
    def test_solveH010_ShouldReturnLRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'L'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'ybbybbybbrrrrrrrrrggwggwggwooooooooogyygyygyybwwbwwbww')
        
    def test_solveH011_ShouldReturnlRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'l'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'wbbwbbwbbrrrrrrrrrggyggyggyooooooooobyybyybyygwwgwwgww')
        
    def test_solveH012_ShouldReturnURotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'U'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'rrrbbbbbbgggrrrrrroooggggggbbbooooooyyyyyyyyywwwwwwwww')
        
    def test_solveH013_ShouldReturnuRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'u'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'ooobbbbbbbbbrrrrrrrrrgggggggggooooooyyyyyyyyywwwwwwwww')
        
    def test_solveH014_ShouldReturnDRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'D'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbbbbbooorrrrrrbbbggggggrrroooooogggyyyyyyyyywwwwwwwww')
        
    def test_solveH015_ShouldReturndRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'd'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbbbbbrrrrrrrrrgggggggggooooooooobbbyyyyyyyyywwwwwwwww')
              