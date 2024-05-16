class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_water = capacity
        for i in range(len(plants)):
            if current_water >= plants[i]:
                current_water -= plants[i]
                steps += 1
            else:
                steps += (2 * i) + 1  
                current_water = capacity - plants[i]
        return steps