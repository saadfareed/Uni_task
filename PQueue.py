class Node():
    def __init__(self,value=-1,priority=0):
        self.priority=priority  #less priority
        self.value=value  #default value is -1
    
    def __str__(self):
        return "(value={0},Priority={1})".format(self.value,self.priority)


#considers 0 as high proiority.
class PriorityQueue():

    def __init__(self):
        self.iterable=[]
    
    def enque(self,value,priority):
        newNode=Node(value,priority)
        if(self.iterable==[]):
            self.iterable.append(newNode)
        else:
            insert_flag=False
            for i in range(0,len(self.iterable)):
                if(newNode.priority<self.iterable[i].priority):
                    self.iterable.insert(i,newNode)
                    insert_flag=True
                    break
            #now checking if insertion has taken place or not
            if(insert_flag==False):
                self.iterable.append(newNode)


    def deque(self):
            if(len(self.iterable)>0):
                value=self.iterable[0]
                del(self.iterable[0])
                return value
            else:
                raise Exception("Empty Queue")

    def size(self):
        return len(self.iterable)
    
    def isEmpty(self):
        if len(self.iterable)==0:
            return True
        else:
            return False

    def getQueue(self):
        return self.iterable

