class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        class mathF:

            def add(self, y: int, x: int) -> int:
                return x + y

            def mul(self, y: int, x: int) -> int:
                return x * y

            def sub(self, y: int, x: int) -> int:
                return x - y

            def div(self, y: int, x: int) -> int:
                return int(x / y)

        mf = mathF()
        # working list
        wl = []

        while len(tokens) > 0:
            # active token
            at = tokens.pop(0)
            print(at)
            if at.isnumeric():
                print(wl)
                wl.append(int(at))
                print(wl)
                continue
            
            
            if at == '+':
                wl.append(mf.add(wl.pop(), wl.pop()))
            if at == '*':
                wl.append(mf.mul(wl.pop(), wl.pop()))
            if at == '-':
                wl.append(mf.sub(wl.pop(), wl.pop()))
            if at == '/':
                wl.append(mf.div(wl.pop(), wl.pop()))
            
            print(wl)
            
        
        return wl[0]

# testing the code

tokens = ["2","1","+","3","*"]
sol = Solution()
print(sol.evalRPN(tokens))