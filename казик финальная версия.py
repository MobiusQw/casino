import random

RED = "красное"
BLACK = "черное"
ZERO = "ноль"

BET = [RED, BLACK, ZERO]
PROBABILITIES = [18/37, 18/37, 1/37]

def spin_wheel():
    return random.choices(BET, weights=PROBABILITIES, k=1)[0]

def play_game(*, starting_funds: int, min_bet: int, max_bet: int):
    #starting_funds = int(input('введите свой капитал')) хотелось бы сделать так, чтоб пользователь вводил сам стартовый капритал, но пока хз как сделать
    current_funds = starting_funds
    current_bet = min_bet
    steps = 0

    print(f" Добро пожаловать! \n У тебя на счету: {starting_funds}  \n Ставь на красное, чёрное или ноль. \n Если угадаешь — ставка удваивается. \n Ставку пиши на русском ")
    while current_funds >= min_bet:
        print(f"\n Баланс: {current_funds} \n Текущая ставка: {current_bet} ")

        user_choice = input(" Сделай ставку (красное / черное / ноль): ").strip().lower()
        while user_choice not in BET:
            user_choice = input(" Неверный ввод. Введи: красное, черное или ноль. ").strip().lower()

        current_funds -= current_bet
        result = spin_wheel()
        print(f" Выпало: {result}")

        if user_choice == result:
            if result == ZERO:
                win = current_bet * 36
                print(f"✅Ты угадал(а) 'ноль'! Выигрыш: {win} ")
            else:
                win = current_bet * 2
                print(f" Угадал(а)! Выигрыш: {win} ")
            current_funds += win
            current_bet = min_bet
        else:
            print("❌Не угадал(а). Ставка проиграна.")
            if user_choice != ZERO:
                current_bet *= 2
                if current_bet > max_bet:
                    print(f"⚠️Ставка выше {max_bet}. Возврат к минимальной.")
                    current_bet = min_bet
                if current_bet > current_funds:
                    current_bet = current_funds
            else:
                current_bet = min_bet

        steps += 1

    print("😵Ты проиграл(а) все деньги.")
    print(f" Всего сыграно раундов: {steps}")

play_game(starting_funds=10, min_bet=1, max_bet=4)




