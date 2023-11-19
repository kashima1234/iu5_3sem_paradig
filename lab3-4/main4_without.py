data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # Sorting with the abs function directly as the key
    result = sorted(data, key=abs, reverse=True)
    print(result)
