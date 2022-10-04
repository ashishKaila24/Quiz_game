print("Wel come to quiz game")
print("enter 1 for master")
print("enter 2 for solver")
print("enter 3 for exit to the game")
question = []
option = []
right_ans = []
while True:
    a = input("Please enter your choise = ")
    if a == "1":
        print("Wel come to master")
        print("1 for add question")
        print("2 for show question")
        print("3 for delete question")
        print("4 for exit")
        while True:
            b = input("Please enter your choise = ")
            if b == "1":
                que = input("q: ")
                f = input("How many option you want : ")
                op = []
                for i in range(int(f)):
                    d = input("op" + str(i+1) + ": ")
                    op.append(d)
                ra = input ("ra: ")
                question.append(que)
                right_ans.append(ra)
                option.append(op)
            elif b == "2":
                for i in range(len(question)):
                    print("question" + str(i+1) + ": " + str(question[i]))
                    print("options : " + str(option[i]))
                    print("right answer : " + str(right_ans[i]))
            elif b == "3":
                w = int(input("Which question you want to delete : "))
                z = w-1
                question.pop(z)
                option.pop(z)
                right_ans.pop(z)
            elif b == "4":
                print("exit")
                break
            else:
                print("please enter valid option")
    elif a == "2":
        print("Welcome solver")
        r = 0
        w = 0
        for i in range(len(quizMaster.question)):
            print(quizMaster.question[i])
            print(quizMaster.option[i])
            k = input("Please enter your ans. = ")
            if k in quizMaster.right_ans:
                print("correct")
                r = r + 1
            else:
                print("sorry")
                w = w + 1
        print("your true ans = " + str(r))
        print("your worng ans = " + str(w))
    
    elif a == "3":
        print("exit")
        break
    else:
        print("please enter valid option")