class Solution:
    def __init__(self):
        self.memoization={}
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [expression]
        if expression in self.memoization:
            return self.memoization[expression]
        temp=[]
        for i in range(len(expression)):
            if expression[i] in "*-+":
                for x in self.diffWaysToCompute(expression[:i]):
                    for y in self.diffWaysToCompute(expression[i+1:]):
                        temp.append(str(eval(x+expression[i]+y)))
        self.memoization[expression]=temp
        return temp