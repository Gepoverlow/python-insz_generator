from common.utility import print_options
from common.insz import insz_printer, insz_decode_printer
from common.bis import bis_printer

if __name__ == "__main__":

    selected_option = 0

    while True:
        print_options()
        selected_option = input('Your selected option:')

        if selected_option == '1':
            bis_printer()

        elif selected_option == '2':
            insz_printer()

        elif selected_option == '3':
            insz_decode_printer()

        elif selected_option == '4':
            print('Thank you for using this console app')
            break

        else:
            print('Invalid input. Please try again')
