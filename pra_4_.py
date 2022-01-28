##20CE112 Yash Patel
##Github Repository Link
##https://github.com/Yash-3122/Assignment4
##List and Answers:Find runner-up from given list



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
