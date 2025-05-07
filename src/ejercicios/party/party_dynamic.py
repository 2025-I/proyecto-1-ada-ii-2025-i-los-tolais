def solve_party_dp(lines):
    index = 1
    results = []
    numproblems = int(lines[0])

    for  in range(num_problems):
        m = int(lines[index])
        matrix = [list(map(int, lines[index + i + 1].split())) for i in range(m)]
        values = list(map(int, lines[index + m + 1].split()))
        index += m + 2

        tree, root = build_tree_dp(matrix)
        dp = tree_dp(tree, values, root)
        invited = [0] * m
        recover_selected(tree, dp, root, False, invited)
        total = max(dp[root][0], dp[root][1])
        results.append(" ".join(map(str, invited)) + f" {total}")

    return results


def build_tree_dp(matrix):
    n = len(matrix)
    children = {i: [] for i in range(n)}
    indegree = [0] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                children[i].append(j)
                indegree[j] += 1

    root = indegree.index(0)
    return children, root


def tree_dp(tree, values, root):
    dp = {}

    def dfs(u):
        include = values[u]
        exclude = 0

        for v in tree[u]:
            dfs(v)
            exclude += max(dp[v][0], dp[v][1])
            include += dp[v][0]

        dp[u] = (exclude, include)

    dfs(root)
    return dp


def recover_selected(tree, dp, node, parent_included, invited):
    exclude, include = dp[node]
    if parent_included:
        invited[node] = 0
        for child in tree[node]:
            recover_selected(tree, dp, child, False, invited)
    else:
        if include > exclude:
            invited[node] = 1
            for child in tree[node]:
                recover_selected(tree, dp, child, True, invited)
        else:
            invited[node] = 0
            for child in tree[node]:
                recover_selected(tree, dp, child, False, invited)
