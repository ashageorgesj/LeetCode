class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append((point,point[0]**2 +point[1]**2))
        values = sorted(distances,key = lambda item:item[1])
        answer = [values[i][0] for i in range(0,K) if i < len(values)]
        return answer