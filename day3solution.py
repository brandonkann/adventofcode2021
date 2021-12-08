from day3data import data 

print(data)


def solution1(data):
    new_data = data.split('\n')
    clean_data = new_data[1:len(new_data) - 1]
    gamma_rate = ""
    epsilon_rate = ""
    temp0 = 0
    temp1 = 0
    x = 0
    while x < 12:
        for val in clean_data:
            if val[x] == "0":
                temp0 += 1 
            else:
                temp1 += 1 

        if (temp0 > temp1):
            gamma_rate = gamma_rate + '0'
            epsilon_rate = epsilon_rate + '1'
        else: 
            gamma_rate = gamma_rate + '1'
            epsilon_rate = epsilon_rate + '0'
        temp0 = 0
        temp1 = 0
        x  += 1 
    
    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = int(epsilon_rate, 2)
    
    answer = gamma_rate_int * epsilon_rate_int

    print(answer) 

def solution2(data):

    print(data)

                    


        

    
solution2(data)