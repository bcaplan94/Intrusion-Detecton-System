#!/usr/bin/python3
"""
Entry point for the program
"""

import time
from statistics import stdev
from lib.pyxhook import HookManager
from lib.keyevent import KeyEvent
from lib.datastore import DataStore


class MainProgram:

    data_store = DataStore()
    previous_event = KeyEvent()
    key_events = []

    def key_log(self, event):
        current_event = KeyEvent()
        if event.Ascii == 13:
            pass
        else:
            current_event.key = event.Key
            current_event.timestamp = time.time()
            self.key_events.append(current_event)

    def start_learning(self):
        # Dump the previous learned data, if applicable.
        self.data_store.data_dict= {}
        tempPass = "password"
        # Create HookManager
        hook = HookManager()
        # Define our callback to fire when a key is pressed down
        hook.KeyDown = self.key_log
        # Hook the keyboard
        hook.HookKeyboard()
        hook.start()
        i = 1
        while i<11:
            # Start the listener
            self.key_events = []
            print("Trial: {0} \t Enter password [again].".format(i))
            # Catch variable for user input while learning. Solves issue with main menu.
            tempPass2 = input()
            """Problem Child below"""
            if tempPass2 == tempPass:
                for j in range(1, self.key_events.__len__()):
                        data = self.key_events[j].log(self.key_events[j-1].key, self.key_events[j-1].timestamp)
                        self.data_store.save(data, i)
                i=i+1
            else:
                print("Password did not match, please redo trial: \n")
        """Commenting out testing
        print(self.data_store.data_dict)"""
        hook.cancel()

    def start_demo(self):

        data_store2 = DataStore()
        data_store2.data_dict = {}
        valid_password = "password"
        sd =0.05
        stdev_learn_array = []
        passed = True

        # Reset Key events
        self.key_events = []

        # Create HookManager
        hook = HookManager()
        # Define our callback to fire when a key is pressed down
        hook.KeyDown = self.key_log
        # Hook the keyboard
        hook.HookKeyboard()
        # Start the HookManager
        hook.start()

        user_input = input("Enter your password: ")
        for j in range(1, self.key_events.__len__()):
            data = self.key_events[j].log(self.key_events[j - 1].key, self.key_events[j - 1].timestamp)
            data_store2.save(data, 1)
        """We are commenting this out because this was just for testing"""
        """print(data_store2.data_dict)"""
        hook.cancel()

        for key in data_store2.data_dict:
            if key in self.data_store.data_dict:
                if data_store2.data_dict[key] > self.data_store.data_dict[key] + sd or data_store2.data_dict[key] < self.data_store.data_dict[key] - sd:
                    passed = False
            else:
                passed = False

        print(passed is True)
        if passed is True and user_input == valid_password:
            print("Passed")
        else:
            print("failed")

    def main(self):

        while True:
            selection = input("""Please select one of the following options:
             \n1. Learn
             \n2. Demo
             \n3. Exit
             """)

            if selection is '1':
                print("You selected the Learn option \n")
                self.start_learning()
            elif selection is '2':
                print("You selected the Demo option \n")
                self.start_demo()
            elif selection is '3':
                quit()
            else:
                print("You did not select a valid option please try again:\n")

if __name__ == "__main__":
    main = MainProgram()
    main.main()
