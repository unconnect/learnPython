def divider():
    print('-' * 40)


def fun_with_controlflow():
    # Input which is converted to int and than stuff is printed based on
    # if statements
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

    print('Counting to five')
    # Loop sequence from 2 to 10 with 2 steps
    for i in range(2,10,2):
        print(i)
    divider()
    # Interate over indizies in sequence
    users = ['max', 'klaus', 'uschi', 'manu', 'alex']
    print('Loop with in range:')
    for i in range(len(users)):
        print(i, users[i])

    # make list
    new_list = list(range(10))
    print(new_list)
    divider()
    print('Find prime numbers, demonstation of break and'
          ' else of a for loop, which is executed'
          'when no break was found')
    for n in range(2,10):
        # Loop is testing for modulo == 0 in range of n,
        # if it true n is no prime number
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                # breaks the loops and continues with next number
                break
        else:
            # Second loop found no factor and break was not executed
            print(n, 'is a prime number')
    divider()
    for x in range(1,15):
        if x % 2 == 0:
            print(f'{x:>2}', 'is even')
            # Found even number continue in loop with next number
            continue
        print(f'{x:>2}', 'is odd')
    divider()


def sqr(x):
    print(x, 'squared is', x*x)


def fac(x):
    """Return the faculty of the given number. Example of recursion."""
    if x == 1:
        return x
    elif x == 0:
        return 0
    else:
        return x * fac(x-1)


def print_fac(x):
    """Recursive procedure which is printing the faculty."""
    if x == 1:
        print(f'Faculty of {x} is', x)
    else:
        print(f'Faculty of {x} is', x * fac(x-1))


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """Function with default arguments"""
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# Default is shared between subsequent calls
def f_eval_sequence(a, L=[]):
    L.append(a)
    return L


# Default is not shared between subsequent calls
def f_eval_sequence2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# *arguments receives a tupel, **keywords receives a dictionary
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    divider()
    for kw in keywords:
        print(kw, ":", keywords[kw])