def main():
    num1 = 0
    num2 = 0
    p = 0
    while p != -1:
        print("enter num1")
        num1 = int(input())
        print("enter num2")
        num2 = int(input())
        print("choose 1 - addition, 2 - subtraction, 3 - multiplication, 4 - division, 5 - power")
        print("choose -1 - exit")
        p = int(input())

        if p == 1:
            print(num1 + num2)
        elif p == 2:
            print(num1 - num2)


        else:
            print("error Please choose a valid operation.")

    print("zho")


if __name__ == '__main__':
    main()