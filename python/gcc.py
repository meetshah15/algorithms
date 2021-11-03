def sol(n):
    value = int(n / 3)
    residue = 1 if n % 3 != n % 2 else 0
    return value * 2 + residue


# do not edit below code
def main():
    n = int(input())
    print(sol(n))


def securitiesBuying(z, security_value):

    no_of_stocks = 0
    security_value.sort()
    i = 0

    while z > 0:

        if i == len(security_value) - 1:
            if z < security_value[0]:
                break
            z -= security_value[i]
            no_of_stocks += 1
            i = 0
            continue

        if z > security_value[i]:
            z -= security_value[i]
            no_of_stocks += 1

        i += 1

    return no_of_stocks


def main1():
    z = 45
    security_value = [10, 7, 19]
    no_of_stocks_purchased=securitiesBuying(z, security_value)
    print(no_of_stocks_purchased)


if __name__ == '__main__':
    # main()
    main1()
