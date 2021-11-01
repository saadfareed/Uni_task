from puzzle import Puzzle as pz
import numpy as np

def main():     
    #defining our state
    initial_state=[3,4,1,2,5,6,7,8,-1]  #here -1 indicates blank tile
    goal_state=[1,2,3,4,5,6,7,8,-1]

    #making an object of type puzzle that is ym custom class
    pz_board=pz(initial_state,goal_state)

    choice=menu()
    #pz_board.solvePuzzle()
    if choice==1:
        level=int(input("Enter Level of Tree or press -1 to see all paths = "))
        if(level==-1):
            pz_board.printPaths()
        elif(level>=0):  #making sure that level is +ve
            pz_board.printPaths(level)
        else : #user has enter -ve depth  so display error
            print("Error.........Invalid Depth.")
    elif  choice ==2 :  #Than Solve The Puzzle
        pz_board.solvePuzzle()
    elif  choice ==3 :  #Than Display The Game Initial State
        print("Printing Initial state of Game Board .")
        #making these lists as  a numpy array
        initial=(np.array(initial_state)).reshape(3,3)
        print(initial)
    elif  choice ==4 :    #Than Goal The Game Initial State
        #making these lists as  a numpy array
        goal=(np.array(goal_state)).reshape(3,3)
        print(goal)




def menu():
    print("\t\t\t\t\t****Displaying Menu****")
    print("\t 1)Display Tree Of Paths")
    print("\t 2)Display Solution to Goal Node using A*.")
    print("\t 3)Display Initil State.")
    print("\t 3)Display Goal State.")
    choice = input("\n\n\tEnter your choice = ")
    return int(choice)
    

#calling main function
main()


