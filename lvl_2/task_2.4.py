# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace('!', '')

print(remove_exclamation_marks("Hi! Hello!"))
print(remove_exclamation_marks(""))
print(remove_exclamation_marks("Oh, no!!!"))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s.endswith("!"):
        return s[:-1]
    return s

print(remove_last_em("Hi!"))
print(remove_last_em("Hi!!!"))
print(remove_last_em("!Hi"))
print(remove_last_em("Hello"))
print(remove_last_em("!!Hello!!"))




# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    result = []
    for word in words:
        if word.count("!") != 1:
            continue
        result.append(word)
    return " ".join(result)

print(remove_word_with_one_em("Hi!"))
print(remove_word_with_one_em("Hi! Hi!"))
print(remove_word_with_one_em("Hi! Hi! Hi!"))
print(remove_word_with_one_em("Hi Hi! Hi!"))
print(remove_word_with_one_em("Hi! !Hi Hi!"))
print(remove_word_with_one_em("Hi! Hi!! Hi!"))
print(remove_word_with_one_em("Hi! !Hi! Hi!"))


