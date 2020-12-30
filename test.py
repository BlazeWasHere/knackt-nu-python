# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from knackt.knackt import Knackt

token = 'your token here'
timestamp = '1591709025441'

knackt = Knackt(token)

ret = knackt.categories()
# you can iterate over the list
for f in ret:
    # f['name'] and f['hash'] can be used to pass into 
    # `download(...)` to download a file
    print(f)

ret = knackt.category_created(timestamp)
# you can iterate over the list
for f in ret:
    print(f)

# example of downloading
# ret = knackt.download(combo_hash, name)
# print(ret.decode())
# with open('test.txt', 'wb') as f:
#    f.write(ret)
