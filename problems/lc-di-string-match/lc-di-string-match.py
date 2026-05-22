class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        output = []
        d = len(s)
        i = 0
        for char in s:
            if char == "D":
                output.append(d)
                d -= 1
                continue
            output.append(i)
            i += 1
        # output.append(i)
        output.append(d)
        return output