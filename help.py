def handleHelpCall(userInput):
    inputAsList = userInput.split()
    if len(inputAsList) == 2:
        if inputAsList[0] == "help":
            if inputAsList[1] == "commands":
                return getCommandsHelp()
            elif inputAsList[1] == "currencies":
                return getCurrenciesHelp()
            elif inputAsList[1] == "convert":
                return getConvertHelp()
            elif inputAsList[1] == "history":
                return getHistoryHelp()
            elif inputAsList[1] == "exit":
                return getExitHelp()
            else:
                return f"'{inputAsList[1]}' is not a supported command."
        return f"'{inputAsList[0]}' is not a supported command."
    return f"'{userInput}' is not a supported command."


def getCommandsHelp():
    return """Displays the full list of commands supported by the program.

This command is automatically called when first running the program.
    """
    
    
def getCurrenciesHelp():
    return """Displays the full list of supported currencies from 'ExchangeRate-API' (https://www.exchangerate-api.com/).

This list is displayed in the format of '<code>-<fullName> and is sorted into alphabetical order.
Example: GBP-Pound Sterling

You will need to use these codes when using the 'convert' command to convert between currencies.
    """
    

def getConvertHelp():
    return """Convert an amount of money frome one currency to another. 

Uses the format 'convert <fromCurrency> <toCurrency> <amount>'.
    
The 'fromCurrency' and 'toCurrency' should be given as the code for that currency.
    
Example: convert GBP USD 500
    """


def getHistoryHelp():
    return """Displays all previous conversions that have been made since the program started running.
    """


def getExitHelp():
    return """Stops the program running.
    """