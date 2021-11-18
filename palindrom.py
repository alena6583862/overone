def palindrom(word) -> str:


    if word == word[::-1]:
        print("Это слово является палиндромом ")
    else:
        print("Это слово не палиндром")

palindrom(word = input("Напиши любое слово: "))
