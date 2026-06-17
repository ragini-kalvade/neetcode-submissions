class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        score = 0
        for op in operations:
            if op == "+" and records:
                records.append(records[-2]+records[-1])
            elif op == 'D' and records:
                records.append(records[-1]*2)
            elif op == 'C' and records:
                records.pop()
            else:
                records.append(int(op))
        total = 0
        for record in records:
            total+=record
        return total

        