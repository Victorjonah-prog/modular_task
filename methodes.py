# custom methodes

class Array:

    data = []


    def append(self,value):
        self.data += [value]
        return self.data


    def remove(self, value):  
        new_number = []
        for number in self.data:
            if number != value:
                new_number += [number] 
        self.data = new_number  
        return self.data

    def insert(self,index,value):
        new_list1 = self.data[:index]
        new_list2 = self.data[index:]
        self.data = new_list1 + [value] + new_list2
        return self.data

    def pop(self): 
           
        del self.data[-1]   
        return self.data 
        '''
        i = 0
        for element in self.data:
            if i == index:
                del self.data[i]
            else:
                pass
            i +=1  
        '''
                     
        


