""" def square_matrix_map(matrix=[]):
   list(map(lambda x: list(map(lambda y: y**2, x)),matrix))
   #outer loop and inner loop list(map(lambda x: ---),matrix))
   #inner loop ---- list(map(lambda y: y**2, x)--
 """

def multiply_list_map(my_list, number):
    return list(map(lambda x : x *number,my_list))
   
my_list = [2, 3, 5, 3, 5]
print(multiply_list_map(my_list, 18))