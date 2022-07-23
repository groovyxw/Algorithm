class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        row, col = len(maze), len(maze[0])
        visited = [start]
        while visited:
            x, y = visited.pop()
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x_, y_ = x, y
                while 0 <= x_ < row and 0 <= y_ < col and maze[x_][y_] != 1:
                    x_ += dx; y_ += dy
                x_ -= dx; y_ -= dy
                if [x_, y_] == destination:
                    return True
                elif maze[x_][y_] == 0:
                    maze[x_][y_] = 2
                    visited.append([x_,y_])
                else:
                    continue
        return False

def main():
    sol = Solution()
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    destination = [4,4]
    print(f'\nInput: maze={maze}, start = {start}, destination={destination}\nOutput: {sol.hasPath(maze, start, destination)}')

    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start = [0,4]
    destination = [3,2]
    print(f'\nInput: maze={maze}, start = {start}, destination={destination}\nOutput: {sol.hasPath(maze, start, destination)}')

    maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
    start = [4,3]
    destination = [0,1]
    print(f'\nInput: maze={maze}, start = {start}, destination={destination}\nOutput: {sol.hasPath(maze, start, destination)}')

if __name__ == '__main__':
    main()
