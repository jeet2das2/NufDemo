import random
import string
print(random.getrandbits(30))

result1 = ''.join((random.choice(string.ascii_uppercase) for x in range(4)))
print(result1)
print(type(result1))
