#Classwork from 8 February 2018
#Обработка данных WALS

def make_dict():
    d = {}
    f = open("WALS.tsv", encoding="utf-8")
    for line in f:
        if '\t' in line:
            l = line.split('\t')
            if l[3] in d:
                d[l[3]] += 1
            else:
                d[l[3]] = 1
    return d

##def make_dict_values():
##    d = {}
##    f = open("WALS.tsv", encoding="utf-8")
##    for line in f:
##        if '\t' in line:
##            l = line.split('\t')
##            if l[3] in d:
##                d[l[3]] += float(l[2])
##            else:
##                d[l[3]] = float(l[2])
##    return d

def sort_dict(d):
    for k in sorted(d, key=d.get, reverse = True):
        print(k,'\t',d[k])

def check_all_orders(d):
    imp_orders = ''
    #all_orders = 'SVO SOV VSO VOS OVS OSV'
    #a = all_orders.split()
    a = list(d.keys())
    for order in a:
        if order not in d:
            imp_orders += s
    if imp_orders != '':
        return 'Нет таких порядков слов как \n' + imp_orders
    else:
        return 'Все возможные порядки слов есть.'

def main():
    d = make_dict()
    sort_dict(d)
    print(check_all_orders(d))
        
if __name__ == "__main__":
    main()
