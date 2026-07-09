class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # def distance(x1,y1):
        #     return (((x1)**2 + (y1)**2)**0.5)
        # out = []
        # min_d = distance(points[0][0],points[0][1])
        # for i in points:
        #     dist = distance(i[0],i[1])
        #     print(dist)
        #     if dist == min_d:
        #         out.append(i)
        #     elif dist < min_d:
        #         min_d = dist
        #         out = []
        #         out.append(i)

        # return out
        points.sort(key=lambda p: p[0]**2 + p[1]**2)  # Sort by squared distance
        return points[:k]