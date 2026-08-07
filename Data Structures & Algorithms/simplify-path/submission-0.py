class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            c = path[i]
            if c != '/':
                pathname = ""
                while i < len(path) and path[i] != '/':
                    pathname += path[i]
                    i +=1
                if pathname == "..":
                    if stack:
                        stack.pop()
                elif pathname == ".":
                    continue
                else:
                    stack.append(pathname)
            else:
                i +=1
        final = "/"
        if not stack:
            return final
        for p in range(len(stack)):
            if p == len(stack)-1:
                final = final + stack[p]
            else:
                final = final + stack[p] + "/"
        return final

                    