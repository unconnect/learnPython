from datetime import datetime

# Learning Python syntax

# Hello / Hi pycharm extended
# Function gets name und birthday
def print_hi_and_age(name, byear, bmonth, bday):
    # Say hi and calculate age
    # Give me just days and hours
    now = datetime.now()
    birthday = datetime(byear, bmonth, bday)
    age = now - birthday
    print('------')
    print('Hello World with age:')
    print(f'Hi, {name} du bist jetzt {int(age.days / 365)} Jahre oder {age.days} Tage und {int(age.seconds / 3600)} Stunden alt.')

def print_string_stuff():
    # Raw String, when \ should be part of the string
    rawstring = r'c:\this\is\a\windows\path\as\raw\string\see\the\r\at\beginning'
    glueAndRepeat = 3 * 'repeat this three times ' + 'and glue this in the end'
    concatStrings = 'Concat thi' 's two to one string. Works only for two strings. Use + otherwise.'
    print('------')
    print('Some Strings:')
    print(rawstring)
    print(glueAndRepeat)
    print(concatStrings)
    print('------')
    print('Slicing Strings:')
    print('Slice after \"Concat\": ' + concatStrings[0:6])
    print('Get length of String \"concatStrings\": ' + str(len(concatStrings)))
    print('------')
    print('Formatted string output:')
    print('{0}, {1}, {2}'.format('Pos: Null', 'Pos: Eins', 'Pos: Zwei'))
    print('{pos1}, {pos2}, {pos3}'.format(pos1='Position 1', pos2='Position 2', pos3='Position 3'))
    print('Aligning strings:')
    print('{pos1:<40} {pos2:<40} {pos3:>40}'.format(pos1='Position 1', pos2='Position 2', pos3='Position 3'))
    print('{pos1:<40} {pos2:<40} {pos3:>40}'.format(pos1='Content an Pos 1, left aligned', pos2='Content an Pos 2, left aligned', pos3='Content an Pos 3, right aligned'))

def print_lists():
    # List with groceries
    gemüse = ['Karotten', 'Kartoffeln', 'Kohlrabi', 'Salat']
    # Loop through Gemüse and print all with given first letter
    print('------')
    FIRSTLETTER = 'K'
    print(f'Gemüse das mit {FIRSTLETTER}')
    for gm in gemüse:
        if gm[0] == FIRSTLETTER:
            print(gm)

    print('------')
    gemüse.append('Tomaten')
    gemüse.append('Avocado')
    print(gemüse)
    gmlen = len(gemüse)
    print(f'Gemüse-Liste beinhaltet {gmlen} Gemüse')
    print('Print ist in Python nice. Jetzt ist Gemüse länger:', gmlen)
    print('------')


# Run main
if __name__ == '__main__':
    # Expanded "Hello World"
    print_hi_and_age('Alex', 1979,12,7)
    # Raw string stuff
    print_string_stuff()
    print_lists()