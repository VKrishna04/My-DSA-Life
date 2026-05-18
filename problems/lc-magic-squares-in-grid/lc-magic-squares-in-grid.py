class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            print("0")
        def is_magic(mag):
            flatmag = [item for row in mag for item in row]
            flatmag = [item for item in flatmag if 1 <= item <= 9]
            if len(flatmag) != 9 or set(flatmag) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
            return (sum(mag[0]) == sum(mag[1]) == sum(mag[2]) == 
                    sum(mag[i][0] for i in range(3)) == 
                    sum(mag[i][1] for i in range(3)) == 
                    sum(mag[i][2] for i in range(3)) == 
                    mag[0][0] + mag[1][1] + mag[2][2] == 
                    mag[0][2] + mag[1][1] + mag[2][0])
        
        rowlen = len(grid)
        collen = len(grid[0])
        magic_count = 0
        
        for row in range(rowlen - 2):
            for col in range(collen - 2):
                mag = [grid[row+i][col:col+3] for i in range(3)]
                if is_magic(mag):
                    magic_count += 1
        
        return magic_count