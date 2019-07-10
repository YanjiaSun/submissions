


class Solution(object):
    def removeInvalidParentheses(self, s):
        if not s:
            return [""]

        def isValid(s):
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return (count == 0)
        queue, result = [s], []
        visited = set()
        visited.add(s)
        level = False
        while queue:
            new_str = queue.pop(0)
            if isValid(new_str):
                result.append(new_str)
                level = True
            if level:
                continue
            for index in range(len(new_str)):
                if not (new_str[index] == "(" or new_str[index] == ")"):
                    continue
                partition_str = new_str[0:index] + new_str[index + 1:]
                if partition_str not in visited:
                    queue.append(partition_str)
                    visited.add(partition_str)
        return result
