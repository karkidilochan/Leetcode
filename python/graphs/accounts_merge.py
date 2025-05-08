class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict

        adj_list = defaultdict(list)
        en_map = {}

        for account in accounts:
            emails = account[1:]
            for i in range(len(emails)):
                adj_list[emails[i]] = adj_list[emails[i]] + emails[:i] + emails[i + 1 :]
                en_map[emails[i]] = account[0]
        visited = set()
        result = []

        def dfs(email):
            visited.add(email)
            path.append(email)
            for edge in adj_list[email]:
                if edge not in visited:
                    dfs(edge)
            return

        for node in adj_list.keys():
            path = []
            if node not in visited:
                dfs(node)
                result.append([en_map[node]] + sorted(path[:]))

        return result
