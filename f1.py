def F1(val):
  if (val <= 2):
    return 1
  else:
    return (F1(val-1)+F1(val-2))


inputVal = []
with open('input1.txt') as f:
    for line in f:
        inputVal.append(int(line))


v=''
for i in inputVal:
    v += str(F1(i)) + '\n'
    
with open('output1.txt', 'a') as f:
    f.write(v)

    


