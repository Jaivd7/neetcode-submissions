class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {"2":['a','b','c'], "3":['d','e','f'], "4":['g','h','i'], "5":['j','k','l',],
                "6":['m','n','o'], "7":['p','q','r','s'], "8":['t','u','v'], "9":['w','x','y','z']}
        out = []
        curr = []
        def dfs(index):
            # Base Case
            if index == len(digits):
                if curr:
                    out.append(''.join(curr))
                return 
            
            digit = digits[index]
            #print(digit)
            for letter in hmap[digit]:
                curr.append(letter)
                dfs(index+1)
                curr.pop()
        dfs(0)
        return out