
def get_dividend(number,divisor):
    dividend = number // divisor
    if number % divisor == 0:
        return dividend
    else:
        return dividend+1

def num_flagstones(n,m,a):
    no_tiles = get_dividend(n,a) * get_dividend(m,a)
    return no_tiles

n, m, a = map(int, input().split())

num_of_flagstones = num_flagstones(n,m,a)
print(num_of_flagstones)