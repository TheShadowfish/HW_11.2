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