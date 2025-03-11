import random
import string

MIN_NUM_PROBABILITY: int = 1
MAX_NUM_PROBABILITY: int = 100
CHAR_MAP: dict[str, list[str]] = {
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


def is_import_module() -> bool:
    """Проверяет, ипортирован ли модуль pyperclip."""
    try:
        import pyperclip
    except ModuleNotFoundError:
        print(
            "Модуль `pyperclip` не установлен, "
            "результат leetspeak невозможно скопировать "
            "в буфер обмена"
        )
        return False
    return True


def validate_user_input(msg: str) -> str:
    valid_chars: str = string.ascii_letters + string.digits + " "

    if not msg:
        raise ValueError("Необходимо ввести сообщение!\n")
    elif any(i not in valid_chars for i in msg):
        raise ValueError(
            "Необходимо ввести текст, состоящий "
            "только из английского алфавита и цифр.\n"
        )

    return msg


def get_user_input() -> str:
    """Принимает ввод от пользователя."""
    while True:
        try:
            msg: str = input("Введите ваше сообщение `leet`: ")
            validate_user_input(msg)
        except ValueError as err:
            print(err)
        else:
            return msg


def validate_probability(num: int) -> int:
    if not (MIN_NUM_PROBABILITY <= num <= MAX_NUM_PROBABILITY):
        raise ValueError(
            "Число должно быть в диапазоне "
            f"от {MIN_NUM_PROBABILITY} "
            f"до {MAX_NUM_PROBABILITY}!"
        )

    return num


def get_user_probability() -> int:
    try:
        num = int(
            input(
                "Укажите вероятность замены символа "
                "(введите целое число "
                f"от {MIN_NUM_PROBABILITY} "
                f"до {MAX_NUM_PROBABILITY}): "
            )
        )
    except ValueError:
        raise ValueError("Нужно ввести целое число!")

    return num


def get_probability() -> float:
    while True:
        try:
            probability_to_replace: int = get_user_probability()
            validate_probability(probability_to_replace)
        except ValueError as err:
            print(err)
        else:
            return probability_to_replace / 100


def convert_to_leetspeak(msg: str, probability: float) -> str:
    leetspeak: str = ""
    for curr_char in msg:
        # Вероятность того, что мы изменим символ на leetspeak
        if curr_char.lower() in CHAR_MAP and random.random() <= probability:
            leet_chars = CHAR_MAP[curr_char.lower()]
            char = random.choice(leet_chars)
            leetspeak = leetspeak + char
        else:  # Добавляется сам символ.
            leetspeak = leetspeak + curr_char

    return leetspeak


def copy_to_clipboard(text: str) -> None:
    """
    Копирует leet-строку в буфер обмена, если установлен модуль `pyperclip`.
    """
    if is_import_module():
        import pyperclip
        pyperclip.copy(text)
        print("\n[INFO] Результат скопирован в буфер обмена.")


def save_to_file(
        text: str,
        filename: str = "results.txt",
        encoding: str = "UTF-8"
) -> None:
    with open(filename, mode="a", encoding=encoding) as f:
        f.write(f"{text}\n")


def show_source_text(msg: str) -> None:
    ans: str = input(
        "Вы хотите увидеть текст до преобразования "
        "в leet - строку? (да/нет): "
    )

    if ans == "да":
        print(f"\nПервоначальный текст: {msg}")
    else:
        print("Ок. Счастливо.")


def main() -> None:
    text: str = get_user_input()
    probability: float = get_probability()

    res: str = convert_to_leetspeak(text, probability)
    print(res)

    save_to_file(res)
    copy_to_clipboard(res)
    show_source_text(msg=text)


if __name__ == "__main__":
    main()
