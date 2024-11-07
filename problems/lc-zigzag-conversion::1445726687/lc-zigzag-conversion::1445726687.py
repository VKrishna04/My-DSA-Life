class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        line = [''] * numRows
        cycle_length = (numRows - 1) * 2
        for i in range(len(s)):
            cycle_pos = i % cycle_length
            if cycle_pos < numRows:
                line[cycle_pos] += s[i]
            else:
                line[cycle_length - cycle_pos] += s[i]
            
        return "".join(line)