print("Wel come to master branch".center(100))
print("\t")
print("menu".center(50))
print("press 1 for add question")
print("press 2 for view question")
print("press 3 for delete question")
print("press 4 for exit question")
question = []
option = []
right_ans = []
while True:
    a = input("Please enter your choice : ")
    if a == "1":
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
    elif a == "2":
        for i in range(len(question)):
            print("question" + str(i+1) + ": " + str(question[i]))
            print("options : " + str(option[i]))
            print("right answer : " + str(right_ans[i]))
    elif a == "3":
        w = int(input("Which question you want to delete : "))
        z = w-1
        question.pop(z)
        option.pop(z)
        right_ans.pop(z)
    elif a == "4":
        print("exit")
        break