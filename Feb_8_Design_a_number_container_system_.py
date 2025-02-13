from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.number_container, self.index_container = {}, {}
        

    def change(self, index: int, number: int) -> None:
        # print(index, number, self.number_container)
        if index not in self.index_container:
            self.index_container[index] = number
        else:
            prev_num = self.index_container[index]
            self.index_container[index] = number
            self.number_container[prev_num].remove(index)
            if len(self.number_container[prev_num]) == 0:
                del self.number_container[prev_num]

        if number in self.number_container:
            self.number_container[number].add(index)
        else:
            self.number_container[number] = SortedSet([index])
        

    def find(self, number: int) -> int:
        if number in self.number_container:
            # print(self.number_container)
            return self.number_container[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)