import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}  # 'r': 12

for character in message.upper():
    if character not in count:
        count[character] = 1
    else:
        count[character] += 1

pprint.pprint(count)
    

# Al's way
#for character in message.lower():
#    count.setdefault(character, 0)
#    count[character] = count[character] + 1

#print(count)
