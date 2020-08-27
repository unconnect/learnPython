import pythonNumbersStrings as pns
import pythonControlFlow as pcf

# Run main
if __name__ == '__main__':
    # Numbers and Strings
    pns.print_hi_and_age('Alex', 1979,12,7)
    # Raw string stuff
    pns.print_string_stuff()
    pns.print_lists()

    # Controlflow with input
    # pcf.fun_with_controlflow()

    # Fun with Loops
    pcf.fun_with_loops()
    pcf.sqr(4)
    print('Faculty of 5 is', pcf.fac(5))

    # Point other name to Function fac()
    f = pcf.fac
    print('Faculty of 12 is', f(12))

    # fac procedure to print the faculty
    pcf.print_fac(6)

    # Prompt user, example of default arguments
    # pcf.ask_ok('Do you really wanna quit? ')

    # Order of evaluation
    print(pcf.f_eval_sequence(1))
    print(pcf.f_eval_sequence(2))
    print(pcf.f_eval_sequence(3))

    print(pcf.f_eval_sequence2(1))
    print(pcf.f_eval_sequence2(2))
    print(pcf.f_eval_sequence2(3))

    # Procedure receiving: keyword, *tupel, **dictionary
    # It is also possible to give a packed argument list or tupel
    # which is unpacked with the * operator
    args = ['Really I do!', 'Is this valid?', 'It seems so ...']
    pcf.cheeseshop('Parmesan',
                   'I love parmesan!', *args,
                   shopowner='Alex Shopowner',
                   customer='Max the super customer',
                   receipe='Shopping receipe')

    # Lambdas
    # Sorting by second value of the tupel,
    # with the help of a lambda function
    pairs = [(1, 'z'), (2, 'e'), (3, 'r'), (4, 'u')]
    pairs.sort(key=lambda pair: pair[1], reverse=1)
    print(pairs)
