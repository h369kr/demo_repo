# a = int(input())
# b = int(input())

# list1 = []
# def fact1(x):
#     for i in range (1,int(a/2)+1):
#         if a % i == 0:
#             list1.append(i)

# list2 = []
# def fact2(y):
#     for i in range (1,int(b/2)+1):
#         if b % i == 0:
#             list2.append(i)

# fact1(a)
# fact2(b)

# if a>b:
#     for i in reversed(list1):
#         for j in reversed(list2):
#             if i == j:
#                 print(i)
#             break
# else:
#     for i in reversed(list2):
#         for j in reversed(list1):
#             if i == j:
#                 print(i)
#             break

def gcd(p,q):
    if p < q:
        small = p
    else:
        small = q
    for i in range(1,small+1):
        if p % i == 0 and q % i == 0:
            gcd = i
    return(gcd)

gcd(8,12)

