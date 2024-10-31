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

    return df          #Returns the dataframe

def caesar_translator(key: int, in_text: str):           #Create a function to translate a caesar string
    in_text = in_text.upper()         #Ensuring all the text is uppercase
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']         #Create a string of the alphabet

    out_text = ""         #Create an empty string for the output

    for char in in_text:          #Iterate over the list to decode each character individually 
        if char in alphabet:            #Ensure that the character is in the alphabet

            pos = alphabet.index(char) + key           #Determine the new position of the character
            pos = pos % 26          #Bring the index back within 26
            out_text += alphabet[pos]         #Add the character to the output

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

def encrypt_affine(a: int, b:int, in_text: str):         #Create a function to encrypt, a for the coefficent, b for constant
    if isinstance(in_text, str):
        in_text = in_text.upper()         #Ensuring all the text is uppercase
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']         #Create a string of the alphabet
    out_text = ""         #Create an empty output string

    for char in in_text:          #Iterate over the string
        if char in alphabet:            #Ensure that the character is not punctuation 

            pos = alphabet.index(char)           #Find the position of the character
            pos = (a*pos+b) % 26         #Perform the Affine cypher on the position
            out_text += alphabet[pos]          #Convert back to a character and add to the output

        else:

            out_text += char          #Add punctuation to the output

    return out_text           #Return the output

def decrypt_affine(a: int, b: int, in_text: str):             #Create a function to encrypt, a for the coefficent, b for constant

    in_text = in_text.upper()           #Ensuring all the text is uppercase
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']         #Create a string of the alphabet
    out_text = ""         #Create an empty output string
    encrypted_alph = encrypt_affine(a,b,alphabet)          #Create the encrypted alphabet

    for char in in_text:          #Iterate over the string
        if char in alphabet:            #Ensure that the character is not punctuation

            pos = encrypted_alph.find(char)          #Find the position of the char in the encrypted alphabet
            out_text += alphabet[pos]         #Use the position found to determine the new character to add to the output

        else:

            out_text += char          #Add the punctuation to the output

    return out_text           #Return the output

def encrypt_viginere(key: str, in_text: str):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']         #Create a string of the alphabet
    viginereTable = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A'],
        ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'],
        ['D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C'],
        ['E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D'],
        ['F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E'],
        ['G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F'],
        ['H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
        ['I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        ['K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        ['J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J'],
        ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L'],
        ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M'],
        ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N'],
        ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O'],
        ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P'],
        ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q'],
        ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
        ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'],
        ['U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
        ['V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
        ['W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'],
        ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'],
        ['Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
        ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']]         #The viginere table
    out_text = ""
    in_text = in_text.upper()           #Ensuring all the text is uppercase
    key = key.upper()           #Ensuring the key is uppercase

    for i in range(0, len(in_text)):          #Loop over the input message

        key_pos = i % len(key)           #Find which position of the key we are in now
        row = alphabet.index(key[key_pos])            #Find which row we are in by cross-referencing the letter in the key we are on with the alphabet
        column = alphabet.index(in_text[i])            #Find which column we are in by cross-referencing the letter in the input character we are on with the alphabet
        out_text += viginereTable[row][column]            #Use the row and column in combination with the viginere table to find an output letter and add it to the output
    
    return out_text         #Return the output