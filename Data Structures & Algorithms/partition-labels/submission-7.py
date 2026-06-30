class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s == "":
            return 0
        final_lengths = []
        start = deque([s[0]])
        length = 0 
        count = {}
        for i in s:
            if i not in count:
                count[i] = [0, 0]

            count[i][0] += 1
            count[i][1] += 1

        for i in s:
            if start == deque([]):
                final_lengths.append(length)
                length = 0
                start.append(i)
            length += 1
            if i != start[-1] and count[i][0] == count[i][1]:
                start.appendleft(i)
            count[i][1] -= 1
            if count[i][1] == 0:
                while count[start[-1]][1] == 0:
                    start.pop()
                    if not start:
                        break
        final_lengths.append(length)
        return final_lengths

