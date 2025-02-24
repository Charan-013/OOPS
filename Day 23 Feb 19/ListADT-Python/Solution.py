class ArrayListADT():
    def __init__(self):
        self.data = []
        self.size = len(self.data)
        self.capacity = 10
    
    def add(self,e):
        self.data.append(e)
        self.size = len(self.data)
        # self.rearrange_list()
        return True
    
    def add_at(self,i,e):
        new = []
        first = self.data[:i]
        middle = [e]
        last = self.data[i:]
        new = first + middle + last
        self.data = new
        self.size = len(self.data)
        # return self.data

    def size_(self):
        return self.size
    
    def add_all(self,c):
        self.data = self.data + c
        self.rearrange_list()
        return True
    
    def add_all_at(self,i,c):
        new = []
        first = self.data[:i]
        middle = list(c)
        last = self.data[i:]
        new = first + middle + last
        self.data = new
        self.size = len(self.data)
        # self.rearrange_list()
        return True
    
    def contains(self,e):
        if e in self.data:
            return True
        return False
    
    def get(self,i):
        return self.data[i]
    
    def ensure_capacity(self,capacity):
        if len(self.data) != capacity and len(self.data) < capacity:
            self.add_all_at(self.size,[None]* (capacity - len(self.data)))
        self.capacity = capacity
    
    def clear(self):
        self.data = []
        self.size = len(self.data)
    
    def index_of(self,obj):
        for i in range(self.size):
            if self.data[i] == obj:
                return i
        return -1
    
    def last_index_of(self,obj):
        for j in range(self.size-1,-1,-1):
            if self.data[j] == obj:
                return j
        return -1
    
    def is_empty(self):
        return len(self.data) == 0
    
    def remove_at(self,index):
        first = self.data[:index]
        middle = self.data[index]
        last = self.data[index+1:]
        self.data = first + last
        self.size = len(self.data)
        return middle

    def remove(self,obj):
        for i in range(self.size):
            if self.data[i] == obj:
                self.data = self.data[:i] + self.data[i+1:]
                self.size = len(self.data)
                return True
        return False

    def set(self,index,ele):
        old = self.data[index]
        self.data[index] = ele      
        return old
    
    def trim_to_size(self):
        self.rearrange_list()
        self.data = self.data[:self.size]
        self.capacity = self.size
        # print(self.data)

    def rearrange_list(self):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i] == None and self.data[j] != None and i < j:
                    self.data[i],self.data[j] = self.data[j],self.data[i]

    def __str__(self):
        return f"{self.data}"