data_input = [(x.rstrip()) for x in open('day2_2021_input.txt')]

forward_counter=0
depth_counter=0
aim_counter=0

for x in data_input:
    if 'forward' in x.split():
        forward=x.split()
        forward_counter=forward_counter + int(forward[1])
        aim_counter=aim_counter + depth_counter * int(forward[1])
       
    if 'down' in x.split():
        down=x.split()
        depth_counter=depth_counter + int(down[1])

    if 'up' in x.split():
         up=x.split()
         depth_counter=depth_counter - int(up[1])
  
print (forward_counter)
print (depth_counter)

position=forward_counter*depth_counter
print ('My position is', position)

final_depth=aim_counter*forward_counter
print ('My final position is', final_depth)




