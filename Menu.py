class Menu():
    def __init__(self):
        self.menu_home = ['\nWhat would you like to do?\n\n',
                          '1: Abstract contour analysis\n',
                          '2: Melodic interval analysis\n\n']

        self.menu_1 = ['\nSelect an option:\n\n',
                       '1: Analyse one composition\n',
                       '2: Analyse more than one composition\n',
                       '3: Analyse one voice from one composition\n'
                       'Back: Return to previous menu\n']

        self.menu_2 = ['\nSelect an option:\n\n',
                       '1: I know the sequence I want to search for\n',
                       '2: I want to run a blind check for sequences\n',
                       'Back: Return to previous menu']

        self.menu_selections = []
        self.scores = []

        self.begin_menu()

    def begin_menu(self):
        VALID_INPUT_FLAG = False
        while VALID_INPUT_FLAG == False:
            option = input(''.join(self.menu_home))
            if option == '1':
                self.menu_selections.append(option)
                self.menu_one_deep()
                VALID_INPUT_FLAG = True
            elif option == '2':
                self.menu_selections.append(option)
                self.menu_one_deep()
                VALID_INPUT_FLAG = True
            else:
                print('\nInvalid input, use the numbers to select an option')

    def menu_one_deep(self):
        VALID_INPUT_FLAG = False
        while VALID_INPUT_FLAG == False:
            option = input(''.join(self.menu_1))
            if option == '1':
                self.menu_selections.append(option)
                VALID_INPUT_FLAG = True
                score = input('Please enter the name of the file')
                self.scores.append(score)
            elif option == '2':
                self.menu_selections.append(option)
                VALID_INPUT_FLAG = True
            elif option == '3':
                self.menu_selections.append(option)
                VALID_INPUT_FLAG = True
            elif option == 'back':
                self.menu_selections.pop()
                self.begin_menu()
            else:
                print('\nInvalid input, use the numbers to select an option')

    def menu_two_deep(self):
        VALID_INPUT_FLAG = False
        while VALID_INPUT_FLAG == False:
            option = input(''.join(self.menu_2))
            if option == '1':
                self.menu_selections.append(option)
                VALID_INPUT_FLAG = True
            elif option == '2':
                self.menu_selections.append(option)
                VALID_INPUT_FLAG = True
            elif option == '3':
                self.menu_selections.append(option)
                VALID_INPUT_FLAG = True
            elif option == 'back':
                self.menu_selections.pop()
                self.begin_menu()
            else:
                print('\nInvalid input, use the numbers to select an option')
