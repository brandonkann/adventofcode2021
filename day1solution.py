from day1data import data 


def solution1(data, question):
    increases = 0 
    for iteration, value in enumerate(data):
        if iteration < len(data) - 1: 
            if data[iteration + 1] > value: 
                increases = increases + 1 
            else: 
                pass
    if question == 1:
        print('The total measurements larger than the previous measurement is: ' + str(increases))
    else: 
        print('Sums of a three-measurement sliding window answer is: ' + str(increases))

def solution2(data):
    threeWindowList = []
    for iteration, value in enumerate(data):
        if iteration < len(data) - 1:
            newIndex = sum(data[iteration:iteration + 3])
            threeWindowList.append(newIndex)
    solution1(threeWindowList, 2)

        

solution2(data)