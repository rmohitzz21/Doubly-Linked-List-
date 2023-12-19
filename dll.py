class node:
    def __init__(self,prev = None,item = None ,next = None):
        self.prev = prev
        self.item = item
        self.next = next
class Dll:
    def __init__(self,start = None):
        self.start = start
    
    def isEmpty(self): # if list is empty 
        return  self.start == None

    def insert_at_start(self,data):  
          new = node(None, data,self.start)  
          if not self.isEmpty():
                self.start.prev = new
          self.start = new
        

    def insert_at_last(self,data):
        temp = self.start
        if self.start != None:
            while temp.next != None:
                temp=temp.next
        
        new = node(temp,data,None)
        if temp==None:
            self.start=new
        else:
            temp.next= new
        
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            new = node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = new
            temp.next = new

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end = ' ')
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev is None
    
    def delete_last(self):
        if self.start is None:              #if list empty 
            pass
        elif self.start.next is None:     # only one node aval
            self.start= None
        else:
            temp=self.start
            while temp.next is not None:    #till the last node next is none 
                temp = temp.next            #increment node
            temp.prev.next=None             #

    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:   
                        temp.next.prev = temp.prev
                    if temp.prev is not None:    # node is avl before temp
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next

    def __iter__(self):
        return DllIterator(self.start)

class DllIterator:
    def __init__(self,start):  #ref to first node
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if  self.current==None:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

my_list = Dll()
my_list.insert_at_start(10)
my_list.insert_at_start(20)
my_list.insert_at_last(25)
my_list.insert_at_last(55)
my_list.insert_at_last(45)
my_list.insert_after(my_list.search(20),34)

my_list.delete_first()
my_list.delete_item(55)
# my_list.print_list()

for x in my_list:
    print(x , end=' ')

       

    