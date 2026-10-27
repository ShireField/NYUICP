def proper_divisors(N):
    adder = 0
    for i in range (1,N,1):
        if N % i == 0:
            adder += i
    return adder
def perfect_number(N):
    return proper_divisors(N) == N
def main():
    for i in range (1,10001,1):
        if perfect_number(i):
            print(i)
main()
