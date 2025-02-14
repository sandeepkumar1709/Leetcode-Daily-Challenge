class ProductOfNumbers:

    def __init__(self):
        self.product = 1
        self.product_array = []
        self.index = -1
        

    def add(self, num: int) -> None:
        if num == 0:
            self.product = 1
            self.index = 1
            self.product_array.append(0)
        else:
            self.product *= num
            if self.index != -1:
                self.index+=1
            self.product_array.append(self.product)

        

    def getProduct(self, k: int) -> int:
        if self.index != -1 and k >= self.index:
            return 0
        if len(self.product_array) == k:
            return self.product
        k +=1
        return self.product // max(self.product_array[-k],1)
 
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


#Time Complexity: O(1) for add and getProduct
#Space Complexity: O(n) for add and getProduct