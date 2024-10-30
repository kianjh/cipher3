#Frequency Analyser
import pandas as pd

def frequency_analyser(text: str):
    if not text:
        return pd.DataFrame()
    
    alphabet = [['a','b','c','d','e','f','g','h','i','k','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
                [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]         #Create a 2d of the alphabet and the frequency

    for i in range(0, len(alphabet[0])):            #Iterate over each character in the alphabet

        alphabet[1][i] = text.count(alphabet[0][i])            #Get the total character count for the character being checked
        alphabet[2][i] = text.count(alphabet[0][i])/len(text)*100         #Get the percentage frequency that it occurs
    
    df = pd.DataFrame(alphabet).T
    df.columns = ["Letter", "Count", "%"]

    return df          #Returns the results