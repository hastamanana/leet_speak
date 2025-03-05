import random
import string

# Закомментируйте чтобы протестировать работу программы
# import pyperclip

def is_import_pyperclip() -> bool:
    """ Проверяет, ипортирован ли модуль pyperclip. """
    try:
        __import__('pyperclip')
        return True
    except ModuleNotFoundError:
        print('Модуль `pyperclip` не установлен')
        return False
            

def eng_word_to_leetspeak() -> str:
    eng_letters_n_digits = string.ascii_letters + string.digits + ' '
    """ Преобразует английскую строку в сообщение и возвращает leetspeak. """
    while True:
        global msg 
        msg = input('Введите ваше сообщение `leet`: ')
        if not msg:
            print('Необходимо ввести сообщение!\n')
            continue
        elif any(i not in eng_letters_n_digits for i in msg):
            print('Необходимо ввести текст, состоящий только из английского алфавита и цифр.\n')
            continue
        break

    while True:
        try:
            probability_of_replacing_char_temp: int = int(input("Укажите вероятность замены символа (введите целое число от 1 до 10): "))
        except BaseException:
            print('Необходимо ввести число! Не строку.')
            continue
        else:
            if not (1 <= probability_of_replacing_char_temp <= 10):
                continue
            probability_of_replacing_char: float = probability_of_replacing_char_temp / 10
            print(probability_of_replacing_char)
        break

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
        # Вероятность того, что мы изменим символ на leetspeak, составляет 70%.
        if char.lower() in char_mapping and random.random() <= probability_of_replacing_char:
            possible_leet_char_replacement = char_mapping[char.lower()]
            leet_replacement = random.choice(possible_leet_char_replacement)
            leetspeak = leetspeak + leet_replacement
        else:
        # Не переводите этот символ.
            leetspeak = leetspeak + char
    return leetspeak

def copy_to_clipboard(text) -> None: # None же возвращает?
    """ Копирует leet-строку в буфер обмена. """
    if is_import_pyperclip:
        import pyperclip
        print()
        print("[INFO] Результат скопирован в буфер обмена.")
        return pyperclip.copy(text)
    

def save_leet_msg(text) -> None:
    with open('results.txt', 'a') as f:
        f.write(f"{text}\n")


def do_you_want_to_see_your_first_msg() -> None:
    answers = ('да', 'нет')
    ans: str = input('Вы хотите увидеть текст до преобразования в leet - строку? (да / нет): ')
    while ans not in answers:
        ans = input(f"Возможные ответы: {answers}: ")

    if ans == 'да':
        print()
        print(f"Первоначальный текст: {msg}")
    elif ans == 'нет':
        print('Ок. Счастливо.')


def main() -> None:
    if is_import_pyperclip():
        leetspeak = eng_word_to_leetspeak()
        print(leetspeak)
        save_leet_msg(leetspeak)
        copy_to_clipboard(leetspeak)
        do_you_want_to_see_your_first_msg()

if __name__ == "__main__":
    main()
