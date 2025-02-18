import numpy as np

def calculate(*args):
    if len(args) != 9:
        raise ValueError('List must contain nine numbers')
    else:
        matrix_A = np.array(args).reshape(3,3)
        
    mean = [(matrix_A.mean(axis=0).tolist()),
                (matrix_A.mean(axis=1).tolist()),
                (matrix_A.mean().flatten())]
        
    vari = [(matrix_A.var(axis=0).tolist()),
                (matrix_A.var(axis=1).tolist()),
                (matrix_A.var().flatten()),]
    maxI = [(matrix_A.max(axis=0).tolist()),
                (matrix_A.max(axis=1).tolist()),
                (matrix_A.max().flatten()),]
    
    standard =  [(matrix_A.std(axis=0).tolist()),
                (matrix_A.std(axis=1).tolist()),
                (matrix_A.std().flatten()),]
    
    minI =  [(matrix_A.min(axis=0).tolist()),
                (matrix_A.min(axis=1).tolist()),
                (matrix_A.min().flatten()),]
    
    sumI=  [(matrix_A.sum(axis=0).tolist()),
                (matrix_A.sum(axis=1).tolist()),
                (matrix_A.sum().flatten()),]
        
    out_dict = {
        'mean': mean,
        'Variance': vari,
        "max": maxI,
        "standard deviation": standard,
        "sum": sumI,
        "min": minI,
    }
    return out_dict

return_value = calculate(1,2,3,4,5,6,7,8,9)

print(return_value)
