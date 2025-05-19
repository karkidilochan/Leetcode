class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        times = [(target - position[i]) / speed[i] for i in range(len(position))]

        pos_times = list(zip(position, times))

        sorted_pos_times = sorted(pos_times, key=lambda x: x[0], reverse=True)

        for post in sorted_pos_times:

            if stack and stack[-1] >= post[1]:
                continue
            else:
                stack.append(post[1])

        return len(stack)


"""
need to look at cars from descending order of position,
faster cars with lesser time catch up to slower cars with greater time
in descending order, if time of car greater than the car in front of it, increase fleet count
can use stack to keep track of the time of the car in front of it
O(n) time complexity, O(n) space complexity
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        times = [(target - position[i]) / speed[i] for i in range(len(position))]

        pos_times = list(zip(position, times))

        sorted_pos_times = sorted(pos_times, key=lambda x: x[0], reverse=True)

        max_time = None
        car_fleet = 0
        for post in sorted_pos_times:
            if max_time and max_time >= post[1]:
                continue
            else:
                max_time = post[1]
                car_fleet += 1
        return car_fleet
