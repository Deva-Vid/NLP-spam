import re

def count_words(text):

    counts = dict()
    text = text.lower()
    words = re.split(r'[^\w]',text)
    for word in words:
        if word != "":
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    
    return counts

def test_run():

    with open('text.txt',"r") as f:

        text = f.read()
        counts = count_words(text)
        sorted_counts =sorted(counts.items(),key= lambda pair:pair[1],reverse=True)

        print('10 most common words:\n Word\tCount')
        for word , count in sorted_counts[:10]:
            print("{}\t{}".format(word,count))

        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word,count))

if __name__ == "__main__":
    test_run()


