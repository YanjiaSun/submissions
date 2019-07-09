_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        paths, results = [[0]], []
        while paths:
            new_paths = []
            for path in paths:
                for next_node in graph[path[-1]]:
                    destination = results if next_node == len(graph) - 1 else new_paths
                    destination.append(path[:] + [next_node])
            paths = new_paths
        return results