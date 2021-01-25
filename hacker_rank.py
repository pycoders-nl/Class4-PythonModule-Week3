# Bonus Question 1
# [HACKERRANK: FIND DIGITS](https: // www.hackerrank.com/challenges/find-digits/problem)

# Bonus Question 2
# [HACKERRANK: CAPITALIZE](https: // www.hackerrank.com/challenges/capitalize/problem)


# first in map I have capitalize the seperated words and add them back by using join method
def solve(s):
    return " ".join(map(lambda x: x.capitalize(), s.split(" ")))
