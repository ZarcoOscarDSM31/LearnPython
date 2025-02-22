try:
    #new_file = open(r'C:\DataFilesPy\new_file.txt', 'w')
    #new_file.write('Hello world\n')
    #new_file.write('Hello UTVT\n')
    #new_file.write('Oscar Zarco\n')
    #new_file.close()

    path = r'C:\DataFilesPy\new_file.txt'
    new_file = open(path, 'r')

    for line in new_file:
        print(line)
except Exception as e:
    print(f'Exception, error: {e}')
