from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_001_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

    def test_check_002_ShouldReturnErrorOnNonStringCube(self):
        parm = {'op':'check',
                'cube': 42}
        result = check._check(parm)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is not a string')
        
    def test_check_003_ShouldReturnErrorOnShortCube(self):
        parm = {'op':'check',
                'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwww'}
        result = check._check(parm)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is not the right length')
    
    def test_check_004_ShouldReturnErrorOnLongCube(self):
        parm = {'op':'check',
                'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'}
        result = check._check(parm)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is not the right length')
        
    def test_check_005_ShouldReturnErrorOnReallyShortCube(self):
        parm = {'op':'check',
                'cube': 'b'}
        result = check._check(parm)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is not the right length')
    
    def test_check_006_ShouldReturnErrorOnReallyLongCube(self):
        parm = {'op':'check',
                'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'}
        result = check._check(parm)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube is not the right length')
        
    def test_check_007_ShouldReturnErrorOnInvalidCharacter(self):
        parm = {'op':'check',
                'cube': '*********rrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        status = result.get('status', None)
        self.assertEqual(status, 'error: invalid character')
        
    def test_check_008_ShouldReturnErrorOnTooManyColors(self):
        parm = {'op':'check',
                'cube':'WWbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: too many colors')
        
    def test_check_009_ShouldReturnErrorOnTooFewColors(self):
        parm = {'op':'check',
                'cube':'rrrrrrrrrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: too few colors')
    
    def test_check_010_ShouldReturnErrorOnUnequalColors(self):
        parm = {'op':'check',
                'cube':'wbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: colors are not equal')
    
    def test_check_011_ShouldReturnErrorOnDuplicateCenter(self):
        parm = {'op':'check',
                'cube':'bbrbrbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: centers are not a unique color')
        
    def test_check_012_ShouldReturnOkOnScrambledCube(self):
        parm = {'op':'check',
                'cube':'gybrbgggoobgowwwyboboggryorbbwwygwyyywyorrrbwrygroobwr'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_013_ShouldReturnOkOnDifferentCharacter(self):
        parm = {'op':'check',
                'cube':'aaaaaaaaarrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')