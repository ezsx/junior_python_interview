class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        print(path.split("/"))
        for elem in path.split("/"):
            if stack and elem == "..":
                stack.pop()
            elif elem not in [".", "", ".."]:
                stack.append(elem)

        return "/" + "/".join(stack)

path = "/a/./b/../../c/"
print(Solution().simplifyPath(path))
