import numpy as np

def calculate(lst):
    if len(lst) != 9: raise ValueError('List must contain nine numbers.')
    mat = np.array(lst).reshape(3,3)

    outpt = {}
    for i in range(3):
        outpt['mean'] = outpt.get('mean', []) + [mat.mean(axis=i).tolist() if i < 2 else mat.flatten().mean().tolist()]
        outpt['variance'] = outpt.get('variance', []) + [np.var(mat, axis=i).tolist() if i < 2 else np.var(mat).tolist()]
        outpt['standard deviation'] = outpt.get('standard deviation', []) + [mat.std(axis=i).tolist() if i < 2 else mat.flatten().std().tolist()]
        outpt['max'] = outpt.get('max', []) + [mat.max(axis=i).tolist() if i < 2 else mat.flatten().max().tolist()]
        outpt['min'] = outpt.get('min', []) + [mat.min(axis=i).tolist() if i < 2 else mat.flatten().min().tolist()]
        outpt['sum'] = outpt.get('sum', []) + [mat.sum(axis=i).tolist() if i < 2 else mat.flatten().sum().tolist()]

    return outpt
