def credit_card(cc: str):

    cc = input("Введи номер кредитной карты (16 цифр без пробелов): ")
    b = cc
    for i in range(12):
        b = b.replace(cc[i], '*', 1)
    print(b)

credit_card('cc')



































