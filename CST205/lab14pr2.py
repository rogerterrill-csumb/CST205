def main():
    with open('pressreleases.html', 'r') as f:
        read_data = list(f)
        # read_data = str(f.readlines())
        for line in range(len(read_data)):
            if '<p class="uscb-margin-TB-02 uscb-title-3">' in read_data[line]:
                print(read_data[line+1].strip())
                # print('FOUND IT~!!!!!!!!!!~@!@#')


if __name__ == '__main__':
    main()
