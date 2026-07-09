class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        for i in range(len(s)):
            if s[i] == '#':
                recorded_i = i
                break
        out = []
        copy = recorded_i
        recorded_i +=1
        i = 0
        while i<copy:
            if s[i] != ',':
                x = i
                while(s[x] != ","):
                    x +=1
                length = int(s[i:x])
                print(length, s[recorded_i:recorded_i+length])
                out.append(s[recorded_i:recorded_i+length])
                recorded_i = recorded_i+length
                i=x+1
        return out
