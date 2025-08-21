from decimal import Decimal, getcontext, ROUND_HALF_UP
e = Decimal("2.7182818284590452353602875")
n = int(input())
getcontext().prec = n + 5
format_str = "1." + "0" * n
rounded_e = e.quantize(Decimal(format_str), rounding=ROUND_HALF_UP)
print(rounded_e)
