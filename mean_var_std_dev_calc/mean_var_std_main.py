#import mean_var_std
from mean_var_std import calculate
from unittest import main

lst1 = [0,1,2,3,4,5,6,7,8]
#lst2 = [9,1,5,3,3,3,2,9,]
print(calculate(lst1))

#THIS WILL RUN THE MEAN_VAR_STD_TEST AUTOMATICALLY
main(module='mean_var_std_test', exit=False)
