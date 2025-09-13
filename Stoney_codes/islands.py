import collections

def numIslands(grid):
    if not grid:
        return 0
    rows,cols=len(grid),len(grid[0])
    # row =>4 and cols=>5
    visit=set()
    # visit  is used for a set to track which cells we’ve already visited (to avoid re-processing).
    # islandCount → counts how many islands we’ve found.
    islandCount=0
    def bfs(r,c):
        # Define bfs(r,c) → explores all connected land starting from cell (r,c).
        # Initialize a deque q.
        # Mark (r,c) as visited
        # Add (r,c) to the queue.
        
        q=collections.deque()
        visit.add((r,c))
        q.append((r,c))
        while q:
            row,col=q.popleft()
            # While the queue is not empty → take one cell (row, col) from the front.       
            directions=[[1,0],[0,-1],[-1,0],[0,1]]
            for dr,dc in directions:
                r,c=row+dr,col+dc
                if(r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit):
                    q.append((r,c))
                    visit.add((r,c  ))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1"  and (r,c) not in visit:
                bfs(r,c)
                islandCount+=1
    return islandCount
 

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))