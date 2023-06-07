
# open file
with open('100words.txt') as file:
    # read lines into a list until empty line. then remaining lines into a second list
    words1 = []
    for line in file:
        if line.strip() == '':
            break
        words1.append(line.strip().lower())
    
    words2 = []
    for line in file:
        words2.append(line.strip().lower())

    print('wrong words:')

    for word in words2:
        if word not in words1:
            print(word)
    
    print('missing words:')
    for word in words1:
        if word not in words2:
            print(word)