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