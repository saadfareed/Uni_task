#print("Allah Almighty Is Greatest OF All")
import numpy as np
from Queue import Queue as q
from PQueue import PriorityQueue as PQ

class Puzzle:
    #accepts a 1 dimensional list and this funcction will auot convert it into 2D array using numpy 
    def __init__(self,i_state,g_state):
        self.rows=3
        self.cols=3
        self.initial_state=(np.array(i_state)).reshape(self.rows,self.cols)
        self.goal_state=(np.array(g_state)).reshape(self.rows,self.cols)
    
    def print(self):
        print(self.initial_state)
        print(self.goal_state)


    def isGoal(self,arr):
        flag=True
        for i in range(0,self.cols):
            for j in range(0,self.cols):
                if ( not (arr[i,j]==self.goal_state[i,j]) ):
                    flag=False
                    break
        return flag

    def getMoves(self,arr):
        #here bti stands for Balnk tile Index
        bti=self.get_blank_index(arr)  #returns as a tuple (row,col)
        moves=[]
        #checking left move
        if bti[1]>0: 
            moves.append( (bti[0],bti[1]-1) )  #col -1 while row remain same
        #checking right move
        if bti[1]<(self.cols-1):  
            moves.append( (bti[0],bti[1]+1) )  #row +1 while row remain same
        #checking up move
        if bti[0]>0:
            moves.append( (bti[0]-1,bti[1]) )  #row -1 while col remain same
        #checking down move
        if bti[0]<(self.rows-1):  
            moves.append( (bti[0]+1,bti[1]) )  #row +1 while col remain same
        return moves

    #returns the index of blank tile as a tuple
    def get_blank_index(self,arr):
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                if arr[i,j]==-1:
                    return (i,j)

    def printPaths(self,depth=float('inf')):
        #enque root puzzle board in queue
        queue=q()
        level_queue=q()
        current_level=0
        queue.enque([self.initial_state,0]) #inserting a list of form [node , depth]
        #printing initial level which is 0
        print("\t\t\t\t\tCurrent Level {0}".format(current_level))
        while(not queue.isEmpty() and current_level<=depth):
            current_state=queue.deque()  # it will return list of form  [node , depth]
            #Checking if current state level is greater than our current_level
            if(current_state[1]>current_level):
                current_level=current_level+1
                print("\t\t\t\t\tCurrent Level {0}".format(current_level))

            #printing Current Node
            print(current_state[0])

            if(self.isGoal(current_state[0])):
                return 
            else:
                blank_index=self.get_blank_index(current_state[0])
                moves=self.getMoves(current_state[0])
                len(moves)
                for move in moves:
                    #swaps the blank tile to available move and retuens the new array
                    new_state=self.swap(current_state[0],blank_index,move)
                    queue.enque([new_state,current_state[1]+1])

    def solvePuzzle(self):
        #enque root puzzle board in queue
        pqueue=PQ()
        current_level=0
        visited=[]
        visited.append(self.initial_state)
        #getHeuristic(arr,gn):
        priority=self.getHeuristic(self.initial_state,0)
        pqueue.enque([self.initial_state,0],priority) #inserting a list of form [node , depth] and priority
        #printing initial level which is 0
        print("\t\t\t\t\tCurrent Level {0}".format(current_level))
        while(not pqueue.isEmpty() ):
            # deque will return a Node Object defined in PQ whose value property specifies a list of form [numpy_array,depth] in this case 
            current_state=pqueue.deque().value  
            #Checking if current state level is greater than our current_level
            if(current_state[1]>current_level):
                current_level=current_level+1
                print("\t\t\t\t\tCurrent Level {0}".format(current_level))
            #printing Current Node
            print(current_state[0])
            #input("........")

            if(self.isGoal(current_state[0])):
                return 
            else:
                blank_index=self.get_blank_index(current_state[0])
                moves=self.getMoves(current_state[0])
                #local_list=[]
                for move in moves:
                    #swaps the blank tile to available move and retuens the new array
                    new_state=self.swap(current_state[0],blank_index,move)               
                    if (not self.isFound(new_state,visited) ):
                        priority=self.getHeuristic(new_state,current_state[1]+1) #here current_state[1]+1 specifies depth of new node
                        #min_arr_priority=self.getHeuristic(minarray,current_state[1]+1)
                        pqueue.enque([new_state,current_state[1]+1],priority)
                        visited.append(new_state)


    def isFound(self,arr,arrList):
        for array in arrList:
            # ussing numpy function numpy.array_equal(a1, a2)
            if(np.array_equal(array,arr)):
                return True
        return False

    """
    1)input :
        *)arr = takes a two dimensioanal numpy array
        *)f_index = indicates a tuple or a list of form (row,col)
        *)s_index = indicates a tuple or a list of form (row,col)
    2)functionality :
        *)this function will swap the the values on given idexes
    3)returns :
        *)return a 2D numpy array with values swapped on given indexes
    """
    def swap(self,arr,f_index,s_index):
        # Python provides short hand property for swapping variables e.g  a,b=b,a
        temp_arr=arr.copy()
        temp_arr[f_index[0],f_index[1]],temp_arr[s_index[0],s_index[1]]=temp_arr[s_index[0],s_index[1]],temp_arr[f_index[0],f_index[1]]
        return temp_arr


    """
    1)input :
        *)arr = takes a two dimensioanal numpy array
        *)as heuristic formula is f(n)=g(n)+h(n)  so here gn specifies g(n)
    2)functionality :
        *)this function will count no of misplace tiles ie h(n)
    3)returns :
        *)returns g(n)+h(n)
    """
    def getHeuristic(self,arr,gn):
        misplace_tile=0
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                if arr[i,j]!=self.goal_state[i,j]:
                    misplace_tile=misplace_tile+1
        return misplace_tile+gn

        


        
    