if __name__ == "__main__":
    all_fibs = [1, 2]
    sum = 0
    while all_fibs[-1] < 4000000:
        x = all_fibs[-1] + all_fibs[-2]
        if x >= 4000000:
            break
        else:
            all_fibs.append(x)
        if (x % 2 == 0):
            sum = sum + x

    print(sum)