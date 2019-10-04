def staircase(n):
    for i in range(1,n+1):
        print(int(n-i)*' '+i*"#")
staircase(6)