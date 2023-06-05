temp = 350

match temp:
    case 200:
        print('Valid')
    case 300:
        print('Redirect')
    case 400:
        print('Eroare')
    case _:
        print('Test')