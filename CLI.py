import os
import APIConnector

class CommandLineInterface:
    def __init__(self):
        self.__previousConversions = []
        self.__displayProgramBanner()
        
        os.environ['API_KEY'] = self.__getAPIKey()
        self.__APIConnector = APIConnector.APIConnector(os.environ['API_KEY'])
        
        self.__commands()
        self.__main()
        
        
    # Get the API key from the .config file
    def __getAPIKey(self):
        try:
            with open('.config', 'r') as configFile:
                return configFile.readline()
        except FileNotFoundError:
            print("ERROR: .config file does not exist. See README.MD to fix this issue.")
            exit()
            
                    
    # Display the banner message when launched
    def __displayProgramBanner(self):    
        text = "Currency Converter"
        padding = len(text)//4
        bannerWidth = int(len(text)*1.5)
        
        # Print the top border
        print("=" * bannerWidth)
        
        # Print the text
        print("|" + " " * padding + text + " " * (padding-1) + "|")
        
        # Print the bottom border
        print("=" * bannerWidth)
        
    
    # Main loop
    def __main(self):
        running = True
        while running:
            userInput = self.__getUserInput()
            if userInput == "commands":
                self.__commands()
            elif userInput == "history":
                print()
            elif userInput == "exit":
                running = False
            else:
                print(f"'{userInput}' is not a supported command")
                

    # Allow the user to enter a command
    def __getUserInput(self):
        return input("\n> ")
    

    # Display the list of support commands
    def __commands(self):
        print("Commands List")
        print("-------------")
        print("1. commands - Display the list of supported commands")
        print("2. history - Display previous conversions")
        print("3. exit - Exit the program")
        print("Use 'help <command>' to get more information about a specific command")        
        
        
if __name__ == "__main__":
    commandLineInterface = CommandLineInterface()