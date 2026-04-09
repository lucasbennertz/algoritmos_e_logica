idade = int(input("Digite a idade do nadador: "))
match idade:
    case idade if idade < 5:
        print("O nadador não pode competir.")
    case idade if idade >= 5 and idade <= 7:
        print("O nadador está na categoria Infantil A.")
    case idade if idade >= 8 and idade <= 10:
        print("O nadador está na categoria Infantil B.")
    case idade if idade >= 11 and idade <= 13:
        print("O nadador está na categoria Juvenil A.")
    case idade if idade >= 14 and idade <= 17:
        print("O nadador está na categoria Juvenil B.")
    case _:
        print("O nadador está na categoria Sênior.")