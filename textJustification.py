words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

def fullJustify(words, maxWidth):
        output = []
        line = []
        count = 0

        while len(words) > 0:

            while len(words) > 0 and count + len(words[0]) <= maxWidth:

                word = words.pop(0)

                line.append(word)
                count += len(word)
                if count < maxWidth:
                    count += 1

            if len(words) == 0:
                
                new_line = " ".join(line)

                while len(new_line) < maxWidth:
                    new_line += " "

                output.append(new_line)

                return output


            word_count = len(line)
            count -= len(line)

            # catch edge case where words with spaces between meets max width exactly
            check_count = 0
            for word in line:
                check_count += len(word)
                check_count += 1
            if check_count > maxWidth:
                count += 1

            # catch edge case where line has a single word
            if word_count == 1 and count < maxWidth:
                line.append("")
                word_count = 2

            spaces = maxWidth - count

            for i in range(spaces % max(1, (word_count - 1))):
                line[i] += " "

            spaces -= (spaces %  max(1, (word_count - 1)))
            spaces = int(spaces /  max(1, (word_count - 1)))

            for i in range(word_count - 1):
                big_space = ""
                line[i] += " " * spaces
            
            output.append("".join(line))

            line = []
            count = 0

print(fullJustify(words, maxWidth))