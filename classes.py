class __main__():
    def __init__(self):
        self.is_open = True
        global file
        file = file_management("user.txt")

    def user_confirmation(self, user_prompt, default_value):
        try:
            self.confirmation = str(input(user_prompt))
            if self.confirmation.lower()[0] == "y":
                return not default_value
            else:
                return default_value
        except ValueError:
            self.confirmation = default_value
        except IndexError:
            self.confirmation = default_value


    def show_menu(self):
        print("Menu: \n 1 to Printe Users\n 2 to Create New User\n 0 to Close")
        self.option = input("\n")
        self.show_submenu()

    def show_submenu(self):
        try:
            self.option = int(self.option)
        except ValueError:
            return

        if self.option == 1:
            self.print_users()
        if self.option == 2:
            self.create_user()
        if self.option == 0:
            self.close_program()

    def print_users(self):   
        file.print_users()

    def create_user(self):
        new_user = create_new_user(file.count_users())
        self.create_report(new_user)
        self.user_confirmation("Would you like to save the user? Y/N: ", False)
        if self.user_confirmation == True:
            file.save_user(new_user)

    def create_report(self, user):
        new_report = new_user_report(user)
        print(new_report.return_user(user))

    def close_program(self):
        self.is_open = False



class file_management:
    def __init__(self, file_name):
        self.file_name = file_name
        self.users = []
        self.line_counter = 0

    def open_file(self, open_mode):    
        self.file = open(self.file_name, open_mode)

    def close_file(self):
        self.file.close()

    def get_users(self):
        self.open_file("r")
        for line in self.file:
            self.users.append(line)
        self.close_file()

    def count_users(self):
        self.open_file("r")
        self.line_counter = 0
        for line in self.file:
            self.line_counter += 1
            line = line
        self.close_file()
        return self.line_counter

    def append_to_file(self, to_append):
        self.open_file("a")
        self.file.write("\n" + str(to_append))
        self.close_file()

    def save_user(self, user):
        self.append_to_file(user.export_user())
        print("User with ID " + str(user.__id__) + " saved")

    def print_users(self):
        self.get_users()
        print('\n\n\n\n\n\n\nUsers:\n' ,' '.join(str(user) for user in self.users) + "\n\n")



class create_new_user:
    def __init__(self, __id__):
        self.__id__ = __id__
        first_name = input("Enter Firstname: ")
        last_name = input("Enter Lastname: ")
        living_address = input("Enter Address: ")
        company_name = input("Enter Company Name: ")
        self.first_name = first_name
        self.last_name = last_name
        self.living_address = living_address
        self.company_name = company_name
        
    def export_user(self):
        return [self.__id__, self.first_name, self.last_name, self.living_address, self. company_name]


class new_user_report:
    def __init__(self, user_object):
        self.report_id = user_object.__id__

    def return_user(self, user_object):
        return "\n\n\n\n\n\nReport-ID: " + str(self.report_id) + "\nFirst Name: " + user_object.first_name + "\nLast Name: " + user_object.last_name + "\nLiving Address: " + user_object.living_address + "\nCompany Name: " + user_object. company_name + "\n"


class create_user_object:
    def __init__(self, __id__, first_name, last_name, living_address, company_name):
        self.__id__ = __id__
        self.first_name = first_name
        self.last_name = last_name
        self.living_address = living_address
        self.company_name = company_name