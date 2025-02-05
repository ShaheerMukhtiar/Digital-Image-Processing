
 # Normalization Function
def normalization(orig_list):
     x_min = min(orig_list)
     x_max = max(orig_list)
     norm_list =[]
     for i in orig_list:
         norm_list.append((i - x_min)/(x_max - x_min))
     return norm_list

 # Main Function
if __name__ == '__main__':
    list1 = [2,5,6,8,12,3,1,-1]
    print("List Before Min_Max Normalization:")
    print(list1)
    x_scaled = normalization(list1)
    print("\nList After Min_Max Normalization: ")
    print(x_scaled)





