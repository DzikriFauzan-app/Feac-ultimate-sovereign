import hashlib, sys, time

data = open(sys.argv[1], "rb").read()
h = hashlib.sha256(data).hexdigest()

print("FILE:", sys.argv[1])
print("TIME:", time.ctime())
print("SHA256:", h)
