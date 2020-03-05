class Menu:
    def __init__(self):
        pass

    def show_menu(self, menu_dict):
        for k, v in menu_dict.items():
            print(k, v)
        print("*"*50)