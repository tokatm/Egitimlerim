import numpy as np
import sympy as sym
from sympy import Matrix
from sympy import *
from sympy import poly
from sympy.abc import x
init_printing(use_unicode=True)


#%% define to variables, my goal is to operate o indices.
sValues = (1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0)


n2 = Matrix([
             [sValues[1], sValues[0]],
             [sValues[2], sValues[1]]
            ])


n3 = Matrix([
             [sValues[2], sValues[1], sValues[0]],
             [sValues[3], sValues[2], sValues[1]],
             [sValues[4], sValues[3], sValues[2]] 
            ])

n4 = Matrix([
             [sValues[3], sValues[2], sValues[1], sValues[0]],
             [sValues[4], sValues[3], sValues[2], sValues[1]],
             [sValues[5], sValues[4], sValues[3], sValues[2]],
             [sValues[6], sValues[5], sValues[4], sValues[3]] 
            ])


n5 = Matrix([
             [sValues[4], sValues[3], sValues[2], sValues[1], sValues[0]],
             [sValues[5], sValues[4], sValues[3], sValues[2], sValues[1]],
             [sValues[6], sValues[5], sValues[4], sValues[3], sValues[2]],
             [sValues[7], sValues[6], sValues[5], sValues[4], sValues[3]],
             [sValues[8], sValues[7], sValues[6], sValues[5], sValues[4]] 
            ])


## Define to functions
#%% for n = 2;


def for_n2():
            
        control_n2 = n2.inv_mod(2)*Matrix([sValues[2], sValues[3]])

        control_n2_1 = Matrix([[sValues[8], sValues[7]], 
                                           [sValues[9], sValues[8]]]) %2 *control_n2 
        control_n2_1 = control_n2_1 % 2
    
        if  control_n2_1 == Matrix([sValues[9], sValues[10]]):
               
            print('{:d} - bit LFSR construct'.format(2))

        else:
             print('not equalitiy')

  
 
#%%for n = 3;

def for_n3():
    control_n3 = n3.inv_mod(2)*Matrix([sValues[3], sValues[4], sValues[5]])
    control_n3_1 = Matrix([[sValues[10], sValues[9], sValues[8]], 
                           [sValues[11], sValues[10], sValues[9]],
                           [sValues[12], sValues[11], sValues[10]]]) %2 * control_n3
       
    control_n3_1 = control_n3_1 %2

    if  control_n3_1 == Matrix([sValues[11], sValues[12], sValues[13]]):
        print('{:d} - bit LFSR construct'.format(3))

    else:
        print(control_n3_1 , '!= {:d}, {:d}, {:d} '.format(sValues[11], sValues[12], sValues[13]))

    

#%% for n = 4;

def for_n4():
    control_n4 = n4.inv_mod(2) * Matrix([sValues[4], sValues[5], sValues[6], sValues[7]])
    control_n4_1 = Matrix([[sValues[18], sValues[17], sValues[16], sValues[15]], 
                            [sValues[19], sValues[18], sValues[17], sValues[16]],
                            [sValues[20], sValues[19], sValues[18], sValues[17]],
                            [sValues[21], sValues[20], sValues[19], sValues[18]]
                            ]) %2 * control_n4 
    
    control_n4_1 = control_n4_1 %2

    if  control_n4_1 == Matrix([sValues[19], sValues[20], sValues[21], sValues[22]]):
        print('{:d} - bit LFSR construct'.format(4))

    else:
        print(control_n4_1 , '!= {:d}, {:d}, {:d}, {:d} '.format(sValues[19], sValues[20], sValues[21], sValues[22]))

    

#%%  for n = 5;

def for_n5():
    cValues_n5 = n5.inv_mod(2) * Matrix([sValues[5], sValues[6], sValues[7], sValues[8], sValues[9]])  
    valid_n5 =  Matrix([[sValues[19], sValues[18], sValues[17], sValues[16], sValues[15]], 
                            [sValues[20], sValues[19], sValues[18], sValues[17], sValues[16]],
                            [sValues[21], sValues[20], sValues[19], sValues[18], sValues[17]],
                            [sValues[22], sValues[21], sValues[20], sValues[19], sValues[18]],
                            [sValues[23], sValues[22], sValues[21], sValues[20], sValues[19]]
                                        ]) %2 * cValues_n5
    valid_n5 = valid_n5 %2
         
    if  valid_n5 == Matrix([sValues[20], sValues[21], sValues[22], sValues[23], sValues[24]]):
        print('{:d} - bit LFSR construct'.format(5))
        print('Validation for s(20-24): ',valid_n5 , '== s20: {:d}, s21: {:d}, s22: {:d}, s:23: {:d}, s24: {:d} '.format(sValues[20], sValues[21], sValues[22], sValues[23], sValues[24]))
        
    else:
        print(valid_n5 , '!= {:d}, {:d}, {:d}, {:d}, {:d} '.format(sValues[20], sValues[21], sValues[22], sValues[23], sValues[24]))

    print('Coeffs of Connection Polynomial: ', cValues_n5 % 2)

    

#%% Run to functions
for_n5()

   
