# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    alphanum = alpha = dig = lower = upper = 'False'
    
    for i in s:
        if i.isalnum(): alphanum = 'True'
        if i.isalpha(): alpha = 'True'
        if i.isdigit(): dig = 'True'
        if i.islower(): lower = 'True'
        if i.isupper(): upper = 'True'
    
    print(alphanum + '\n' + alpha + '\n' + dig + '\n' + lower + '\n' + upper)
        
