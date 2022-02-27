import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):

    def test_solve_H001_ShouldReturnOkOnValidCubeFRotate(self):
        parms = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'F'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_solve_H002_ShouldReturnOkOnEmptyRotate(self):
        parms = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': ''}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_solve_H003_ShouldReturnOkOnNoRotate(self):
        parms = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_solve_S001_ShouldReturnErrorOnInvalidCube(self):
        parms = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'F'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is not the right length')
        
           


    