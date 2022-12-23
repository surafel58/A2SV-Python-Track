if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    t = tuple(integer_list)
    print(hash(t))
