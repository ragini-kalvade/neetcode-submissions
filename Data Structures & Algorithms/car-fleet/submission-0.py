class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #creates a list of tuple(position,speed) sorted by position -- from closest to target to farthest
        cars = sorted(zip(position,speed),reverse=True)

        fleets = 0
        slowest_time_ahead = 0
        
        for pos,speed in cars:
            time_to_target = (target - pos)/speed

            if time_to_target > slowest_time_ahead:
                fleets+=1
                slowest_time_ahead = time_to_target
            
        return fleets