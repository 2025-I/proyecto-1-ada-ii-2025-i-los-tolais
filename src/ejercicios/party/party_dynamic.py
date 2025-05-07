def solve_party_dynamic(lines):
    index = 1
    results = []
    num_problems = int(lines[0])

    for _ in range(num_problems):
        m = int(lines[index])
        matrix = [list(map(int, lines[index + i + 1].split())) for i in range(m)]
        values = list(map(int, lines[index + m + 1].split()))
        index += m + 2

        tree, root = build_tree_and_root(matrix)
        invited, total = dp(tree, values, root)
        result_line = " ".join(str(i) for i in invited) + f" {total}"
        results.append(result_line)

    return results


def build_tree_and_root(matrix):
    n = len(matrix)
    tree = {i: [] for i in range(n)}
    in_degree = [0] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                tree[i].append(j)
                in_degree[j] += 1

    root = in_degree.index(0)
    return tree, root


def dp(tree, values, root):
    def dfs(u):
        include_u = values[u]
        exclude_u = 0
        include_list = [0] * len(values)
        exclude_list = [0] * len(values)

        include_list[u] = 1

        for v in tree[u]:
            excl_v_val, excl_v_list = dfs(v)
            exclude_u += max(excl_v_val)
            exclude_list = [max(a, b) for a, b in zip(exclude_list, excl_v_list)]

            for vv in tree[v]:
                inc_vv_val, inc_vv_list = dfs(vv)
                include_u += inc_vv_val
                include_list = [max(a, b) for a, b in zip(include_list, inc_vv_list)]

        if include_u > exclude_u:
            return include_u, include_list
        else:
            return exclude_u, exclude_list

    total, invited = dfs(root)
    return invited, total
