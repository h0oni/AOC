#part 1
Li =[1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
Li_mem=Li[:]

# Li=[1,9,10,3,
# 2,3,11,0,
# 99,
# 30,40,50]

i=0
while i<len(Li):
  if Li[i]==1:
    Li[Li[i+3]]= Li[Li[i+1]]+Li[Li[i+2]]
  if Li[i]==2:
    Li[Li[i+3]]= Li[Li[i+1]]*Li[Li[i+2]]
  if Li[i]==99:
    break
  i=i+4

print(f'Ans(part-1): {Li[0]}')

# part2
Li=Li_mem[:]
flag=1
for j in range(100):
  for k in range(100):
    Li=Li_mem[:]
    i=0
    Li[1]=j
    Li[2]=k
    while i<len(Li):
      if Li[i]==1:
        Li[Li[i+3]]= Li[Li[i+1]]+Li[Li[i+2]]
      if Li[i]==2:
        Li[Li[i+3]]= Li[Li[i+1]]*Li[Li[i+2]]
      if Li[i]==99:
        break
      i=i+4
    # print(Li[0])
    if (Li[0])==19690720:
      flag=0
      # print(flag)
      break
  if not(flag):
    break

print(100*j+k)