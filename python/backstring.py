def reverse_string(s):
    s = list(s)
    s.reverse()
    return "".join(s)

def back_string(s,n):
    n = n % len(s)
    head = reverse_string(s[0:n])
    tail = reverse_string(s[n:])
    result = reverse_string(head + tail)
    return result
    
if __name__ == "__main__":
    s = "abcdeg"
    n = 2
    result = back_string(s,n)
    print result 