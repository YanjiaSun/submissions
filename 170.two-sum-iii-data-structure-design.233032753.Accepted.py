'''
Design and implement a TwoSum class. It should support the following operations: add and find.
add – Add the number to an internal data structure.
find – Find if there exists any pair of numbers which sum is equal to the value.
For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
'''


class TwoSum(object):
    def __init__(self):
        self.value_count = {}

    def add(self, number):
        if number in self.value_count:
            self.value_count[number] += 1
        else:
            self.value_count[number] = 1

    def find(self, value):
        for val in self.value_count:
            diff = value - val
            if diff in self.value_count and (diff != val or self.value_count[val] > 1):
                return True
        return False
