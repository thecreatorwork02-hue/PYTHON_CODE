a = str(input("Enter your comment: ")).lower()

if( "click now".lower() in a):
    print("your comment has been flagged by the AI")
elif("free money".lower() in a):
    print("your comment has been flagged by the AI")
elif("free trading course".lower() in a):
    print("your comment has been flagged by the AI")
else:
    print("Your comment has been posted successfully.")
