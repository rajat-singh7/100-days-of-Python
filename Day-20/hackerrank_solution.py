#TODAY-21|06|2026
#PROBLEM NO.01
#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
import sys
from io import StringIO
test_input = """5
Harry
37.2
Berry
37.2
Tina
41
Akriti
41
Harsh
39
"""
#sys = System
#stdin = Standard Input
sys.stdin = StringIO(test_input)
if __name__ == '__main__':
    name_list = []
    score_list = []
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        records.append([name,score])
        name_list.append(name)
        score_list.append(score)
    score_list = list(set(score_list))
    score_list.sort()
    second_lowest = score_list[1]
    out = [i[0] for i in records if i[1] == second_lowest]
    out.sort()
    for i in out:
        print(i)  
