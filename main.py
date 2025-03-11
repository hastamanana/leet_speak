import random
import string

MIN_NUM_PROBABILITY: int = 1
MAX_NUM_PROBABILITY: int = 100


def is_import_module() -> bool:
    """ Проверяет, ипортирован ли модуль pyperclip. """
    try:
        import pyperclip
    except ModuleNotFoundError:
        print(f'Модуль `pyperclip` не установлен')
        return False
    return True


def validate_user_input(msg) -> str:
    eng_letters_n_digits: str = string.ascii_letters + string.digits + ' '

    if not msg:
        raise ValueError('Необходимо ввести сообщение!\n') 
    elif any(i not in eng_letters_n_digits for i in msg):
        raise ValueError('Необходимо ввести текст, состоящий только из английского алфавита и цифр.\n')

    return msg


# TODO: Декомпозировать функцию 

def get_user_input() -> str:
    """ Принимает ввод от пользователя. """
    while True:
        try:
            msg: str = input('Введите ваше сообщение `leet`: ')
            validate_user_input(msg)
        except ValueError as err:
            print(err)
        # TODO: Написать валидатор(ы)
        # написал 
        else:
            return msg


def validate_probability(num) -> int:
    if not (MIN_NUM_PROBABILITY <= num <= MAX_NUM_PROBABILITY):
        raise ValueError(f'Число должно быть в диапазоне от {MIN_NUM_PROBABILITY} до {MAX_NUM_PROBABILITY}!')
    
    return num


def get_user_probability() -> int:
    try:
        num = int(input('Укажите вероятность замены символа (введите целое число от 1 до 100): '))
    except ValueError:
        raise ValueError('Нужно ввести число! Не строку!')
    return num


def get_probability() -> float:
    while True:
        try:
            probability_of_replacing_char_temp: int = get_user_probability()
            validate_probability(probability_of_replacing_char_temp)
        except ValueError as err:
            print(err)
        else:
            # TODO: Написать валидатор
            # написал

            # TODO: Антипаттерн: Магические числа в коде
            # написал 2 константы

            return probability_of_replacing_char_temp / 100


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
# напомните, что тут нужно добавить.

def save_to_file(text, filename='results.txt', encoding='UTF-8') -> None:
    with open(filename, mode='a', encoding=encoding) as f:
        f.write(f"{text}\n")


def response_to_user_want_see_first(msg) -> None:
    answers: tuple[str] = ('да', 'нет')
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
