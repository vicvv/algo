
# # without the generator
# def fib(getrange):
#     fib_seq = [1,1]
#     for i in range(2,getrange+1):
#         last = fib_seq[i-1]
#         second_last = fib_seq[i-2]
#         num = last + second_last
#         fib_seq.append(num)
#     return fib_seq

# print(fib(10))


# with generator

def fib(n):
    last = 1
    second_last = 1
    current = 3
    while current <= n:
        num = last + second_last
        yield num
        second_last = last
        last = num
        current +=1

for val in fib(10):
    print(val)