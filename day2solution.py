from day2data import data 

def solution1(data):
    newData = data.split("\n")
    final_depth = 0 
    final_horizontal = 0
    for val in newData:
        current_val = val.strip().strip(',')
        if "forward" in current_val:
            temp = int((current_val[len(val)- 2]))
            final_horizontal = final_horizontal + temp
        elif "up" in current_val:
            temp = int((current_val[len(val)- 2]))
            final_depth -= temp
        elif "down" in val:
            temp = int((current_val[len(val)- 2]))
            final_depth += temp
        else: 
            pass
    product = final_depth * final_horizontal 
    print("Solution 1: The produce of final_depth and final_horizontal is: " + str(product))

def solution2(data):
    newData = data.split("\n")
    final_depth = 0 
    aim = 0 
    final_horizontal = 0
    for val in newData:
        current_val = val.strip().strip(',')
        if "forward" in current_val:
            temp = int((current_val[len(val)- 2]))
            final_horizontal += temp
            depth_change = aim * temp
            final_depth += depth_change 
        elif "up" in current_val:
            temp = int((current_val[len(val)- 2]))
            aim -= temp
        elif "down" in val:
            temp = int((current_val[len(val)- 2]))
            aim += temp
        else: 
            pass
    product = final_depth * final_horizontal 
    print("Solution 2: The produce of final_depth and final_horizontal is: " + str(product))
    

            



solution1(data)
solution2(data)