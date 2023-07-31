def shuixian(n):
    x = n//100
    y = n//10 % 10
    z = n % 10
    if n == x**3+y**3+z**3:
        print(n, "这个数是水仙花数")
    else:
        print(n, "这个数不是水仙花数")


def sushu(n):
    for i in range(2, n):
        if n % i == 0:
            print(n, "这个数不是素数")
            break
        else:
            print(n, "这个数是素数")


if __name__ == "__main__":
    print("2150810123徐佳乐")
