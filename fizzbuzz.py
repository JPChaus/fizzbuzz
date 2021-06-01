def main():
    for i in range(1, 101):
        print(printValue(i))

def printValue(i):
    if((i%3 != 0) and (i%5 != 0)):
        return i

if __name__ == '__main__':
    main()