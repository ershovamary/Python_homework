
def make_dict():
    d = {}
    f = open("South park.tsv", encoding="utf-8")
    for line in f:
        if ',' in line:
            l = line.split(',')
            if l[0] != 'Season':
                
    return d


def main():



if __name__ == "__main__":
    main()
