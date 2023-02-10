import random
import string
n=random.randint(8,16)
uppercase=list(string.ascii_uppercase)
lowercase=list(string.ascii_lowercase)
digits=list(string.digits)
special=list(string.punctuation)
total=uppercase+lowercase+digits+special
s=[]
s.extend(random.choice(uppercase))
s.extend(random.choice(lowercase))
s.extend(random.choice(digits))
s.extend(random.choice(special))
s.extend(random.sample(total,n-4))
random.shuffle(s)
password=''.join(s)
print(password)
