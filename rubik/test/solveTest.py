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
        
    def test_solve_H002_ShouldReturnFRotatedCubeOnEmptyRotate(self):
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
        
    def test_solveH016_ShouldReturnFRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'F'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'oggrbyboorwobrwgyggboggrrybwrybowyowbowyybbrwrgywwgroy')
        
    def test_solveH017_ShouldReturnfRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'f'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'oobybrggowwowrwyyggboggrrybwrgbobyorbowyybygrwrbwwgroy')
        
    def test_solveH018_ShouldReturnRRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'R'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'gywgbgoryrgyyrwgwogbobgrwybwrwboryobbooyyorbbywrwwgrog')
        
    def test_solveH019_ShouldReturnrRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'r'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'gywgbborgowgwryygryboggrwybwrwboryobboryygrbgywowworob')
        
    def test_solveH020_ShouldReturnBRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'B'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'gyogboorbywygroryrrggygbbrowrwoorbobowgyybrbgywwwwgwby')
        
    def test_solveH021_ShouldReturnbRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'b'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'gyogboorbywbgroryworbbgyggrrrwooryobybwyybrbgywwwwggwo')
        
    def test_solveH022_ShouldReturnLRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'L'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'byoyborrbywogrwryggbrggwryyybwoorbrwbowrybobggwwgwgooy')
        
    def test_solveH023_ShouldReturnlRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'l'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'yyowborrbywogrwryggbrggyrybwrbroowbygowgybobgbwwrwgooy')
        
    def test_solveH024_ShouldReturnURotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'U'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'ywogboorbgbogrwrygwrwggrrybgyoboryobrybbyogbwywwwwgroy')
        
    def test_solveH025_ShouldReturnuRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'u'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'wrwgboorbgyogrwrygywoggrrybgboboryobwbgoybbyrywwwwgroy')
        
    def test_solveH026_ShouldReturnDRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'D'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'gyogboyobywogrworbgboggrrygwrwborrybbowyybrbgrwyowwygw')
        
    def test_solveH027_ShouldReturndRotatedScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gyogboorbywogrwryggboggrrybwrwboryobbowyybrbgywwwwgroy',
                'rotate': 'd'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'gyogborygywogrwrybgboggryobwrwbororbbowyybrbgwgywwoywr')
        
    def test_solveY001_ShouldreturnFrRotatedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': 'Fr'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'bbybbybborrrrrryyywggwggrggoowoowoowyygyygoogrrbwwbwwb')
        
    def test_solveY002_ShouldSolveScrambledCube(self):
        parms = {'op':'solve',
                'cube':'bbogyoyoygrybrrrrbggrgwoobwwgwwowbrrgooygyowwgybwbbryy',
                'rotate': 'RULuDrDFLLUUflFdRRBBUUFFUURR'}
        result = solve._solve(parms)
        self.assertIn('cube', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        cube = result.get('cube', None)       
        self.assertEqual(cube, 'yyyyyyyyyrrrrrrrrrwwwwwwwwwooooooooogggggggggbbbbbbbbb')
        
    def test_SolveH028_CheckBottomCrossShouldReturnTrueOnSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertTrue(solve.checkDownCross(cubeTest) == True)
        
    def test_SolveH29_CheckBottomCrossShouldReturnFalseOnUnsolvedBottomCross(self):
        cubeString = 'bgbobywyyrbwbrgbbogygrgggwwyrwwowgrrrgryywooyboobwoory'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertFalse(solve.checkDownCross(cubeTest) == True)
        
    def test_SolveY003_CheckBottomCrossShouldReturnTrueOnSolvedBottomCross(self):
        cubeString = 'gooybgwbyyybyrbbrwobbrgbrgwrgroorbooyywryoygggwowwwrwg'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertTrue(solve.checkDownCross(cubeTest) == True)
            
    def test_solveH030_ShouldReturnEmptySolutionOnSolvedCube(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        self.assertTrue(len(solution) == 0)
        
    def test_solveH031_ShouldReturnEmptySolutionOnSolvedCubeEmptyRotate(self):
        parms = {'op':'solve',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                'rotate': ''}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        self.assertTrue(len(solution) == 0)        
    
    def test_solveH032_ShouldSolveFrontPieceOfBottomCrossOnMostlySolvedCross(self):
        parms = {'op':'solve',
                'cube':'bgbbgbbgbrrrrrrrrrgbggbggbgoooooooooyyyywyyyywwwwywwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'bgbbgbbgbrrrrrrrrrgbggbggbgoooooooooyyyywyyyywwwwywwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveH033_ShouldSolveCrossWithFlippedFrontDownFrontPiece(self):
        parms = {'op':'solve',
                'cube':'wybrboowbrrogryobgwgybgorgrgoryobwggowbwywgrywbyrwobyy'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'wybrboowbrrogryobgwgybgorgrgoryobwggowbwywgrywbyrwobyy',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
    
    def test_solveH034_ShouldSolveCrossWithFlippedFrontUpFrontPiece(self):
        parms = {'op':'solve',
                'cube':'ywwrbbyoygroyrybowwgyrgoggrgoryobwgrowbwywbbrgborwgbyo'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'ywwrbbyoygroyrybowwgyrgoggrgoryobwgrowbwywbbrgborwgbyo',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveH035_ShouldSolveCrossWithFlippedDownRightFrontPiece(self):
        parms = {'op':'solve',
                'cube':'roogbrroybrobrgrwgwgyrgorbogogyoywybowbwywwgywbbrwbgyy'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'roogbrroybrobrgrwgwgyrgorbogogyoywybowbwywwgywbbrwbgyy',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveH036_ShouldSolveCrossWithClockwiseFrontFrontPiece(self):
        parms = {'op':'solve',
                'cube':'gggbbworbwrobrbrbywgyrgogrbgowyoyyobowbwywryoyywgworgr'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'gggbbworbwrobrbrbywgyrgogrbgowyoyyobowbwywryoyywgworgr',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveH037_ShouldSolveCrossWithClockwiseRightFrontPiece(self):
        parms = {'op':'solve',
                'cube':'gbwrbyrobgrogrwrbowgybgoyrbgooyoyyogowbwywwrrybwgwyrgb'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'gbwrbyrobgrogrwrbowgybgoyrbgooyoyyogowbwywwrrybwgwyrgb',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveH038_ShouldSolveCrossWithFlippedClockwiseBackFrontPiece(self):
        parms = {'op':'solve',
                'cube':'yyrrbgbyggroorgorwwgyygbbrwgobwoyrorowbwywobyyowbwggbr'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'yyrrbgbyggroorgorwwgyygbbrwgobwoyrorowbwywobyyowbwggbr',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveH039_ShouldMostlySolveCrossWithUpRightFrontPiece(self):
        parms = {'op':'solve',
                'cube':'wrrybrryywbobrgrogwgyrgrybyoogyoogobbwbwywowgwgbgwbryo'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'wrrybrryywbobrgrogwgyrgrybyoogyoogobbwbwywowgwgbgwbryo',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        #checking for three pieces that should definitely be solved
        self.assertTrue((assertCube.down[0][1] == assertCube.down[1][1] and assertCube.front[2][1] == assertCube.front[1][1]) == True)
        self.assertTrue((assertCube.down[1][0] == assertCube.down[1][1] and assertCube.left[2][1] == assertCube.left[1][1]) == True)
        self.assertTrue((assertCube.down[2][1] == assertCube.down[1][1] and assertCube.back[2][1] == assertCube.back[1][1]) == True)
        
    def test_solveH040_ShouldMostlySolveCrossWithFlippedUpRightFrontPiece(self):
        parms = {'op':'solve',
                'cube':'wrbbbyobbywgoryybwygrgggrobbogroowyywwrwybowogyrrwrogg'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'wrbbbyobbywgoryybwygrgggrobbogroowyywwrwybowogyrrwrogg',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        #checking for three pieces that should definitely be solved
        self.assertTrue((assertCube.down[0][1] == assertCube.down[1][1] and assertCube.front[2][1] == assertCube.front[1][1]) == True)
        self.assertTrue((assertCube.down[1][0] == assertCube.down[1][1] and assertCube.left[2][1] == assertCube.left[1][1]) == True)
        self.assertTrue((assertCube.down[2][1] == assertCube.down[1][1] and assertCube.back[2][1] == assertCube.back[1][1]) == True)
        
    def test_solveH041_ShouldMostlySolveCrossWithFlippedUpBackFrontPiece(self):
        parms = {'op':'solve',
                'cube':'wgwrbgyowbrbrrybyoywyggbwbyborooboorrbowywgwoggrywrgyg'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'wgwrbgyowbrbrrybyoywyggbwbyborooboorrbowywgwoggrywrgyg',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        #checking for three pieces that should definitely be solved
        self.assertTrue((assertCube.down[0][1] == assertCube.down[1][1] and assertCube.front[2][1] == assertCube.front[1][1]) == True)
        self.assertTrue((assertCube.down[1][0] == assertCube.down[1][1] and assertCube.left[2][1] == assertCube.left[1][1]) == True)
        self.assertTrue((assertCube.down[1][2] == assertCube.down[1][1] and assertCube.right[2][1] == assertCube.right[1][1]) == True)
        
    def test_solveY004_ShouldSolveCrossWithFlippedCounterFrontFrontPieceAndDownBackRightPiece(self):
        parms = {'op':'solve',
                'cube':'wbbwbbroyrrorryobwwgwogggrbroryoboggbwbwyygoyyggrwyywo'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'wbbwbbroyrrorryobwwgwogggrbroryoboggbwbwyygoyyggrwyywo',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveY005_ShouldSolveCrossWithFlippedClcokwiseBackFrontPieceAndCounterRightRightPieceAndFlippedDownRightBackPiece(self):
        parms = {'op':'solve',
                'cube':'wbyrbgoywbrgorrbwyorrwgbbbrgogwoygywybywygoorbgrowgwyo'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'wbyrbgoywbrgorrbwyorrwgbbbrgogwoygywybywygoorbgrowgwyo',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveY006_ShouldSolveCrossOfScrambledCubed(self):
        parms = {'op':'solve',
                'cube':'wrryorrbyyowbwgogybogwrbbrywybwybgwwoyogbwrybgogrgorgo'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'wrryorrbyyowbwgogybogwrbbrywybwybgwwoyogbwrybgogrgorgo',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_solveY007_ShouldSolveCrossOfAnotherScrambledCubed(self):
        parms = {'op':'solve',
                'cube':'bgrbwbwwywoyygygbgbgoryyowryyogbwwrbgwrorbyogorrgorbow'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'bgrbwbwwywoyygygbgbgoryyowryyogbwwrbgwrorbyogorrgorbow',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)

    def test_solveY008_ShouldSolveCrossOfAThirdScrambledCubed(self):
        parms = {'op':'solve',
                'cube':'gogygwgwrowobrogwbbrbgbyrybryroorwgwybygwoybyogwryrobw'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'gogygwgwrowobrogwbbrbgbyrybryroorwgwybygwoybyogwryrobw',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)
        
    def test_SolveH042_CheckFirstLayerShouldReturnTrueOnSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertTrue(solve.checkFirstLayer(cubeTest) == True) 
        
    def test_SolveH043_CheckFirstLayerShouldReturnFalseOnSolvedBottomCross(self):
        cubeString = 'gooybgwbyyybyrbbrwobbrgbrgwrgroorbooyywryoygggwowwwrwg'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertFalse(solve.checkFirstLayer(cubeTest) == True)
        
    def test_SolveH044_CheckFirstLayerShouldReturnTrueOnSolvedFirstLayer(self):
        cubeString = 'oyorbobbbbrrgryrrryyyggbgggrygoobooogbboygyrywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertTrue(solve.checkFirstLayer(cubeTest) == True)
        
    def test_SolveH045_ShouldSolveFrontRightCornerInUpFROnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'oywrbbbborggyryyrryrrggbgggyygoobooobgroyoyrbwwbwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'oywrbbbborggyryyrryrrggbgggyygoobooobgroyoyrbwwbwwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)        
        
    def test_SolveH046_ShouldSolveFrontRightCornerInUpRBOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'yboybbbbobowyrygrrrrrggbgggggrooroooygboyybrywwywwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'yboybbbbobowyrygrrrrrggbgggggrooroooygboyybrywwywwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)
        
    def test_SolveH047_ShouldSolveFrontRightCornerInUpBLOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'orrybobbogoygrygrrbbwggbgggrryoorooobyrbyybgywwywwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'orrybobbogoygrygrrbbwggbgggrryoorooobyrbyybgywwywwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)
        
    def test_SolveH048_ShouldSolveFrontRightCornerInUpLFOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'ryrybgbboyryrrygrrobgggbgggyowoorooorybgybbobwwywwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'ryrybgbboyryrrygrrobgggbgggyowoorooorybgybbobwwywwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)
        
    def test_SolveH049_ShouldSolveFrontRightCornerInDownRBOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'yooybgbbobyrrrbgrbwyrygbrggyrgoorooobogbygrgywwywwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'yooybgbbobyrrrbgrbwyrygbrggyrgoorooobogbygrgywwywwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(assertCube.front[2][2] == assertCube.front[1][1] and assertCube.right[2][0] == assertCube.right[1][1] and assertCube.down[0][2] == assertCube.down[1][1])
                           
    def test_SolveH050_ShouldSolveFrontRightCornerInDownBLOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'yrrybrbbbggobroorryggbgoggbwyryobroooogryybgywwywwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'yrrybrbbbggobroorryggbgoggbwyryobroooogryybgywwywwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(assertCube.front[2][2] == assertCube.front[1][1] and assertCube.right[2][0] == assertCube.right[1][1] and assertCube.down[0][2] == assertCube.down[1][1]) 

    def test_SolveH051_ShouldSolveFrontRightCornerInDownRFOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'rbggbrrbbogrbroorrgybbgygggorbroyoobwoygyoyyywwywwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'rbggbrrbbogrbroorrgybbgygggorbroyoobwoygyoyyywwywwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(assertCube.front[2][2] == assertCube.front[1][1] and assertCube.right[2][0] == assertCube.right[1][1] and assertCube.down[0][2] == assertCube.down[1][1])
        
    def test_SolveH052_ShouldSolveRightBackCornerInUpBLOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'yroybobbbboggrbrrgyywrgyygggbrrobooorgroyybgywwwwwwwwo'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'yroybobbbboggrbrrgyywrgyygggbrrobooorgroyybgywwwwwwwwo',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)
        
    def test_SolveY009_ShouldSolveRightBackCornerInDownBLOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'yogybrbbbwrogryrrobbgggyggryyroobgooroyrybbgowwwwwwwwy'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'yogybrbbbwrogryrrobbgggyggryyroobgooroyrybbgowwwwwwwwy',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(assertCube.right[2][2] == assertCube.right[1][1] and assertCube.back[2][0] == assertCube.back[1][1] and assertCube.down[2][2] == assertCube.down[1][1])
        
    def test_SolveH053_ShouldSolveBackLeftCornerInUpRBOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'rryybrbbbggwgrgrrroyyogoggyboybobboorrgyyygbowwwwwwoww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'rryybrbbbggwgrgrrroyyogoggyboybobboorrgyyygbowwwwwwoww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)
        

    def test_SolveY010_ShouldSolveBackLeftCornerInDownBLOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'gobybrbbbrgrgrgrrgwboygyogyyyroobboogrgryoybywwwwwwoww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'gobybrbbbrgrgrgrrgwboygyogyyyroobboogrgryoybywwwwwwoww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(assertCube.back[2][2] == assertCube.back[1][1] and assertCube.left[2][0] == assertCube.left[1][1] and assertCube.down[2][0] == assertCube.down[1][1])
        
    def test_SolveH054_ShouldSolveLeftFrontCornerInUpFLOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'wybybgobbrgroryrrrgobggrgggybobooooyobyyyrbrygwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'wybybgobbrgroryrrrgobggrgggybobooooyobyyyrbrygwwwwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)  
        
    def test_SolveY011_ShouldSolveLeftFrontCornerInDownFROnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'rbrbbroboyrwyrybrrrooggrgggbyybooooyygboyggybgwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube': 'rbrbbroboyrwyrybrrrooggrgggbyybooooyygboyggybgwwwwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(assertCube.left[2][2] == assertCube.left[1][1] and assertCube.front[2][0] == assertCube.front[1][1] and assertCube.down[0][0] == assertCube.down[1][1])
        
    def test_SolveY012_ShouldSolveFirstLayerOfScrambledCube(self):
        parms = {'op':'solve',
                'cube':'oybobrgryowoyrgrgbgggwgbryyrwgwogboywrwoyryowrbbbwyobw'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'oybobrgryowoyrgrgbgggwgbryyrwgwogboywrwoyryowrbbbwyobw',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)   
        
    def test_SolveY013_ShouldSolveFirstLayerOfAnotherScrambledCube(self):
        parms = {'op':'solve',
                'cube':'gwyybowwgoyobrowybybbwggyygogrrooogrwrgwyrybbbrrowbwgr'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'gwyybowwgoyobrowybybbwggyygogrrooogrwrgwyrybbbrrowbwgr',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)
        
    def test_SolveY014_ShouldSolveFirstLayerOfThirdScrambledCube(self):
        parms = {'op':'solve',
                'cube':'ogyybrbrrgbgwrygwbwwrggrwogygyborrywboooyobworgwbwbyyo'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'ogyybrbrrgbgwrygwbwwrggrwogygyborrywboooyobworgwbwbyyo',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstLayer(assertCube) == True)
        
    def test_SolveY015_ShouldSolveFirstLayerOfFailedIteration2AcceptanceTestCube(self):
        parms = {'op':'solve',
                'cube':'EEtEttEttjOOOjjOjjEttEEtEEtOjjjOOjOOAAAAnAnAnnnnnAnAnA'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        #putting provided solution into solve as 'rotate' to check if bottom cross is solved
        assertParms = {'op':'solve',
                       'cube':'EEtEttEttjOOOjjOjjEttEEtEEtOjjjOOjOOAAAAnAnAnnnnnAnAnA',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkDownCross(assertCube) == True)    
            
    def test_SolveH055_CheckFirstTwoLayersShouldReturnTrueOnSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertTrue(solve.checkFirstTwoLayers(cubeTest) == True)
    
    def test_SolveH056_CheckFirstTwoLayersShouldReturnFalseOnUnSolvedSecondLayer(self):
        cubeString = 'oyyobobbbrroyrgrrrbbrogbgggyrgrobooobyyyyhyggwwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertTrue(solve.checkFirstTwoLayers(cubeTest) == False)
        
    def test_SolveH057_CheckFirstTwoLayersShouldReturnTrueOnSolvedF2L(self):
        cubeString = 'obbbbbbbbryrrrrrrrggoggggggbygooooooyyyryoyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertTrue(solve.checkFirstTwoLayers(cubeTest) == True)
        
    def test_solveH058_RightFrontTriggerShouldPerformCorrectRotationsOnSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        solve.rightFrontTrigger(cubeTest)
        assertString = 'ybbbbobbywrryrrrrrggoggggggbboooooooyyyyyygrrwwbwwwwww'
        self.assertEqual(cubeTest.convertCube(), assertString)
        
    def test_solveH059_RightBackTriggerShouldPerformCorrectRotationsOnSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        solve.rightBackTrigger(cubeTest)
        assertString = 'obbbbbbbbrrwrryrrrggyoggyggoggoooooobrryyyyyywwwwwwwwg'
        self.assertEqual(cubeTest.convertCube(), assertString)
        
    def test_solveH060_BackRightTriggerShouldPerformCorrectRotationsOnSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        solve.backRightTrigger(cubeTest)
        assertString = 'rrbbbbbbbyrrrrbrrywggygggggoobooooooyygyygyyowwwwwwwwr'
        self.assertEqual(cubeTest.convertCube(), assertString)
    
    def test_solveH061_LeftBackTriggerShouldPerformCorrectRotationsOnSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        solve.leftBackTrigger(cubeTest)
        assertString = 'bbrbbbbbbggrrrrrrryggggrggywooyooooooobyyyyyywwwwwwgww'
        self.assertEqual(cubeTest.convertCube(), assertString)
        
    def test_solveH062_LeftFrontTriggerShouldPerformCorrectRotationsOnSolvedCube(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        solve.leftFrontTrigger(cubeTest)
        assertString = 'bbyrbbybbrbbrrrrrrrggggggggoowooyoooyyyyyyoogbwwwwwwww'
        self.assertEqual(cubeTest.convertCube(), assertString)

    def test_SolveH063_ShouldSolveFrontRightMiddleEdgeInTopLayerOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'ybbbbybbbryygrrrrrorrgggggggboooooooyybyyogrywwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        assertParms = {'op':'solve',
                       'cube': 'ybbbbybbbryygrrrrrorrgggggggboooooooyybyyogrywwwwwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstTwoLayers(assertCube) == True)
        
    def test_SolveY016_CheckEdgeShouldReturnTrueOnCorrectEdgeAndFalseOnIncorrectEdge(self):
        cubeString = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        cubeTest = rubik.Cube()
        cubeTest.convertString(cubeString)
        self.assertTrue(solve.checkEdge((cubeTest.front[0][1], cubeTest.up[2][1]), cubeTest.front[1][1], cubeTest.up[1][1]) == True)
        self.assertTrue(solve.checkEdge((cubeTest.front[1][2], cubeTest.right[1][0]), cubeTest.up[1][1], cubeTest.back[1][1]) == False)
        
    def test_SolveH064_ShouldSolveRightBackMiddleEdgeInTopLayerOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'obybbbbbbrryrrgrrrboyygggggorgoooooobyrgyyyygwwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        assertParms = {'op':'solve',
                       'cube': 'obybbbbbbrryrrgrrrboyygggggorgoooooobyrgyyyygwwwwwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstTwoLayers(assertCube) == True)
        
    def test_SolveH065_ShouldSolveFlippedFrontRightMiddleEdgeInTopLayerOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'grybbybbbbyrrrrrrrgyyggggggooyoooooobbyyygobrwwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        assertParms = {'op':'solve',
                       'cube': 'grybbybbbbyrrrrrrrgyyggggggooyoooooobbyyygobrwwwwwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstTwoLayers(assertCube) == True)
        
    def test_SolveH066_ShouldSolveFlippedRightBackMiddleEdgeInTopLayerOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'obybbbbbbrgyrryrrrboyrgggggoggoooooobyryyryygwwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        assertParms = {'op':'solve',
                       'cube': 'obybbbbbbrgyrryrrrboyrgggggoggoooooobyryyryygwwwwwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstTwoLayers(assertCube) == True)
        
    def test_SolveH067_ShouldSolveBackLeftMiddleEdgeInTopLayerOnMostlySolvedFirstLayer(self):
        parms = {'op':'solve',
                'cube':'gbybbbbbbryrrrrrrrygbggygggyrygooooooobyyooygwwwwwwwww'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        solution = result.get('solution', None)
        assertParms = {'op':'solve',
                       'cube': 'gbybbbbbbryrrrrrrrygbggygggyrygooooooobyyooygwwwwwwwww',
                       'rotate': solution}
        assertResult = solve._solve(assertParms)
        assertString = assertResult.get('cube', None)
        assertCube = rubik.Cube()
        assertCube.convertString(assertString)
        self.assertTrue(solve.checkFirstTwoLayers(assertCube) == True)