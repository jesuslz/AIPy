from collections import defaultdict

d = {(i,j):i+j for i in range(1, 7) for j in range(1, 7)}
dinv = defaultdict(list)

for i, j in d.iteritems():
    dinv[j].append(i)
X = {i: len(j)/36. for i, j in dinv.iteritems()}
#print(X)
sum = 0
for i, j in X.iteritems():
    sum = sum + j#X[i]
    print(sum)
