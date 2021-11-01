class Queue():

    def __init__(self,iterable=[]):
            if(iterable is not None):
                self.__arr=list(iterable)
            else:
                self.__arr=[]
    #overriding stack methods
    def enque(self,item):
        self.__arr.append(item)
    
    def deque(self):
        if(len(self.__arr)>0):
            value=self.__arr[0]
            del(self.__arr[0])
            return value
        else:
            raise Exception("Empty Queue")

    def size(self):
        return len(self.__arr) 

    def front(self):
        if(len(self.__arr)>0):  #if not empty
            return self.__arr[0]
        else:
            raise Exception("Empty Queue")

    def isEmpty(self):
        if(len(self.__arr)==0):
            return True
        else:
            return False


"""

def main():
    obj=Queue()
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    print(obj.dequeue())
    print(obj.dequeue())
    print(obj.dequeue())
    
#calling main funtion
main()

"""