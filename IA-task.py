## Question

# In a university, your attendance determines whether you will be
# allowed to attend your graduation ceremony.
# You are not allowed to miss classes for four or more consecutive days.
# Your graduation ceremony is on the last day of the academic year,
# which is the Nth day.


#  Your task is to determine the following:

# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.

# Represent the solution in the string format as "Answer of (2) / Answer
# of (1)", don't actually divide or reduce the fraction to decimal

# Test cases:

# for 5 days: 14/29
# for 10 days: 372/773

# mathematical programming approach
import pdb
def possibilities_to_graduate(N):
    # pdb.set_trace()
    if N<4:
        # we can solve the problem using mathematical formula
        # 2 ** (N - 1)
        return f'{2**(N-1)}/{2**N}'

    # There would be two choices everyday present , absent
    total_choices=2
    present=1
    absent=1

    # taking 3 because until 3 days it is handled inside the condition
    # Sample possibilities for 3 days
    # ['AAA','PPP','PAP','APA','PPA','APP','AAP','PAA'] -> n = 8
    # possibilities of graduating for 3 days -> ['PPP','PAP','PPA','APP'] -> P 50%
    possibilities = 2**(3-1)
    no_of_ways_to_attend = 2**3

    for _ in range(4,N+1):
        temp,absent,present,total_choices,possibilities = absent,present,total_choices,possibilities,no_of_ways_to_attend
        no_of_ways_to_attend = (no_of_ways_to_attend-temp)*2+temp
    return f'{absent+present+total_choices}/{no_of_ways_to_attend}'

print(possibilities_to_graduate(5))
print(possibilities_to_graduate(10))


# reference
# https://math.stackexchange.com/a/4163603/1257569


