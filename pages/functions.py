#Frequency Analyser
import pandas as pd

def frequency_analyser(text: str):
    if not text:
        return pd.DataFrame()
    text = text.upper()
    
    alphabet = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]         #Create a 2d of the alphabet and the frequency

    for i in range(0, len(alphabet[0])):            #Iterate over each character in the alphabet

        alphabet[1][i] = text.count(alphabet[0][i])            #Get the total character count for the character being checked
        alphabet[2][i] = text.count(alphabet[0][i])/len(text)*100         #Get the percentage frequency that it occurs
    
    df = pd.DataFrame(alphabet).T           #Make the table into a dataframe for easier formatting
    df.columns = ["Letter", "Count", "%"]           #Label each column

    return df          #Returns the results

def caesar_Translator(key: int, in_text: str):           #Create a function to translate a caesar string, k stands for key, s stands for string, aplh for alphabet
    in_text = in_text.upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']         #Create a string of the alphabet

    out_text = ''         #Create an empty string for the output

    for char in in_text:          #Iterate over the list to decode each character individually 
        if char in alphabet:            #Ensure that the character is in the alphabet

            Pos = alphabet.index(char) + key           #Determine the new Position of the character
            print(Pos)
            Pos = Pos % 26          #Bring the index back within 26
            out_text += alphabet[Pos]         #Add the character to the output

        else:
            out_text += char          #Add the punctuation back in

    return out_text           #Return the output