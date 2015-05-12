a = '\xa1'
b = 'normal string'

try:
    c = b.encode('ascii')
    d = a.encode('ascii')
except Exception as e:
    print (e.object)
