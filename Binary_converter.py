#To convert to Binary, divide by 2, get the remainder, and then divide again, get the remainder, repeat until its 1/2, and then
#concatenate the 1s and 0s, then reverse.
import math

pre_binary_list1 = []
pre_binary_list2 = []
binary_sum = []

def convert_to_binary(pre_binary_list):
    num = int(
        input(
            "Input a number to convert to Binary:\n"
            ).strip()
        )

    while num > 0:
        remainder = num % 2
        pre_binary_list.append(str(remainder))
        num = math.floor(num/2)
        
    binary_str = "".join(reversed(pre_binary_list))
    
    print(binary_str)

    pre_binary_list.reverse()

    return pre_binary_list


def add_binary(num_list_1, num_list_2):
    carry = False
    while len(num_list_1) > 0 and len(num_list_2) > 0:
        
        num_list_1.reverse()
        num_list_2.reverse()
        
        try:
            if carry == True:
                sum = int(num_list_1.pop(0)) + int(num_list_2.pop(0)) + 1
                
            elif carry == False:
                sum = int(num_list_1.pop(0)) + int(num_list_2.pop(0))

        
        except:
            if len(num_list_1) == 1 and len(num_list_2) == 0 or len(num_list_1) == 0 and len(num_list_2) == 1 or len(num_list_1) == 0 and len(num_list_2) == 0:
                if carry == True:
                    sum = int(num_list_1.pop(0)) + int(num_list_2.pop(0)) + 1
                
                elif carry == False:
                    sum = int(num_list_1.pop(0)) + int(num_list_2.pop(0))

            elif 
                if carry == True:
                    sum = int(num_list_1.pop(0)) + int(num_list_2.pop(0)) + 1
                
                elif carry == False:
                    sum = int(num_list_1.pop(0)) + int(num_list_2.pop(0))
            
            elif len(num_list_1) > len(num_list_2)
            
        if sum == 1:
                sum = 1
                carry = False

        elif sum == 2:
            sum = 0
            carry = True

        elif sum == 3:
            sum = 1
            carry = True

        binary_sum.insert(0, str(sum))

        


convert_to_binary(pre_binary_list1)
convert_to_binary(pre_binary_list2)
add_binary(pre_binary_list1, pre_binary_list2)

print("".join(binary_sum))