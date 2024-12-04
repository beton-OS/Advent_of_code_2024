import re
import pandas as pd

def mul(s):
    numbers = s[s.find('(') +1:s.find(')')].split(',')
    return int(numbers[0]) * int(numbers[1])

with open('input.txt', 'r') as file:
    s = file.read()
    matches = re.findall('mul\(\d+,\d+\)' ,s)

df = pd.DataFrame(matches, columns = ['match'])

df['result'] = df['match'].apply(mul)

tot = df['result'].sum()

print('Solution to the first part:',tot)

cleaned = re.sub(r"don't\(\).*?do\(\)", '',s)
matches_2 = re.findall('mul\(\d+,\d+\)' ,cleaned)
df2 = pd.DataFrame(matches_2, columns = ['match'])

df2['result'] = df2['match'].apply(mul)

tot2 = df2['result'].sum()

print('Solution to the second part:',tot2)
