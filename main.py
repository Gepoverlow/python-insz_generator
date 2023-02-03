from util import print_options

if __name__ == "__main__":
    selected_option = 0
    while True:
        print_options()
        selected_option = input('Your selected option:')

        if selected_option == '1':
            print('I selected option 1')
        elif selected_option == '2':
            print('I selected option 2')
        elif selected_option == '3':
            print('Thank you for using this console app')
            break
        else:
            print('Invalid input. Please try again')
