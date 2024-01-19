def string_upper(value: str) -> str:
    """
    Принимает строку, возвращает строку, где все буквы замены на заглавные
    """
    return value.upper()

def string_capitalize(value: str) -> str:
    """
    Делает заглавными первые буквы каждого слова в строке, поступившей на вход функции.
    """
    words = value.split(' ')
    words_capitalize = []
    for word in words:
        word = word.capitalize()
        words_capitalize.append(word)
    return ' '.join(words_capitalize)

def main():
    user_string = input("Введите строку")
    print(f"Все буквы заглавные: {string_upper(user_string)}")
    print(f"Все слова с заглавной буквы: {string_capitalize(user_string)}")

if __name__ == '__main__':
    main()