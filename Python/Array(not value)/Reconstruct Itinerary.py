class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # we need a dictionary to store 图的边， then sort dict, when key is the same, sort the items in the list
        # a is departure, b is arrival
        # pop the last one of the list, which has the smaller lexical order, and remove it from the dict list
        target = collections.defaultdict(list)
        
        for a,b in tickets: #sort based on FROM, and in reversed order
            target[a].append(b)
            
        for k in target:
            target[k].sort() # sort TO according to lexical order

        res=[]
        stack=['JFK']
        while stack:
            while target[stack[-1]]:
                stack.append(target[stack[-1]].pop(0)) # the smallest lexical order
            res.append(stack.pop()) # the biggest lexical order
            
        return res[::-1] # reverse order
        
'''
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
'''