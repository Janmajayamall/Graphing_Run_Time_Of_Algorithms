
def powerofG (n):
  G = [[0, 1],[1, 1]]
  if(n == 1):
    return G
  else :
    if (n%2 == 0):
      H = powerofG(n/2)
      return (matrixMul(H, H))
    else:
      H = powerofG((n-1)/2)
      temp = (matrixMul(H, H))
      return (matrixMul(temp, G))

def matrixMul(X, Y):
  result = [[0,0],[0,0]]
  for i in range((len(X))):
    for j in range(len(Y[0])):
      for k in range(len(Y)):
        result[i][j] += X[i][k] * Y[k][j]
  return result


def F3(n):
    temp = powerofG(n)
    return (temp[0][1])


inputVal = []
with open('input3.txt') as f:
    for line in f:
        inputVal.append(int(line))

v=''     
for i in inputVal:
    v += str(F3(i)) + '\n'

with open('output3.txt', 'a') as f:
    f.write(v)

  