class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = []
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        stack.append((sr,sc))
        startColor = image[sr][sc]
        visited = set()
        while len(stack) > 0:
            current = stack.pop()
            visited.add(current)
            image[current[0]][current[1]] = newColor
            for direction in directions:
                new = (current[0] + direction[0],current[1] + direction[1])
                if new not in visited and 0 <= new[0] < len(image) and 0 <= new[1] < len(image[0]):
                    if image[new[0]][new[1]] == startColor:
                        stack.append((new[0],new[1]))
        return image
