class Solution:
class Solution: 
    class Node:
        def __init__(self, name):
            self.name = name
            self.outgoing = {}

    def bfs(self, gf, gt):
        q = [(gf, 1)]
        visited = set([gf])
        while len(q) > 0:
            p, v = q.pop(0)
            if p.name == gt.name:
                return v
            for t, vt in p.outgoing.items():
                if t not in visited:
                    q.append((t, v * vt))
        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = {}

        for i, (f, t) in enumerate(equations):
            v = values[i]
            if f not in g:
                g[f] = self.Node(f)
            if t not in g:
                g[t] = self.Node(t)
            g[f].outgoing[g[t]] = v
            g[t].outgoing[g[f]] = 1.0 / v

        results = []
        for (f, t) in queries:
            gf = g.get(f)
            gt = g.get(t)
            if gf is None or gt is None:
                results.append(-1.0)
            else:
                v = self.bfs(gf, gt)
                results.append(v)

        return results