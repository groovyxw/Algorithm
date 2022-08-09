from typing import List
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited=[[0 for x in range(len(maze[0]))] for y in range(len(maze))]
        # print(visited)
        dirs = [[0,1], [0,-1],[-1,0],[1,0]]
        queue = deque([start])
        visited[start[0]][start[1]] = 1
        while queue:
            point = queue.popleft()
            
            if point[0] == destination[0] and point[1] == destination[1]:
                return True
            
            for dir in dirs:
                cur_x, cur_y = point[0] + dir[0], point[1] + dir[1]
                while 0<=cur_x<len(maze) and 0<= cur_y < len(maze[0]) and maze[cur_x][cur_y] == 0:
                    cur_x += dir[0]
                    cur_y += dir[1]
                    
                cur_x -= dir[0]
                cur_y -= dir[1]
                if visited[cur_x][cur_y] == 0:
                    queue.append([cur_x, cur_y])
                    visited[cur_x][cur_y] = 1
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