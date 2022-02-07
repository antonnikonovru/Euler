n=20
i=19
while i>0:
  if n%i==0:
      i-=1
  else:
      n+=20
      i=19
  if i==1:
    print (n)

c = 0
e = 0
while c != 20:
    c = 0
    e += 2520
    for i in range(1,21):
        if e % i == 0:
            c += 1
print(e)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def lcmList(nums):
    if (len(nums) == 2):
        return int(lcm(nums[0], nums[1]))
    last = nums.pop()
    return int(lcm(lcmList(nums), last))


nums = []
for i in range(1, 21):
    nums.append(i)

print(lcmList(nums))

k=20
mn=6
for n in range(4,k+1):
    i=2
    while mn%n!=0:
        if n%i==0:
            while n>i:
                n=n/i
            mn*=n
        else:
            i+=1
print(mn)