def remove(l):
    """Removes all the even indexed elements from a list and returns a new list"""
    new_l = []
    for i in range(1, len(l), 2):
        new_l.append(l[i])
    return new_l

# Parts of speech that we need
parts_of_speech = ['NN', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS']

"""def find_matching(tags, questions):
    count = 0; maxcount = 0
        for i in range(len(questions)):
            for j in tags:
                if j in tags of questions[i]:
                    count += 1
            if count > maxcount:
                index = i        return index """
