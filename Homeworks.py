def Rec3(n):
    if n>0:
        Rec3(n-1)
        if n%10%3==0:
            if n%10==0:
                return
            print(n)
Rec3(50)