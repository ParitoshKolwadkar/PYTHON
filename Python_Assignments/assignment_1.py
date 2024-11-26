var_int = 9
var_float = 8.1234
var_str = "Hello"
var_boolean = False

int_sum = var_int +2
print(int_sum)
int_subtraction = var_int -2
print(int_subtraction)

float_add = var_float+2
print(float_add)
float_subtraction = var_float-2
print(float_subtraction)

string_concat = var_str + " World"
str_repeat = var_str * 3
print(string_concat)
print(str_repeat)

list = [1,2,3,4,5]

for i in range(len(list)):
    print(list[i])
    i+=1

for i in list:
    print(i)