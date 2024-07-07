import tkinter as tk
import time

window = tk.Tk()
photo = tk.PhotoImage(file = 'assets/xorIcon.png')
window.wm_iconphoto(False, photo)
# width= window.winfo_screenwidth() 
# height= window.winfo_screenheight()
window.geometry('1000x500')
window.title('XorVizualization')


def binaryTransform(word):
    # there is an issue with the bit conversion -> losing the first bit
    # binary for a = 01100001 -> our output= 01100001
    byte = word.encode()
    binary_int= int.from_bytes(byte,"big")
    binary_string = bin(binary_int)
    return binary_string


def binaryReadabilityHelper(word):
    # remove first two characters (0b) add 0 so its accurate to binary number
    returnString = str(0)+word[2:]
    returnString = ' '.join([returnString[i:i+8] for i in range(0, len(returnString), 8)])
    return returnString


def confirmInput(): 
    inp1 = input_variable1.get() 
    inp2 = input_variable2.get()
    if(inp1 != ''): out1 = binaryReadabilityHelper(binaryTransform(inp1))
    if(inp2 != ''): out2 = binaryReadabilityHelper(binaryTransform(inp2))
    animateXor(out1,out2)
 
def binaryXor(word1, word2):
    #loop through word and xor each of the binary values
    if(len(word1) == len(word2)):
        for i in range(0,len(word1)):
            if (word1[i] != ' ' and word2[i] != ' '):
                print(f'{i} w1: {int(word1[i])} w2: {int(word2[i])}')
    else: 
        print('Info: Words have to be the same size. Please try again.')


def highlightCharacter(labels, word, index):

    beforeIndex = word[:index]
    atIndex = word[index]
    afterIndex = word[index+1:]
    print(f'Before: {beforeIndex}')
    print(f'At: {atIndex}')
    print(f'After: {afterIndex}')

    labels[0].config(text=beforeIndex)
    labels[1].config(text=atIndex, fg="#00ff00")
    labels[2].config(text=afterIndex)


def displayNormal(labels, word):
    labels[0].config(text=word)
    labels[1].config(text='')
    labels[2].config(text='')


def animateXor(word1,word2):
    if(len(word1) == len(word2)):
        for i in range(0,len(word1)):
            if (word1[i] != ' ' and word2[i] != ' '):
                highlightCharacter(labelLine0, word1, i)
                highlightCharacter(labelLine1, word2, i)
                window.update()
                time.sleep(0.500)
        displayNormal(labelLine0, word1)
        displayNormal(labelLine1, word2)
        window.update()




input_variable1 = tk.StringVar()
input_variable2 = tk.StringVar()

tk.Label(window, text='Plaintext').grid(row=0, column = 0, pady='5', padx='5')
tk.Label(window, text='Initialization Vector').grid(row=0, column = 4, pady='5', padx='5')
input1 = tk.Entry(window, textvariable=input_variable1)
input2 = tk.Entry(window, textvariable=input_variable2)
input1.grid(row=1, column=0, padx=10)
input2.grid(row=1, column=4, padx=10)



# Button Creation 
confirmButton = tk.Button(window, 
                        text = "Confirm",  
                        command = confirmInput) 
confirmButton.grid(row=1, column=5)


# Label Creation 
outputLabel0 = tk.Label(window, padx=0,font=("JetBrains Mono",16))
outputLabel0.grid(row=5,column=1)
outputLabel1 = tk.Label(window, padx=0, font=("JetBrains Mono",16))
outputLabel1.grid(row=5,column=2)
outputLabel2 = tk.Label(window, padx=0, font=("JetBrains Mono",16))
outputLabel2.grid(row=5,column=3)
labelLine0 = [outputLabel0,outputLabel1,outputLabel2]

outputLabel3 = tk.Label(window, padx=0,font=("JetBrains Mono",16))
outputLabel3.grid(row=6,column=1)
outputLabel4 = tk.Label(window, padx=0, font=("JetBrains Mono",16))
outputLabel4.grid(row=6,column=2)
outputLabel5 = tk.Label(window, padx=0, font=("JetBrains Mono",16))
outputLabel5.grid(row=6,column=3)
labelLine1 = [outputLabel3,outputLabel4,outputLabel5]

outputXorFrame = tk.LabelFrame(window)
outputXor = tk.Label(outputXorFrame, height=3)
outputXorFrame.grid(row=7, column=1)
window.mainloop()
