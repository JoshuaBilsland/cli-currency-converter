import os
import APIConnector

class CommandLineInterface:
    def __init__(self):
        self.__previousConversions = []
        self.__displayProgramBanner()
        
        os.environ['API_KEY'] = self.__getAPIKey()
        self.__APIConnector = APIConnector.APIConnector(os.environ['API_KEY'])
        
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
        
        
if __name__ == "__main__":
    commandLineInterface = CommandLineInterface()