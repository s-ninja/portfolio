def pamatb(kol, ed):
    if ed =='B':
        return kol
    elif ed == 'KB':
        return kol*1024
    elif ed == 'MB':
        return kol*1024*1024
    elif ed == 'GB':
        return kol*1024*1024*1024


with open('files.txt', encoding='utf-8') as f:
    sum = 0
    fline = f.readlines()
    fline = sorted(fline)
    fline = sorted(fline, key= lambda x: x[x.find('.'):x.find(' ')])
    for i in range (len(fline)):
        name, ob, ed = fline[i].split()
        if i != len(fline)-1:
            name1, ob1, ed1 = fline[i+1].split()
        else:
            name1, ob1, ed1 = fline[0].split()
        print(name)
        sum += pamatb(int(ob),ed.rstrip())
        if name1[name1.find('.'):] != name[name.find('.'):]:
            ed = 'B'
            if sum > 1023:
                ed = 'KB'
                sum = round(sum/1024)
                if sum > 1023:
                    ed = "MB"
                    sum = round(sum/1023)

                    if sum > 1023:
                        ed = 'GB'
                        sum = round(sum/1024)
            print('----------')
            print('Summary:',sum, ed)
            print()
            sum = 0
