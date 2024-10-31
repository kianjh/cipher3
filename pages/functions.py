#Frequency Analyser
import pandas as pd
import streamlit as st

def frequency_analyser(text: str):
    if not text:            #Catching out empty inputs
        return pd.DataFrame()
    
    text = text.upper()         #Ensuring all the text is uppercase
    alphabet = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]         #Create a 2d of the alphabet and the frequency

    for i in range(0, len(alphabet[0])):            #Iterate over each character in the alphabet

        alphabet[1][i] = text.count(alphabet[0][i])            #Get the total character count for the character being checked
        alphabet[2][i] = text.count(alphabet[0][i])/len(text)*100         #Get the percentage frequency that it occurs
    
    df = pd.DataFrame(alphabet).T           #Make the table into a dataframe for easier formatting
    df.columns = ["Letter", "Count", "%"]           #Label each column

    return df          #Returns the results

def caesar_translator(key: int, in_text: str):           #Create a function to translate a caesar string
    in_text = in_text.upper()         #Ensuring all the text is uppercase
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']         #Create a string of the alphabet

    out_text = ''         #Create an empty string for the output

    for char in in_text:          #Iterate over the list to decode each character individually 
        if char in alphabet:            #Ensure that the character is in the alphabet

            Pos = alphabet.index(char) + key           #Determine the new Position of the character
            Pos = Pos % 26          #Bring the index back within 26
            out_text += alphabet[Pos]         #Add the character to the output

        else:

            out_text += char          #Add the punctuation back in

    return out_text           #Return the output

def brute_caesar_translator(in_text: str):          #Create a function to brute force a caesar cipher
    if not in_text:         #Catching out empty inputs
        return pd.DataFrame()
    
    in_text = in_text.upper()         #Ensuring all the text is uppercase
    out_text = [[],[]]          #Preparing a 2d list for the output

    for i in range(1, 26):          #Iterate over all possible keys
        out_text[0].append(i)           #Add the key to the list
        out_text[1].append(caesar_translator(i, in_text))           #Use the caesar translator function to work with the current key and add it to the list

    df = pd.DataFrame(out_text).T           #Transform the 2d list into a dataframe
    df.columns = ["Key", "Result"]          #Label each column
    return df           #Return the dataframe