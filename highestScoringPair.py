# import data, sort longest to shortest
with open('words.txt','r') as f:
	words=[]
	for line in f:
		strip_lines=line.strip()
		words.append(strip_lines)
words.sort(reverse=True, key = lambda x: len(x))

def highest_scoring_pair(input):
    topScore = 0
    i = 0
    result = [input[i], input[i + 1]]
    while (len(input[i]) * len(input[i + 1]) > topScore):   # iterate through words from longest, until we can't beat the top score
        w = input[i]
        j = 1
        while (len(w) * len(input[i + j]) > topScore):  # iterate through second word in pair, until we can't beat the top score
            w2 = input[i + j]
            skip = 0  # trigger to move to the next word
            for l in w:
                if l in w2:
                    j += 1
                    skip = 1
                    break
            if skip == 0:  # if no letters match, replace the current top pair and score
                result = [w, w2]
                topScore = len(w) * len(w2)
        i += 1
    return result

print(highest_scoring_pair(words))










