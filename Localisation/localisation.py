#! usr/bin/env python


colors = [['R','G','G','R','R']
		,['R','R','G','R','R']
		,['R','R','G','G','R']
		,['R','R','R','R','R']]

# pHit = 0.6
# pMiss = 0.2
# pExact = 0.8
# pOvershoot = 0.1
# pUndershoot = 0.1
measurement = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
p_move = 0.8
def localize(colors,measurement,motions,sensor_right,p_move):
	pinit = 1.0/ float(len(colors)) / float(len(colors[0]))
	# print pinit
	p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
	for i in range(len(measurement)):
		p = move(p,motions[i],p_move)
		p = sense(p,measurement[i],colors,sensor_right)
	
	return p


def sense(p,Z,colors,sensor_right):
	q = []
	sum = 0

	for i in range(len(p)):
		row = []
		for j in range(len(p[i])):
			hit = (colors[i][j] == Z)
			row.append(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
		q.append(row)
	
	for i in range(len(q)):
		for j in range(len(q[i])):
			sum = sum + q[i][j]
	
	for i in range(len(q)):
		for j in range(len(q[i])):
			q[i][j] /= sum
	# show(q)
	return q


		
	# 	sum = sum + q[i]
	# for i in range(len(q)):
	# 	q[i] = q[i] / sum
	# return q


def move(p,motion,p_move):
	q = []
	for i in range(len(p)):
		row = []
		for j in range(len(p[i])):
			row.append(p[(i-motion[0])%len(p)][(j-motion[1])%len(p[i])] * p_move + p[i][j] * (1-p_move))
		q.append(row)
			# q[i][j] = p[i][(j-motion[1])%len(p[i])] * p_move + p[(i-motion[0])%len(p)][j] * p_move
	# show(q)
	return q

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'


p = localize(colors,measurement,motions,sensor_right, p_move)
# sum_check = 0
# for i in range(len(p)):
# 	for j in range(len(p[i])):
# 		sum_check += p[i][j]

# print sum_check
show(p)
	# for i in range(len(p)):
	# 	q.append(pExact*(p[(i-U)%len(p)]) + pOvershoot*(p[(i-U-1)%len(p)]) + pUndershoot*(p[(i-U+1)%len(p)]))
	# return q

# for i in range(len(Z)):
# 	p = sense(p,Z[i])
# 	p = move(p,1)


# print p



	