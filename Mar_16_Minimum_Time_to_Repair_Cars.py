"""
Approach:
    This problem can be solved using binary search. We can use binary search to find the minimum time required to repair all cars.
    The key idea is to calculate how many cars can be repaired in a given time based on the ranks of the mechanics.
    For each mechanic, the number of cars they can repair in time `t` is given by the formula: `floor(sqrt(t / rank))`.
    We can sum this up for all mechanics and check if it meets or exceeds the number of cars to be repaired.
Time Complexity:
    O(n log m) where n is the number of mechanics and m is the maximum time required to repair all cars.
# Space Complexity:
    O(1) since we are not using any extra space.
"""

def repairCars(ranks, cars: int) -> int:
    left = 1
    right = min(ranks) * cars * cars 
    
    def can_repair_all(time):
        total_cars_repaired = 0
        for rank in ranks:
            cars_repaired = int((time / rank) ** 0.5)
            total_cars_repaired += cars_repaired
            if total_cars_repaired >= cars:
                return True
        return False
    
    while left < right:
        mid = (left + right) // 2
        if can_repair_all(mid):
            right = mid
        else:
            left = mid + 1
            
    return left
    

# Example usage
print(repairCars([4,2,3], 10))  # Expected output: 36
print(repairCars([5,1,8], 6))   # Expected output: 16