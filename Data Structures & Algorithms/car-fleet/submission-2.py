class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((target - position[i], speed[i]))
        combined.sort(key=lambda x:x[0])
        out = []
        # [(3, 1), (6, 2), (9, 2), (10, 1)]
        # [3, 3, 4.5, 10]

        for i in combined:
            time = i[0]/i[1]
            # print(time, out)
            if not out:
                out.append(time)
            else:
                if out[-1] < time:
                    out.append(time)
        return len(out)