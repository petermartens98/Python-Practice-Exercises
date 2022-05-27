# Fibonacci String
# A Fibonacci string is a precedence of the Fibonacci series. It works with any two characters of the English alphabet
# (as opposed to the numbers 0 and 1 in the Fibonacci series) as the initial items and concatenates them together
# as itprogresses in a similar fashion as the Fibonacci series.
# Examples:
#   fib_str(3, ["j", "h"]) ➞ "j, h, hj"
#   fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"
#   fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"
# Difficulty: Hard
# Date: 8/7/2021

letters = [0,1]

def fib_str(fiblength, letters):
    fibseq = letters

    i = 0

    while i < fiblength - 2:
        nextfib = fibseq[i+1] + fibseq[i]
        fibseq.append(nextfib)
        i += 1

    return fibseq

print(fib_str(3, ["j", "h"]))
print(fib_str(5, ["e", "a"]))
print(fib_str(6, ["n", "k"]))

