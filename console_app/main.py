from common.utility import print_options
from common.insz import generate_insz, decode_insz
from common.bis import generate_bis

if __name__ == "__main__":

    selected_option = 0

    while True:
        print_options()
        selected_option = input('Your selected option:')

        if selected_option == '1':
            generate_bis()

        elif selected_option == '2':
            generate_insz()

        elif selected_option == '3':
            decode_insz()

        elif selected_option == '4':
            print('Thank you for using this console app')
            break
        else:
            print('Invalid input. Please try again')
