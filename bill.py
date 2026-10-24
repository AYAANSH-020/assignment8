def calc(n, a, u, t, p, f):
    # n = name, a = address, u = units, t = type, p = previous due, f = senior flag
    print('Customer:', n)
    print('Address:', a)
    if t == 'H':
        if u <= 100:
            amt = u * 3
        elif u <= 300:
            amt = 100 * 3 + (u - 100) * 5
        else:
            amt = 100 * 3 + 200 * 5 + (u - 300) * 8
    elif t == 'C':
        if u <= 100:
            amt = u * 6
        elif u <= 300:
            amt = 100 * 6 + (u - 100) * 9
        else:
            amt = 100 * 6 + 200 * 9 + (u - 300) * 12
    else:
        print('bad type')
        return -1
    tax = amt * 0.18
    if f == 1 and t == 'H':
        amt = amt - amt * 0.05
    temp = amt + tax
    total = amt + tax + p
    if p > 0:
        total = total + p * 0.02
    print('Total:', total)
    return total


def calc2(n, a, u, t, p, f):
    # same as calc but returns a receipt string instead of printing
    s = ''
    s = s + 'Customer: ' + n + '\n'
    s = s + 'Address: ' + a + '\n'
    if t == 'H':
        if u <= 100:
            amt = u * 3
        elif u <= 300:
            amt = 100 * 3 + (u - 100) * 5
        else:
            amt = 100 * 3 + 200 * 5 + (u - 300) * 8
    elif t == 'C':
        if u <= 100:
            amt = u * 6
        elif u <= 300:
            amt = 100 * 6 + (u - 100) * 9
        else:
            amt = 100 * 6 + 200 * 9 + (u - 300) * 12
    else:
        return 'bad type'
    tax = amt * 0.18
    if f == 1 and t == 'H':
        amt = amt - amt * 0.05
    total = amt + tax + p
    if p > 0:
        total = total + p * 0.02
    s = s + 'Total: ' + str(total)
    return s
