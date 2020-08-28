from knackt.knackt import Knackt

token = 'your account token here'
timestamp = 'unix timestamp here'

e = Knackt(token).categories()
# you can iterate over the list
for f in e:
    print(f)

e = Knackt(token).category_created(timestamp)
# you can iterate over the list
for f in e:
    print(f)