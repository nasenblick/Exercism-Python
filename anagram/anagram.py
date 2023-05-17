def find_anagrams(word, candidates):
    result = []
    compare = ''

    word_s = ''.join(sorted(word.lower()))
    
    # for candidate in candidates:
    #     word_s = word.lower()
    #     #print(word_s)
    #     candidate_s = candidate.lower()
    #     #print(candidate_s)
    #     if word_s != candidate_s:
    #         word_s = ''.join(sorted(word_s))
    #         print(word_s)
    #         candidate_s = ''.join(sorted(candidate_s))
    #         #print(candidate_s)
    #         if candidate_s == word_s:
    #             result.append(candidate)
    return word_s

print(find_anagrams('Orchestra', ['cashregister', 'Carthorse', 'radishes']))


        #print('word', word)
        #print('word_s', word_s)
        #print('candidate', candidate)
        #print('candidate_s', candidate_s)