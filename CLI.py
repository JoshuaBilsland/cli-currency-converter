import os

class CommandLineInterface:
    def __init__(self):
        previousConversions = []
        self.__displayProgramBanner()
        
        
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