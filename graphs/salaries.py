from collections import defaultdict

employees = int(input())
employees_graph = defaultdict(list)
salaries = employees * 1


for manager in range(employees):
    relations = [x for x in input()]
