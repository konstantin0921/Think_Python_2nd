import random

def has_duplicates(t):
    """returns True when any element i t appears more than once

    t: list or string

    returns: bool
    """
    return len(set(t)) != len(t)


def random_birthday(n):
    """returns a list of integers between 1 and 365 with length n, which represents n birthdays

    n: integers

    returns: list of int
    """
    birthdays = []
    for i in range(n):
        bd = random.randint(1, 365)
        birthdays.append(bd)

    return birthdays


def trial_simulation(num_students, num_simulations):
    """generates a sample of birthdays, check whether there are two students having same birthdays

    num_students: how many students in a sample
    num_simulations: how many samples to simulate

    returns: int
    """
    count = 0
    for i in range(num_simulations):
        birthdays = random_birthday(num_students)
        if has_duplicates(birthdays):
            count += 1

    return count



def main():
    num_students = 23
    num_simulations = 10000
    hit = trial_simulation(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % hit)
    print('Probability is %f' % (hit / num_simulations))


if __name__ == '__main__':
    main()

