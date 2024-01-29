numbers = [1, 5, 7, 9, 15]

while True:
    answer = input("数字か q を入力して")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字か q をタイプしてくれたら終わる")
    if answer in numbers:
        print("君の入力した数字は正解です。")
        break
    else:
        print("その数字ではないです")