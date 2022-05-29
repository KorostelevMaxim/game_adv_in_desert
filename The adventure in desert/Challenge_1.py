def challenge_1(knight_hp_points):
    print("Странник, ты сможешь пройти, если отгадаешь все мои загадки")
    print("Ты готов?")
    print()
    amount_of_answers = 0
    while knight_hp_points > 0 and amount_of_answers != 3:
        print("Тогда 1 загадка.")
        print("Что есть у всех смертных?")
        answer1 = str(input('Ваш ответ: '))
        amount_of_answers = amount_of_answers + 1
        if answer1.title() == "Имя":
            print("Верный ответ")
        else:
            knight_hp_points = knight_hp_points - 1
            print("Сожалею, неверный ответ")
        print("Загадка №2.")
        print("Бежать, бежать - не добежать, лететь, лететь - не долететь")
        answer2 = str(input('Ваш ответ: '))
        amount_of_answers = amount_of_answers + 1
        if answer2.title() == "Горизонт":
            print("Верный ответ")
        else:
            knight_hp_points = knight_hp_points - 1
            print("Сожалею, неверный ответ")
        if knight_hp_points == 0:
            print("Вы стали жертвой коварности могучего сфинкса. Игра окончена")
        else:
            print("Браво. Ну и напоследок загадка №3.")
            print("Сперва блеск, за блеском треск, за треском плеск. ")
            answer3 = str(input('Ваш ответ: '))
            amount_of_answers = amount_of_answers + 1
            if answer3.title() == "Гроза" and knight_hp_points != 0:
                print("Верный ответ")
            else:
                knight_hp_points = knight_hp_points - 1
                print("Сожалею, неверный ответ")
                if knight_hp_points == 0:
                    print("Вы стали жертвой коварности могучего сфинкса. Игра окончена")
    return knight_hp_points



