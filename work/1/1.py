## fairly simple solution
if __name__ == '__main__':
    for x in range(1, 1001):
        if (x % 3 == 0) or (x % 5 == 0):
            print(x)
        else:
            continue