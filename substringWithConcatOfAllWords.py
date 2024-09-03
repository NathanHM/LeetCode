s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]

def findSubstring(s, words):

    clean_concat = {}

    for word in words:
        clean_concat[word] = 0

    words_count = clean_concat.copy()
    for word in words:
        words_count[word] += 1
        
    results = []
    word_len = len(words[0])

    for j in range(word_len):

        n = j
        slow = n
        fast = n
        count = 1

        slow_word = s[slow:slow + word_len]

        while clean_concat.get(slow_word) == None and n <= len(s):
            n += word_len
            slow = n
            fast = n
            slow_word = s[slow:slow + word_len]


        concat = clean_concat.copy()
        if concat.get(slow_word) != None:
            concat[slow_word] += 1
            if len(words) == 1 and slow_word == words[0]:
                results.append(slow)

        for i in range(n + word_len, len(s) + 1, word_len):

            fast = i
            word = s[fast:fast + word_len]

            if concat.get(word) != None:

                concat[word] += 1

                while concat[word] > words_count[word]:
                    concat[slow_word] -= 1
                    slow += word_len
                    slow_word = s[slow:slow + word_len]
                    count -= 1

                if concat[word] <= words_count[word]:
                    count += 1

            else:
                concat = clean_concat.copy()
                slow = i + word_len
                slow_word = s[slow:slow + word_len]
                count = 0

            if count == len(words):

                results.append(slow)
                concat[slow_word] -= 1
                slow += word_len
                slow_word = s[slow:slow + word_len]
                count -= 1

    return results

print(findSubstring(s, words))