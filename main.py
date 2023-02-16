from utility import print_options
from insz import generate_insz
from bis import generate_bis

if __name__ == "__main__":

    selected_option = 0

    while True:
        print_options()
        selected_option = input('Your selected option:')

        if selected_option == '1':
            generate_bis()
            break
        elif selected_option == '2':
            generate_insz()
            break
        elif selected_option == '3':
            print('Thank you for using this console app')
            break
        else:
            print('Invalid input. Please try again')
