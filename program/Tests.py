
with open("questions.txt", "r", encoding="utf-8") as my_file:
    with open("ansnwer.txt", "w") as answer_file:
        # reading file line by line
    # читання файлу рядок за рядком
        answerCorrect = 0
        for line in my_file:
            # print line with question
            # друкувати рядок із запитанням
            print(f"question: {line.strip()}")
            # print 3 lines with answers (because we know that there are 3 lines with answers always)
            # надрукувати 3 рядки з відповідями (адже ми знаємо, що завжди є 3 рядки з відповідями)
            for _ in range(3):
                print(f"option {my_file.readline().strip()}")
            # parse correct answer from the next line and convert to int
            # проаналізуйте правильну відповідь із наступного рядка та перетворіть на int
            answer = int(my_file.readline().split(":")[1].strip())

            user_answer = input("\nPlease, input your number and press Enter: ")
            # TODO: handle exceptions
        
            # TODO: обробляти винятки
            try:
                user_answer = int(user_answer.strip())
            except ValueError:
                print('не правильна відповідь')


            # TODO: add logic - check if answer is correct
            # TODO: додайте логіку - перевірте правильність відповіді
            if user_answer == answer:
                answer_file.write(f"answer {answer} is CORRECT\n")
                print('Corrcet')
                answerCorrect += 1
            else:
                answer_file.write(f"answer {answer} is WRONG\n")
                print('Wrong')
print(f'you have {answerCorrect} comn. answer')

