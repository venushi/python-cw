# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#student id(iit)-20191028     student id(uow)-W1790291
progress=0
trailer=0
retriever=0
exclude=0

pass_credit=[120,100,100,80,80,80,60,60,60,60]
defer_credit=[0,20,0,40,20,0,60,40,20,0]
fail_credit=[0,0,20,0,20,40,0,20,40,60]

total=0
for a in range(0,10):
    if pass_credit[a]==120:
        print("progress")
        progress+=1
        total+=1
for a in range(0,10):
    if pass_credit[a]==100:
        print("progress-module trailer")
        trailer+=1
        total+=1
for a in range(0,10) and range(0,10):
    if pass_credit[a]<=80 and fail_credit[a]<=60:
        print("do not progress-module retriever")
        retriever+=1
        total+=1
for a in range(0,10):
    if fail_credit[a]>=80:
        print("exclude")
        exclude+=1
        total+=1

print("progress",progress,'a ',progress  * '*')
print("trailer",trailer,'a ',trailer * '*')
print("retriever",retriever,'a ',retriever * '*')
print("exclude",exclude,'a ', exclude * '*')
print(total,'outcomes in total')
