from abc import ABC, abstractmethod

class ListADT(ABC):
    
    @abstractmethod
    def add(self, e: int) -> bool:
        pass
    
    @abstractmethod
    def add_at(self, i: int, e: int) -> None:
        pass
    
    @abstractmethod
    def addAll(self, i: int, c) -> bool:
        pass
    
    @abstractmethod
    def clear(self) -> None:
        pass
    
    @abstractmethod
    def contains(self, e: int) -> bool:
        pass
    
    @abstractmethod
    def ensureCapacity(self, capacity: int) -> None:
        pass
    
    @abstractmethod
    def get(self, i: int) -> int:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class ArrayListADT(ListADT):
    def __init__(self):
        self.data = []
        self.size = len(self.data)
    
    def add(self,e):
        self.data.append(e)
        self.size = len(self.data)
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
    # def size(self):
    #     return len(self.data)
    
    def addAll(self,i,c):
        new = []
        first = self.data[:i]
        middle = list(c)
        last = self.data[i:]
        new = first + middle + last
        self.data = new
        self.size = len(self.data)
        return True
    
    def contains(self,e):
        if e in self.data:
            return True
        return False
    
    def get(self,i):
        return self.data[i]
    
    def ensureCapacity(self,capacity):
        self.addAll(self.size - 1,[""]* capacity)
    
    def clear(self):
        self.data = []
        self.size = len(self.data)
        
    def __str__(self):
        return f"{self.data}"
    
# def test_all_data_types():
#     # Test with Integer
#     int_list = ArrayListADT()
#     int_list.add(10)
#     int_list.add(1000000000000000)
#     int_list.add(-50)
#     print(f"Integer List: {int_list}")  # Expected: [10, 1000000000000000, -50]

#     # Test with String
#     str_list = ArrayListADT()
#     str_list.add("apple")
#     str_list.add("banana")
#     str_list.add("")  # Empty string
#     print(f"String List: {str_list}")  # Expected: ["apple", "banana", ""]

#     # Test with Float
#     float_list = ArrayListADT()
#     float_list.add(1.1)
#     float_list.add(3.1415926535)  # Pi value
#     float_list.add(0.0000001)  # Small float
#     print(f"Float List: {float_list}")  # Expected: [1.1, 3.1415926535, 0.0000001]

#     # Test with Boolean
#     bool_list = ArrayListADT()
#     bool_list.add(True)
#     bool_list.add(False)
#     bool_list.add(None)  # None as an edge case
#     print(f"Boolean List: {bool_list}")  # Expected: [True, False, None]

#     # Test with None (null-like case)
#     none_list = ArrayListADT()
#     none_list.add(None)  # Adding None explicitly
#     print(f"None List: {none_list}")  # Expected: [None]

#     # Test with Custom Objects
#     class CustomObject:
#         def __init__(self, name):
#             self.name = name
        
#         def __repr__(self):
#             return f"CustomObject({self.name})"
    
#     obj_list = ArrayListADT()
#     obj_list.add(CustomObject("object1"))
#     obj_list.add(CustomObject("object2"))
#     obj_list.add(CustomObject("object3"))
#     print(f"Object List: {obj_list}")  # Expected: [CustomObject(object1), CustomObject(object2), CustomObject(object3)]

#     # Test with List inside List (Nested Lists)
#     nested_list = ArrayListADT()
#     nested_list.add([1, 2, 3])  # Adding list as an element
#     nested_list.add([4, 5, 6])
#     print(f"Nested List: {nested_list}")  # Expected: [[1, 2, 3], [4, 5, 6]]

#     # Test with Dictionary inside List
#     dict_list = ArrayListADT()
#     dict_list.add({"key1": "value1", "key2": "value2"})
#     dict_list.add({"key3": "value3"})
#     print(f"Dictionary List: {dict_list}")  # Expected: [{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]

#     # Test Add At Method with Negative Index
#     mixed_list = ArrayListADT()
#     mixed_list.add("hello")
#     mixed_list.add(42)
#     mixed_list.add_at(-1, 3.14)  # Invalid negative index behavior needs to be tested
#     print(f"Mixed List with negative index: {mixed_list}")  # Expected: ["hello", 42, 3.14]

#     # Test Add All Method with Non-Standard Data Types
#     mixed_list.addAll(1, ["new_item", 99.9, {"key": "value"}])
#     print(f"Mixed List after Add All: {mixed_list}")  # Expected: ["hello", "new_item", 99.9, {"key": "value"}, 42, 3.14]

#     # Test Edge Case: Empty List (Initial Case)
#     empty_list = ArrayListADT()
#     print(f"Empty List: {empty_list}")  # Expected: []

#     # Test Add Method with Invalid Data Type (e.g., list of lists or unhashable types)
#     try:
#         empty_list.add([1, 2, 3])  # Adding a list inside the list
#         print(f"List after adding a list inside: {empty_list}")  # Expected: [ [1, 2, 3] ]
#     except Exception as e:
#         print(f"Error when adding a list: {e}")

#     # Test Get Method with Index out of range
#     try:
#         print(f"Get index 10: {empty_list.get(10)}")  # Should raise an IndexError or handle it gracefully
#     except Exception as e:
#         print(f"Error when getting index 10: {e}")

#     # Test Clear Method
#     empty_list.clear()
#     print(f"List after clear: {empty_list}")  # Expected: []

# # Running the tests
# test_all_data_types()