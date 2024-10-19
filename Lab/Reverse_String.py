def reverse_string(s):
    ''' 's' is Supposed to be a string
        and It returns the reverse of 's' '''
    rv=''
    for ch in s:
        rv=ch+rv
    return rv
string=input("Enter a String: \n")
print(reverse_string(string))
