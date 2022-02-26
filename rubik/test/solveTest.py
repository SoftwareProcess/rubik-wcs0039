import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):

    def test_solve_H001_ShouldReturnOkOnValidCube(self):
        parms = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'F'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')


    