#original version, can run but not matching assignment requirement
'''
def greatest_common_divisor (numerator, denominator):
    greatest_common_divisor = 0
    can_simplify = False
    for i in range (denominator+1,1,-1):
        if numerator%i == 0 and denominator % i == 0:
            greatest_common_divisor = i
            break
    if greatest_common_divisor != 1:
        can_simplify = True
    return int(greatest_common_divisor), can_simplify
def reduce_fraction (numerator, denominator, greatest_common_divisor):
    simplified_numerator = numerator/greatest_common_divisor
    simplified_denominator = denominator/greatest_common_divisor
    return int(simplified_numerator), int(simplified_denominator)
def main():
    Numerator = int(input("Enter the numerator: >"))
    Denominator = int(input("Enter the denominator: >"))
    Greatest_common_divisor , Can_simplify = greatest_common_divisor(Numerator, Denominator)
    Simplified_numerator , Simplified_denominator = reduce_fraction(Numerator, Denominator, Greatest_common_divisor)
    if Can_simplify:
        print(f'The fraction {Numerator}/{Denominator} can be reduced to {Simplified_numerator}/{Simplified_denominator}')
    else:
        print(f'The fraction {Numerator}/{Denominator} cannot be reduced')
main()
'''

def greatest_common_divisor(n, d):
    for i in range(min(n, d), 0, -1):
        if n % i == 0 and d % i == 0:
            return i
    return 1
def reduce_fraction(n, d):
    gcd = greatest_common_divisor(n, d)
    reduced_n = n // gcd
    reduced_d = d // gcd
    return reduced_n, reduced_d
def main() :
    num = int(input("Enter the numerator: >"))
    den = int(input("Enter the denominator: >"))
    gcd = greatest_common_divisor(num, den)
    reduced_num, reduced_den = reduce_fraction(num, den)
    if gcd > 1 :
        print(f"The fraction {num}/{den} can be reduced to {reduced_num}/{reduced_den}")
    else :
        print(f"The fraction {num}/{den} cannot be reduced")
main()