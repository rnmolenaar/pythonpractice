# return index of a list

def index_list(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]

print(index_list([1,2,3,4,5], -2))
