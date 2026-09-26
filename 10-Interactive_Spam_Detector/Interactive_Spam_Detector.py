spam_keywords={"free","win"."winner","cash","prize","urgent","click","lottery"}
vocubulary={}
print("=====INTERACTIVE SPAM DETECTOR=====")
print("Type Exit To Quit The Program.")
while True:
    user_input=input("Enter The Sample Text Message To Be Analyzed:" )
    if user_input.strip().lower()=='exit':
        print("Exiting The Program.....")
        break
    cleaned_message=user_input.lower().replace("!","").replace("?",'').replace(".",'').replace(",","")
    words_list=cleaned_message.split()
    if not words_list:
        print("You Didn't Enter Any Message. Please Enter A Message To Run The Program...")
        continue
    spam_counter=0
    for word in words_list:
        if word in spam_keywords:
            vocubulary[word]+=1
        else:
            vocubulary[word]=1
        if word in spam_keywords:
            spam_counter+=1
if spam_counter>=2:
    print(f"RESULT: SPAM FLAGGED! Contains {spam_counter} Spam Words.\n")
else:
    print(f"RESULT: SAFE MESSAGE! Contains {spam_counter} Spam Words.\n")
input()
    
