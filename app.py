import os
from secret import Configuration
from twilio.rest import Client, TwilioException
from colorama import Fore, init

init(autoreset=True)

class CreateConnection:
    def connect(self):
        """Connect python to Twilio REST API
        
        return:
            boolean: True for success and False for failure
        """
        try:
            print(f"{Fore.LIGHTCYAN_EX}Connecting to Twilio...\r", end="")
            self.__client = Client(Configuration.SID, Configuration.AUTH_TOKEN)
            print(f"{Fore.LIGHTGREEN_EX}Connected Successfully...")
            return 1
        except TwilioException as e:
            print(f"{Fore.LIGHTRED_EX}{str(e)}")
            return 0
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}{str(e)}")
            return 0
            
    def send_message(self, message: str, to: str = Configuration.RECEIVER, subject: str = "Update For Novel"):
        """Sends message to the user from parameter<to>

        Args:
            message (str): Text Message which is to be sent to receiver
            to (str, optional): Verified Phone number (for trial account) otherwise regular phone number of receiver. 
                Defaults to Configuration.RECEIVER.
        return:
            boolean: True for success and False for failure
        """
        print(f"{Fore.LIGHTCYAN_EX}Sending message to {to}\r", end="")
        try:
            message = self.__client.messages.create(
                body=subject + "\n" + message,
                from_=Configuration.PHONE,
                to=to,
            )
            if message.status:
                print(f"{Fore.LIGHTGREEN_EX}Message has been sent successfully to {to}")
                print(f"{Fore.LIGHTBLUE_EX}SID {message.sid}")
                return 1
            print(f"{Fore.LIGHTRED_EX}Sending message to {to} failed", end="")
            return 0
        except TwilioException as e:
            print(f"{Fore.LIGHTRED_EX}{str(e)}")
            return 0
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}{str(e)}")
            return 0

if __name__ == "__main__":
    app = CreateConnection()
    if app.connect():
        app.send_message("Hello, There")