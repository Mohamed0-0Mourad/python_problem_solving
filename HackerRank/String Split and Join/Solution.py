

def split_and_join(line):
    # write your code here
    new = line.split()
    final = '-'.join(new)
    return final

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
