import tkinter as tk

window = tk.Tk()
photo = tk.PhotoImage(file = 'assets/xorIcon.png')
window.wm_iconphoto(False, photo)
# width= window.winfo_screenwidth() 
# height= window.winfo_screenheight()
window.geometry('1000x500')
window.title('XorVizualization')

input_variable1 = tk.StringVar()
input_variable2 = tk.StringVar()

tk.Label(window, text='Plaintext').grid(row=0, column = 0, pady='5', padx='5')
tk.Label(window, text='Initialization Vector').grid(row=0, column = 2, pady='5', padx='5')
input1 = tk.Entry(window, textvariable=input_variable1)
input2 = tk.Entry(window, textvariable=input_variable2)
input1.grid(row=1, column=0, padx=10)
input2.grid(row=1, column=2, padx=10)

wordTransormed = ''

def binaryTransform(word):
    # there is an issue with the bit conversion -> losing the first bit
    # binary for a = 01100001 -> our output= 01100001
    byte = word.encode()
    binary_int= int.from_bytes(byte,"big")
    binary_string = bin(binary_int)
    return binary_string


def binaryReadabilityHelper(word):
    # remove first two characters (0b)
    returnString = word[2:]
    returnString = ' '.join([returnString[i:i+8] for i in range(0, len(returnString), 8)])
    return returnString

def displayOutput(word1, word2):
    output1.delete('1.0', tk.END)
    output2.delete('1.0', tk.END)
    output1.insert('1.0', word1)
    output2.insert('1.0', word2)


def confirmInput(): 
    inp1 = input_variable1.get() 
    inp2 = input_variable2.get()
    if(inp1 != ''): out1 = binaryReadabilityHelper(binaryTransform(inp1))
    if(inp2 != ''): out2 = binaryReadabilityHelper(binaryTransform(inp2))
    displayOutput(out1, out2)
    #displayXor(binaryXor(binaryTransform(inp1), binaryTransform(inp2)))
 
def binaryXor(word1, word2):
    #remove the 0b in front
    word1 = ''+word1[2:]
    word2 = ''+word2[2:]
    #loop through word and xor each of the binary values
    if(len(word1) == len(word2)):
        word1 = str(word1)
        word2 = str(word2)
        for i in range(0,len(word1)):
            print(f'{i} w1: {int(word1[i])} w2: {int(word2[i])}')
        


def displayXor(word):
    outputXor.delete('1.0', tk.END)
    outputXor.insert('1.0', word)


# Button Creation 
confirmButton = tk.Button(window, 
                        text = "Confirm",  
                        command = confirmInput) 
confirmButton.grid(row=3, column=1)
  
# Label Creation 
output1 = tk.Text(window, height=3)
output1.grid(row=4, column=1)

output2 = tk.Text(window, height=3)
output2.grid(row=5, column=1)

outputXor = tk.Text(window, height=3)
outputXor.grid(row=7, column=1)
window.mainloop()
