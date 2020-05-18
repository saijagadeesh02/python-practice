def large_sum(l):

    current_sum = max_sum = l[0]

    for item in l[1:]:
        current_sum = max(current_sum+item, item)
        max_sum = max(current_sum, max_sum)
    return max_sum


def rev1(string):

    s = string.strip()
    s = s.split()
    return " ".join(reversed(s))

def rev(string, delimit = None):

    l = len(string)
    delimiter = delimit if delimit else [" "] 
    words_list = []
    i = 0
    while(i < l):

        if string[i] not in delimiter:
            word_start = i

            while((i < l) and  (string[i] not in delimiter)):
                i += 1

            words_list.append(string[word_start:i])
        i += 1

    return words_list


def compress(s):

    r = ""
    l = len(s)
    i = 1
    cnt = 1
    while(i<l):

        if s[i] == s[i-1]:
            cnt += 1
        else:
            r += s[i-1] + str(cnt)
            cnt = 1
        i += 1
    r += s[i-1] + str(cnt)
    print(r)

def uniq_char(s):

    l = len(s)
    i = 1
    while i<l:
        if s[i] in s[i+1 :] and s[i-1::-1]:
            return False
        i += 1
    return True

#compress("AAALLL")

print(uniq_char("abcde"))
        