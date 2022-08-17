                # '''      email validation project in python using string          '''




email = input("enter your email : ")
j,d,k=0,0,0
if len(email)>=6:                                          # --> lenth of the email
    if(email)[0].isalpha():                                #---> check first letter of the email is alphabetic or not
        if ("@" in email) and (email.count("@")==1):       #---> check @ count on email
            if(email[-4] ==".") ^ (email[-3]=="."):        #---> check the last (.) sigh in email
                for i  in email:
                    if i==i.isspace():                     #----> check space in email 
                        k=1
                    elif i.isalpha():                      #---> check first letter 
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                        
                if k==1 or j==1 or d==1:
                    print("wrong email 5")
                else:
                    print("right email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email  1 ")









                            # Email validation python (Using Regex)>


# import re 
# email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# user_email = input("enter your email : ")
# if re.search(email_condition,user_email):
#     print("right email")
# else:
#     print("wrong email")