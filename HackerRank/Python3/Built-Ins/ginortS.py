# Enter your code here. Read input from STDIN. Print output to STDOUT
def sortedString(s):
    lowercase = []
    uppercase = []
    odd = []
    even = []
    for char in s:
        if char.islower():
            lowercase.append(char)
        elif char.isupper():
            uppercase.append(char)
        elif char.isdigit():
            if int(char)%2 == 0:
                even.append(char)
            else:
                odd.append(char)
    return (''.join(sorted(lowercase)+sorted(uppercase)+sorted(odd)+sorted(even)))

if __name__=='__main__':
    
    S = input()
    print (sortedString(S))
