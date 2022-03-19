
class Node:
    def __init__(self, data) -> None:
        self.reference = None
        self.data = data

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    
    def add_begining(self, data):
        new = Node(data)
        new.reference = self.head
        self.head = new  
    
        
    def add_end(self, data):
        n = self.head
        if n:
            while n.reference:
                n=n.reference
            
            new = Node(data)
            new.reference = None
            n.reference = new
        else:
            self.add_begining(data)
    
    
    def display(self)->None:
        n = self.head
        if n:
            while n:
                if n.reference:
                    print(n, end='->')
                else:
                    print(n, '--->|||')
                n=n.reference
        else:
            print('Empty Linked list')
    
    
    def add_after(self, ref_data, new_data)->None:
        
        new = Node(new_data)
        if not self.head:
            print('Empty List')
            return
        elif self.head.data == ref_data:
            new.reference = self.head.reference
            self.head.reference = new
            return
        else:
            n=self.head
            while n:
                if n.data==ref_data: break
                else: pass
                n=n.reference 
            if n:
                new.reference = n.reference
                n.reference = new
            else:
                raise Exception('data error -> no such data found in linked list')
            return 
    
    
    def add_before(self, ref_data, new_data):
        new = Node(new_data)
        if not self.head:
            print('empty list')
        elif self.head.data == ref_data:
            new.reference = self.head
            self.head = new
        else:
            try:
                n= self.head
                while True:
                    if n.reference.data == ref_data:
                        break
                    n=n.reference
                
                new.reference = n.reference
                n.reference = new
            except:
                raise Exception('data error -> no such data found in linked list')


    def del_head(self):
        if self.head:
            self.head = self.head.reference
        else:
            raise Exception('Empty linked list to delete objets')

    
    def del_rear(self):
        if self.head:
            if self.head.reference:
                n = self.head
                while n.reference.reference:
                    n=n.reference
                
                n.reference = None
                    
            else:
                self.head = None
        else:
            raise Exception('Empty linked list to delete objets')
    
    def del_point(self, data): 
        if self.head is None:
            raise Exception('Empty linked list to delete objets')
        elif self.head.data == data:
            self.del_head()
        else:
            n = self.head
            found = False
            noto = False
            while n.reference.reference:
            
                if n.reference.data == data:
                    found = True
                    break
                n = n.reference
            else:
                noto = True
                n.reference = None
            
            
            if not found and not noto: 
                raise Exception('data error -> no such data found in linked list')
            else: 
                if noto: pass
                else:
                    n.reference=n.reference.reference
                
if __name__ == '__main__':
    pass
