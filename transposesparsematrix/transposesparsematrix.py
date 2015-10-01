data='''10  1   x_time
10  2   x_time
9   3   x_time
2   15  x_time
7   16  x_time
10  18  x_time
3   25  x_time
5   31  x_time
2   35  x_time
4   1   t_msg
3   5   t_msg
5   9   t_msg
8   10  t_msg
4   90  t_msg
8   4    g_up
3   5    g_up
3   56   g_up'''

matrix = {}
for line in data.splitlines():
	rank, day, parameter = line.split()
	if parameter not in matrix.keys():
		matrix[parameter] = {}
	daydict = {day: rank}
	matrix[parameter].update(daydict)

print '\t{}'.format('\t'.join(['day'+str(i) for i in range(1,91)]))

for parameter in matrix:
	colvals = [matrix[parameter].get(str(i),'0') for i in range(1, 91)]
	print '{}\t{}'.format(parameter, '\t'.join(colvals))