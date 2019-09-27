#   O(N^2)    O(N)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

'''
Sort people in the descending order by height.

Among the guys of the same height, in the ascending order by k-values.
Take guys one by one, and place them in the output array at the indexes equal to their k-values.

Return output array.
'''