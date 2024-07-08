class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(graph, pos, dest, weights, visited):
            nonlocal answer
            visited.add(pos)

            if pos == dest:
                answer = 1
                for val in weights:
                    answer *= val
                return answer

            for next_pos, pos_w in graph[pos]:
                if next_pos not in visited:
                    weights.append(pos_w)
                    dfs(graph, next_pos, dest, weights, visited)
                    weights.pop()


        graph = defaultdict(list)
        answers = []

        for (x, y), val in zip(equations, values):
            graph[x].append([y, val])
            graph[y].append([x, 1/val])

        for x, y in queries:
            if x not in graph or y not in graph:
                answers.append(-1.0)
                continue
            answer = -1.0
            dfs(graph, x, y, [], set())
            answers.append(answer)

        return answers
