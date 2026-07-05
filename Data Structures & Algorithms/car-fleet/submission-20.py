class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        test_map = {position[i]:speed[i] for i in range(len(position))}
        sorted_positions = sorted(position)
        for i in range(len(sorted_positions) - 1, -1, -1):
            #print(f"{sorted_positions[i]} + {stack}")
            if not stack:
                stack.append([sorted_positions[i], test_map[sorted_positions[i]]])
                continue
            time_left_car1 = (target - sorted_positions[i])/test_map[sorted_positions[i]]
            time_left_car2 = (target - stack[-1][0])/stack[-1][1]
            print(f"{time_left_car1} + {time_left_car2}")
            #print(f"{stack} + {pos} + {fleet}")
            if time_left_car1 > time_left_car2:
                stack.append([sorted_positions[i], test_map[sorted_positions[i]]])
        return len(stack)

