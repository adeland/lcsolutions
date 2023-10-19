    def evalRPN(self, tokens: List[str]) -> int:
      
        operators = "+-/*"
        stack = []

        for i in tokens:
            if i in operators:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    value = b + a 
                    stack.append(value)
                elif i == "-":
                    value = b - a
                    stack.append(value)
                elif i == "/":
                    value = int(b / a)
                    stack.append(value)
                elif i == "*":
                    value = b * a
                    stack.append(value)
            else:
                stack.append(int(i))
    
        return stack[0]
