import random
import string


def is_import_module() -> bool:
    """ Проверяет, ипортирован ли модуль pyperclip. """
    try:
        import pyperclip
    except ModuleNotFoundError:
        print(f'Модуль `pyperclip` не установлен')
        return False
    return True


# TODO: Декомпозировать функцию
def get_user_input() -> str:
    """ Принимает ввод от пользователя. """
    eng_letters_n_digits: str = string.ascii_letters + string.digits + ' '
    while True:
        msg: str = input('Введите ваше сообщение `leet`: ')

        # TODO: Написать валидатор(ы)
        if not msg:
            print('Необходимо ввести сообщение!\n')
            continue
        elif any(i not in eng_letters_n_digits for i in msg):
            print('Необходимо ввести текст, состоящий только из английского алфавита и цифр.\n')
            continue

        return msg


def get_probability() -> float:
    while True:
        try:
            probability_of_replacing_char_temp: int = int(
                input("Укажите вероятность замены символа (введите целое число от 1 до 100): "))
        except ValueError:
            print('Необходимо ввести число! Не строку.')
            continue
        else:
            # TODO: Написать валидатор
            # TODO: Антипаттерн: Магические числа в коде
            if not (1 <= probability_of_replacing_char_temp <= 100):
                print('Число должны быть в диапазоне от 1 до 100!')
                continue
            probability_of_replacing_char: float = probability_of_replacing_char_temp / 100

            return probability_of_replacing_char


def msg_to_leet(msg, probability) -> str:
    char_mapping = {
        "a": ["4", "@", "/-\\"],
        "b": ["8", "|:"],
        "c": ["(", "["],
        "d": ["|)"],
        "e": ["3"],
        "f": ["ph"],
        "g": ["9"],
        "h": ["]-[", "|-|"],
        "i": ["1", "!", "|"],
        "j": ["_|"],
        "k": ["]<"],
        "l": ["|_"],
        "m": ["^^", "|\\/|", "(V)", "/^^\\"],
        "o": ["0"],
        "p": ["|*"],
        "q": ["()_", "0."],
        "r": ["2", "Я"],
        "s": ["$", "5"],
        "t": ["7", "+"],
        "u": ["|_|"],
        "v": ["\\/"],
        "w": ["\\/\\/", "\\X/", "vv"],
        "x": ["><", "Ж", "}{"],
        "y": ["7"],
        "z": ["2"],

    }

    leetspeak = ""
    for char in msg:
        # Вероятность того, что мы изменим символ на leetspeak
        if char.lower() in char_mapping and random.random() <= probability:
            possible_leet_char_replacement = char_mapping[char.lower()]
            leet_replacement = random.choice(possible_leet_char_replacement)
            leetspeak = leetspeak + leet_replacement
        else:  # Добавляется сам символ.
            leetspeak = leetspeak + char

    return leetspeak


def copy_to_clipboard(text) -> None:
    """ Копирует leet-строку в буфер обмена. """
    import pyperclip
    print()
    pyperclip.copy(text)
    print("[INFO] Результат скопирован в буфер обмена.")


# TODO: Можно добавить гибкости к функции.
def save_to_file(text, encoding='UTF-8') -> None:
    with open('results.txt', mode='a', encoding=encoding) as f:
        f.write(f"{text}\n")


def response_to_user_want_see_first(msg) -> None:
    answers = ('да', 'нет')
    ans: str = input('Вы хотите увидеть текст до преобразования в leet - строку? (да / нет): ')
    while ans not in answers:
        ans = input(f"Возможные ответы: {answers}: ")

    if ans == 'да':
        print(f"\nПервоначальный текст: {msg}")
    elif ans == 'нет':
        print('Ок. Счастливо.')


def main() -> None:
    text = get_user_input()
    probability = get_probability()

    res = msg_to_leet(text, probability)
    print(res)
    save_to_file(res)

    if is_import_module():
        copy_to_clipboard(res)

    response_to_user_want_see_first(msg=text)


if __name__ == "__main__":
    main()
