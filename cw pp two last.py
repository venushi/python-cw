# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#student id(iit)-20191028     student id(uow)-W1790291
def credits() :
    global pass_credit
    global defer
    global fail
    global total

count =0
progress = 0
trailer = 0
retriever = 0
excluded = 0


while True :
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

        credits()

        if pass_credit+defer+fail!=120:
            print("total error")

        else:
         count+=1
            
         if pass_credit==120:
               print("progress")
               progress+=1
               
            
         else:
                if pass_credit==100:
                    print("progress-module trailer")
                    trailer+=1
                
                else:
                    if pass_credit==80 or pass_credit==60:
                        print("do not progress-module retriever")
                        retriever+=1
                     
                         
                    else:
                        if pass_credit==40 and defer !=0 or pass_credit==20 and defer>20 or pass_credit==0 and defer>40:
                            print("do not progress-module retriever")
                            retriever+=1
                          
                             
                        else:
                            print("excluded")
                            excluded+=1
       
     
         input_decision =input("Enter 'q' to quit or to continue enter any other letter:")
         if input_decision=='q':
              
         
          print("progress",progress,': ',progress  * '*')
          print("trailer",trailer,': ',trailer * '*')
          print("retriever",retriever,': ',retriever * '*')
          print("excluded",excluded,': ', excluded * '*')
          print(count,'outcomes in total')
          break

        
        

        
    
