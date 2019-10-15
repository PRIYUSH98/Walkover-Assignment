import sys                #For Exit Function
import random             #For Random Initialization of Grid
import numpy as np        #For Maintaining Grid

#Defining  class for Game Of Life
class Game:

    def __init__(self,r,c,a1,a2): 
        self.r=r      # No.of Rows
        self.c=c      # No.of Columns   
        self.a1=a1    # Input Grid
        self.a2=a2    # New Generation Grid
        self.n=True   

     
    def CheckGrid(self):        #Function to Check that all inputs to the Grid are Either 1 or 0
        for i in range(0,self.r):
            for j in range(0,self.c):
                if(self.a1[i][j]==0 or self.a1[i][j]==1):
                    continue
                else:
                    print("Invalid Input")    
                    sys.exit()

    def InputGrid(self):         #Function to Print the Input Grid
        print("Input Colony:")
        print(self.a1)

    def Next_Generation_Computer(self):       #Function To Compute Next Generation 
        while(self.n==True):
            for i in range(0,self.r):

                for j in range(0,self.c):
                    count=0

                    #Not Checking Boundary Conditions when not a boundary postion of Grid
                    if(i-1>=0 and j-1>=0 and i+1<=self.r-1 and j+1<=self.c-1):  

                        count=self.a1[i-1,j-1] + self.a1[i-1,j] + self.a1[i-1,j+1] + self.a1[i,j+1]+ self.a1[i,j-1] + self.a1[i+1,j-1] +self.a1[i+1,j+1]+self.a1[i+1,j]
                    
                    else:                                                       #Checking Boundary Conditions
                        if((i-1)>=0):
                            count+=self.a1[i-1,j]
                        if((i+1)<self.r):
                            count+=self.a1[i+1,j]
                        if((i+1)<self.r and (j+1)<self.c):
                            count+=self.a1[i+1,j+1]
                        if((i-1)>=0 and (j+1)<self.c):
                            count+=self.a1[i-1,j+1]
                        if((i+1)<self.r and (j-1)>=0):
                            count+=self.a1[i+1,j-1]
                        if((i-1)>=0 and (j-1)>=0):
                            count+=self.a1[i-1,j-1]
                        if((j+1)<self.c):
                            count+=self.a1[i,j+1]
                        if((j-1)>=0):
                            count+=self.a1[i,j-1]

                    #Assigning values to Next Generation Grid 
                    if(count==2 and self.a1[i][j]==1):
                        self.a2[i,j]=1
                    else:
                        if(count==3):
                            self.a2[i,j]=1
                        
                        else:
                            self.a2[i,j]=0

            #Checking whether the Final Colony Computed                
            if(np.array_equal(self.a2,self.a1)):
                self.n=False

            #Copying the Values of Next Generation to Current Generation
            self.a1=np.array(self.a2,copy=True)
        
        #Printing The Final Colony
        print("Final Colony:")
        print(self.a2)                   

        
def main():
    
    #Taking Inputs From The User
    print("Enter no. of rows in Grid:")
    r=int(input())              
    print("Enter no. of columns in Grid:")
    c=int(input()) 
    l=list()  

    print("For entering the position of cells manually Press 1 \nFor entering the position of cells automatically Press 0")
    value=int(input())

    if(value==1):
        
        for i in range(0,r):
            for j in range(0,c):
                x=int(input())
                l.append(x)
    else:

        if(value==0):
            for i in range(0,r):
                for j in range(0,c):
                    x=random.randrange(0,2)
                    l.append(x)

        else:
            print("Invalid Input")
            sys.exit()

    a1=np.reshape(l,(r,c))
    a2=np.array(a1,copy=True)

    g=Game(r,c,a1,a2)     #Object Creation of Class Game

    g.CheckGrid()
    
    g.InputGrid()

    g.Next_Generation_Computer()

if __name__ =="__main__":
    main() 