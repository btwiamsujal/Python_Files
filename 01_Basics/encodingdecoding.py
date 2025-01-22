import random
import string

n = input("Enter your secret message: ")
  
#Encoding the message  
if len(n) >= 3:
    random_prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    s = random_prefix + n[1:] +n[0] + random_suffix
    print("your encoded message is:", s)
else:
    s = n[::-1]
    print("Your encoded Message is:", s)

#Decoding the message
if len(n)<=3:
    print("Your decoded Message is:", s[::-1])
else:
    e = s[len(n)+2] + s[3:len(n)+2]
    print("Your decoded Message is:", e)