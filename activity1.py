class UserProfile:
    def __init__(self, user_name, passcode):
        self.user_name = user_name
        self.__passcode = passcode

    def display_info(self):
        print("Logged in as:", self.user_name)
        print("Secure code is stored.")

    def change_code(self, new_code):
        if len(new_code) == 4 and new_code.isdigit():
            self.__passcode = new_code
            print("System: Code successfully modified.")
        else:
            print("Alert: Verification failed. Requirements not met.")

    def verify_passcode(self, code_to_test):
        if code_to_test == self.__passcode:
            print("Access status: Authorized.")
        else:
            print("Access status: Denied.")

    def __str__(self):
        return "User Account: " + self.user_name


user1 = UserProfile("Gaurish", "0000")
print(user1)
user1.display_info()

user1.__passcode = "5555"
print("Testing if I can bypass the privacy and change it directly.")

user1.verify_passcode("5555")
user1.verify_passcode("0000")

user1.change_code("5555")
user1.verify_passcode("5555")

