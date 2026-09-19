class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for opr in operations:
            match opr:
                case 'C':
                    scores.pop()
                case '+':
                    scores.append(scores[-1] + scores[-2])
                case 'D':
                    scores.append(2*scores[-1])
                case _:
                    scores.append(int(opr))
        return sum(scores)