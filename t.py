secret_answer = "python"
answer = ""
count = 0
limit = 3
lose = False
while secret_answer != answer and not lose:
    if count  < limit:
        answer = input("What is the programming language used in this script?:")
        count += 1
    else:
        lose = True
if lose:
    print("u lose!")
else:
    print("u won!")