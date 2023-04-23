class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = p.parent
        while q:
            if q in p_ancestors:
                return q
            q = q.parent
        return None
