import unittest                         #Module for Unit Testing
from Game_Of_Life import Game           #Importing the code to be tested
import numpy as np

class Game_Of_Life_Testing(unittest.TestCase):

    def setUp(self):
        self.g=Game(3,3,[[0,0,0]],[[0,0,0]])     


    #Method to check working of Check_Grid method
    def test_Check_Grid(self):
        self.g.a1=[[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.g.Check_Grid(), True)

        self.g.a1=[[0,0,0],[0,8,0],[0,0,0]]
        self.assertEqual(self.g.Check_Grid(), False)

        self.g.a1==[[5,-1,0],[0,0,0],[0,0,5]]
        self.assertEqual(self.g.Check_Grid(), False)

        self.g.a1==[[0,5,0],[0,0,-1],[0,0,0]]
        self.assertEqual(self.g.Check_Grid(), False)
  
    #Method to check working of Stable_Grid method
    def test_Stable_Grid(self):
        self.g.a1=[[0,0,1],[0,1,0],[0,0,0]]
        self.g.a2=[[0,0,1],[0,1,0],[0,0,0]]
        self.assertEqual(self.g.Stable_Grid(),True)

        self.g.a1=[[0,0,6],[0,1,0],[0,0,0]]
        self.g.a2=[[0,0,7],[0,0,0],[0,0,0]]
        self.assertEqual(self.g.Stable_Grid(),False)
        
    #Method to check working of Next_Generation method
    def test_Next_Generation(self):
        l=[[0,0,6],[0,1,0],[0,0,0]]
        self.g.a2=np.reshape(l,(3,3))
        
        self.assertEqual(self.g.Next_Generation(3,1,1),1)

        self.assertEqual(self.g.Next_Generation(4,1,1),0)

        self.assertEqual(self.g.Next_Generation(1,1,1),0)


if __name__ == '__main__':
    unittest.main()