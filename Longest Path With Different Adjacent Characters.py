from collections import defaultdict

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        tree = defaultdict(list)
        for child, par in enumerate(parent):
            if par != -1:
                tree[par].append(child)
        self.max_path = 0
        def dfs(node):
            if node not in tree:
                return 1
            max_len1, max_len2 = 0, 0
            for child in tree[node]:
                child_len = dfs(child)
                if s[child] != s[node]:
                    if child_len > max_len1:
                        max_len2 = max_len1
                        max_len1 = child_len
                    elif child_len > max_len2:
                        max_len2 = child_len
            self.max_path = max(self.max_path, max_len1 + max_len2 + 1)
            return max_len1 + 1
        if len(parent) == 1:
            return 1
        dfs(0)
        return self.max_path
