import os

file_dir = os.getcwd()[:-5]
converted_lines = []
f = open(file_dir + '/rars/input.csv', 'r')

csv_lines = f.readlines()[1:]


for line in csv_lines:
    line = line.strip('\n')
    first_clause = False
    second_clause = False

    elems = line.split(';')
    print('line_name:', elems[0])
    print('first clause:', end='\t')
    if ('X' not in elems[0]) and ('Z' not in elems[0]):
        first_clause = True
    
    print(first_clause)
    
    sum = 0
    elems = elems[2:]
    elems = elems[:3]

    for elem in elems:
        sum += int(elem)

          
    if sum in [15, 25, 35, 47, 101, 201]:
        second_clause = True
    print('second clause: (sum: ' + str(sum) + ')', end='   ')
    print(second_clause)

    if first_clause and second_clause:
        converted_lines.append(line)


f_out = open(file_dir + '/rars/output.csv', 'w')
for conv in converted_lines:
    f_out.write(conv)