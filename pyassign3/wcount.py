import sys
from urllib.request import urlopen

def wcount(lines,topn=10):
    import string
    a=lines.lower()
    for i in string.punctuation:  
            a=a.replace(i,"")
    lst=list(reversed(a.split()))
    counts = {}
    for l in lst:
        counts[l] = counts.get(l, 0) + 1
    counts2=sorted(counts.items(), key=lambda kv:kv[1])
    for k in range(1,topn+1):
        print(counts2[-k][0],"      ",counts2[-k][1])

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)