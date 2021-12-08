data = [(x.rstrip()) for x in open('day3_2021_input.txt')]


rows=len(data) # number of rows (12)
columns=len(data[0]) # number of columns. Lenght of binary string (5)


gamma_rate=[]
epsilon_rate=[]

for i in range (0,columns):
    one=[]
    zero=[]
    for j in range (0, rows):
        bit=data[j][i]
        if bit=='1':
            one.append(bit)
        else:
            zero.append(bit)
    if len(one)>len(zero):
         gamma_rate.append('1')
         epsilon_rate.append('0')
    else:
         gamma_rate.append('0')
         epsilon_rate.append('1')


#converting strings to numbers
gamma_rate = [int(i) for i in gamma_rate]
#print (gamma_rate)
epsilon_rate = [int(i) for i in epsilon_rate]
#print (epsilon_rate)

#binary to integer
def binatointeger(binary):
  number = 0
  for b in binary:
    number = (2 * number) + b
  return number
            
#print (binatointeger(gamma_rate))
#print (binatointeger(epsilon_rate))

print('Final answer pt.1:', binatointeger(gamma_rate)*binatointeger(epsilon_rate))
    
    
####################### part 2

data2 = data.copy()
index = 0

while len(data)>1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    for c in range(0,len(data)):
        if data[c][index] == '0':
            zero += 1
            zeros.append(data[c])
        else:
            one += 1
            ones.append(data[c])
    if zero > one:
        data = zeros
    else:
        data = ones
    index += 1
    
oxygen = int(data[0],2)


data=data2
index = 0

while len(data)>1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    for c in range(0,len(data)):
        if data[c][index] == '0':
            zero += 1
            zeros.append(data[c])
        else:
            one += 1
            ones.append(data[c])
    if one < zero:
        data = ones
    else:
        data = zeros
    index += 1
    
co2 = int(data[0],2)

print ('Final answer pt.2:', oxygen * co2)

            
