class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        score = 0
        for op in operations:
            if op == "+" and records:
                last = records.pop()
                second = records.pop()
                records.append(second)
                records.append(last)
                records.append(second+last)
            elif op == 'D' and records:
                last = records.pop()
                records.append(last)
                records.append(last*2)
            elif op == 'C' and records:
                records.pop()
            else:
                records.append(int(op))
        total = 0
        print(records)
        for record in records:
            total+=record
        return total

        