data_input = [int(x.rstrip()) for x in open('day1_2021_input.txt')]

######## part 1 How many measurements are larger than the previous measurement?

increased=[]
#counter=0

for position, number in enumerate(data_input[:len(data_input)]):
    try:      
        if  number  < data_input[position+1]:
            #counter+=1
            increased.append(data_input[position+1])
    except IndexError:
        continue
  
print ('The number of times a depth measurment increases:', len(increased))

######### part 2 Count the number of times the sum of measurements in this sliding window increases from the previous sum

sum_list=[]

for position, number in enumerate(data_input[:len(data_input)]):
    try:      
        sum= data_input[position] + data_input[position+1] + data_input[position+2]
        sum_list.append(sum)
        
    except IndexError:
        continue


increased_sum=[]

for position, number in enumerate(sum_list[:len(sum_list)]):
    try:      
        if  number  < sum_list[position+1]:
            increased_sum.append(sum_list[position+1])
    except IndexError:
        continue
  
print ('The number of times the sum of measurements increases:', len(increased_sum))

