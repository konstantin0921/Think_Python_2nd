def str_fill(i, n):
    """returns i as a string with at least n digits.

    i: int
    n: int length

    returns: string
    """
    return str(i).zfill(n)



def is_reverse(n, m):
    """returns True if n and m are mutually reversed
    e.g. '37' and '73'

    n: int
    m: int

    returns: bool
    """
    return str_fill(n, 2)[::-1] == str_fill(m, 2)


def num_incidents(diff, flag=False):
    """Counts the number of palindromic ages.

    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.

    diff: int difference in ages
    flag: bool, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if is_reverse(daughter, mother) or is_reverse(daughter, mother+1):
            count += 1
            if flag:
                print(daughter,'\t', mother)

        if mother > 100:
            break
        daughter += 1

    return count



def check_diffs():
    """Finds age differences that satisfy the problem.

    Enumerates the possible differences in age between mother
    and daughter, and for each difference, counts the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 80:
        n = num_incidents(diff)
        if n > 0:
            print(diff,'\t', n)
        diff += 1

if __name__ == "__main__":
    print('diff\t #instances')
    check_diffs()

    print()
    print('daughter \t mother')
    num_incidents(18, True)







