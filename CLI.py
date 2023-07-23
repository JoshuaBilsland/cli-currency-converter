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
            elif userInput == "currencies":
                self.__currencies()
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
        print("commands - Display the list of supported commands")
        print("currencies - View full list of available currencies")
        print("history - Display previous conversions")
        print("exit - Exit the program")
        print("\nUse 'help <command>' to get more information about a specific command")        
        
    
    # Display the currencies supported by CurrencyFreaks API
    def __currencies(self):
        try:
            response = self.__APIConnector.getCurrencyCodesAndNames()    
            currenciesJson = response.json()
    
        except response.exceptions.RequestException as e:
            print(f"API request error: {e}")
        
        else:
            self.__printCurrenciesList(currenciesJson)
            
    
    # Take the JSON returned and print the data it contains to show the available currencies
    def __printCurrenciesList(self, jsonData):
        data = jsonData['currencySymbols']

        # Print out in alphabetical order by the full name of the currency
        for value in sorted(data.values()):
            for symbol, fullName in data.items():
                if fullName == value:
                    print(f"{symbol}-{fullName}")
        
        
if __name__ == "__main__":
    commandLineInterface = CommandLineInterface()