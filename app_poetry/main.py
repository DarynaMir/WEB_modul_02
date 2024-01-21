from Bot_new import (
    AddBot,
    ExitBot,
    SearchBot,
    EditBot,
    RemoveBot,
    SaveBot,
    LoadBot,
    Congratulate,
    ViewContact,
)
import logging
from my_logger import get_logger

logger = get_logger(__name__)

class ContactAssistant:
    AUTO_SAVE_FILE = "auto_save"

    def __init__(self):
        self.choices = {
            "add": AddBot(),
            "search": SearchBot(),
            "edit": EditBot(),
            "remove": RemoveBot(),
            "save": SaveBot(),
            "load": LoadBot(),
            "congratulate": Congratulate(),
            "view": ViewContact(),
            "exit": ExitBot(),
        }

    def display_commands(self):
        format_str = "{:^20}"
        for command in self.choices:
            print(f"{format_str}{command}")

    def get_bot_instance(self, action):
        if action in self.choices:
            return self.choices[action]
        else:
            logger.error(f"Invalid action: {action}")

    def run(self):
        print("Hello. I am your contact-assistant. What should I do with your contacts?")
        while True:
            action = input("Type help for a list of commands or enter your command\n").strip().lower()

            if not action:
                logger.warning("Please enter a valid action.")
                continue

            if action not in self.choices:
                logger.warning(f"Unrecognized command: {action}")
                continue

            bot_instance = self.get_bot_instance(action)

            try:
                bot_instance.book.load(self.AUTO_SAVE_FILE)
                bot_instance.handle()

                if action in ["add", "remove", "edit"]:
                    bot_instance.book.save(self.AUTO_SAVE_FILE)
            except FileNotFoundError as e:
                logger.error(f"FileNotFoundError: {e}")
                logger.error(f"Error: File '{self.AUTO_SAVE_FILE}' not found.")
            except Exception as e:
                logger.error(f"Exception: {e}", exc_info=True)
                logger.error(f"Error: {e}")

            if action in ["add", "remove", "edit"]:
                try:
                    bot_instance.book.save(self.AUTO_SAVE_FILE)
                except Exception as e:
                    logger.error(f"Exception while saving: {e}", exc_info=True)
                    logger.error(f"Error: {e}")
            elif action == "help":
                self.display_commands()
            elif action == "exit":
                break

if __name__ == "__main__":
    assistant = ContactAssistant()
    assistant.run()