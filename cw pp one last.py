# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#student id(iit)-20191028     student id(uow)-W1790291
def total():
    global pass_credit
    global defer      #defer_credit
    global fail       #fail_credit
    global total
    total=pass_credit+defer+fail
while True:
    try:
        pass_credit=int(input("enter your pass credit:"))
        if pass_credit%20==0 and pass_credit<=120 and pass_credit>=0:
            break
        else:
            print("range error")
    except ValueError:
         print("integer required")

while True:
    try:
        defer=int(input("enter your defer:"))
        if defer%20==0 and defer<=120 and defer>=0:
            break
        else:
            print("range error")
    except ValueError:
        print("integer required")

while True:
    try:
        fail=int(input("enter your fail:"))
        if fail%20==0 and fail<=120 and fail>=0:
            break
        else:
            print("range error")
    except ValueError:
        print("integer required")

total()
while True:
    if total<=120:
        break
    else:
        print("total error")
        break
while True:
    if pass_credit==120:
        print("progress")
        break
    else:
        if pass_credit==100:
            print("progress-module retriever")
            break
        else:
            if pass_credit==80 or pass_credit==60:
                print("do not progress")
                break
            else:
                if pass_credit==40 and defer !=0 or pass_credit==20 and defer>20 or pass_credit==0 and defer>40:
                    print("do not progress-module retriever")
                    break
                else:
                    print("exclude")
                    break
        
    
