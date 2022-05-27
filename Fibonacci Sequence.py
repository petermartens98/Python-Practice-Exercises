# Fibonacci Sequence
# The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous
# two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
# Date: 8/9/2021


fiblength = int(input("Fibonacci Length: "))
fibseq = [1, 1]
i = 0
while i < fiblength - 2:
    nextfib = fibseq[i]+fibseq[i+1]
    fibseq.append(nextfib)
    i += 1

print(fibseq)





