def merge(a,b):
    result = []
    for i in range (max(len(a), len (b))):
        if i < len(a): result.append(a[i])
        if i < len(b): result.append(b[i])
        return result
