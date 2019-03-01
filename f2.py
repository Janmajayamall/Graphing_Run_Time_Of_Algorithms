def F2(val):
  if (val <= 2):
    return 1
  else:
    p = 1
    q = 1
    r = 0
    for i in range(3, val+1):
      r = p + q
      p = q
      q = r
    return r  


inputVal = []
with open('input2.txt') as f:
    for line in f:
        inputVal.append(int(line))
  
v = ''      
for i in inputVal:
    v+=str(F2(i)) + '\n'



with open('output2.txt', 'a') as f:
    f.write(v)
