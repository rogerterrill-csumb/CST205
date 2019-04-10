def headlines(file):
    f = open(file,'r')
    print("**** U.S. Census Bureau News! ****")
    read_data = list(f)
    for line in range(len(read_data)):
        if '<p class="uscb-margin-TB-02 uscb-title-3">' in read_data[line]:
            print(read_data[line+1].strip())
    f.close()

