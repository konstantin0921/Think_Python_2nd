def ack(m, n):
    """Ackermann function

    if m = 0, then A(m, n) = n +1
    if m > 0 and n = 0, then A(m, n) = A(m-1, 1)
    if m > 0 and n > 0, then A(m, n) = A(m-1, A(m, n-1))
    """
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))



memo = {}

def ack_memo(m, n):
    if (m, n) in memo:
        return memo[m, n]

    if m == 0:
        res = n+1
        memo[m, n] = res
        return res
    if m > 0 and n == 0:
        memo[m, n] = ack_memo(m-1, 1)
        return memo[m, n]
    if m > 0 and n > 0:
        memo[m, n] = ack_memo(m-1, ack_memo(m, n-1))
        return memo[m, n]




if __name__ == '__main__':
    assert(ack(3, 4) == 125)

    print(ack(3,6))
    print(ack_memo(3,6))
