import sys

def circular_array_path(n, m):
    array = list(range(1, n+1))
    path = []
    index = 0
    while len(path) < n:
        path.append(array[index])
        index = (index + m - 1) % n
    return ''.join(map(str, path))

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])  
    print(circular_array_path(n, m))
