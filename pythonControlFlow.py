def fun_with_controlflow():
    # Input which is converted to int and than stuff is printed based on if statements
    eingabe = int(input('Bitte eine Zahl eingeben: '))
    if eingabe < 0:
        # If eingabe negative set to zero
        eingabe = 0
        print(f'Negative Zahl auf {eingabe} gesetzt')
    elif eingabe == 0:
        print('Eingabe war Null')
    elif eingabe == 42:
        print('Answer to everything!')
    else:
        print('Eingabe war:', eingabe)
    # if elif is substitution for the switch case statement

def fun_with_loops():
    print('Wie viele Buchstaben sind in den Wörtern?')
    woerter = ['Kurz', 'Länger', 'Superlang', 'Extrasupermegalang']
    MAXLEN = len(max(woerter, key=len))
    for wort in woerter:
        wort_len = len(wort)
        print(f'{wort:<{MAXLEN}}{wort_len:>3}')