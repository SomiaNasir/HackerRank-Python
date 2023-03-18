# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count = 0
    i= 0
    while i < len(string)-len(sub_string):
        if sub_string in string[i:]:
            count += 1
            i = string.find(sub_string, i)
        i += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
