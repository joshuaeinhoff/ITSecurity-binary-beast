import tkinter as tk
import time

window = tk.Tk()
photo = tk.PhotoImage(file = 'assets/xorIcon.png')
window.wm_iconphoto(False, photo)
# width= window.winfo_screenwidth() 
# height= window.winfo_screenheight()
#window.geometry('1000x500')
window.title('XorVizualization')
font = 'JetBrains Mono'
fontSize = 16

xorString = '' 


def binaryTransform(word):
    # there is an issue with the bit conversion -> losing the first bit
    # binary for a = 01100001 -> our output= 1100001
    byte = word.encode()
    binary_int= int.from_bytes(byte,"big")
    binary_string = bin(binary_int)
    # removing '0b' at beginning of String and adding 0 because of the before mentioned problem
    returnString = str(0)+binary_string[2:]
    return returnString


def binaryReadabilityHelper(word):
    # add space after each 8 bits
    returnString = ' '.join([word[i:i+8] for i in range(0, len(word), 8)])
    return returnString


def confirmInput(): 
    global xorString
    inp1 = input_variable1.get() 
    inp2 = input_variable2.get()
    if(inp1 != ''): out1 = binaryReadabilityHelper(binaryTransform(inp1))
    if(inp2 != ''): out2 = binaryReadabilityHelper(binaryTransform(inp2))
    plaintext.config(text=out2)
    xorString = animateXor(out1,out2)
 

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
    # print(f'Before: {beforeIndex}')
    # print(f'At: {atIndex}')
    # print(f'After: {afterIndex}')

    labels[0].config(text=beforeIndex)
    labels[1].config(text=atIndex, fg="#00ff00")
    labels[2].config(text=afterIndex)


def displayNormal(labels, word):
    labels[0].config(text=word)
    labels[1].config(text='')
    labels[2].config(text='')


def animateXor(word1,word2):
    result = ''
    if(len(word1) == len(word2)):
        for i in range(0,len(word1)):
            if (word1[i] != ' ' and word2[i] != ' '):
                highlightCharacter(labelLine0, word1, i)
                highlightCharacter(labelLine1, word2, i)
                result += showCalculation(word1[i], word2[i],outputCalculation)
                showResult(outputXor,result)
                window.update()
                time.sleep(0.500)
        displayNormal(labelLine0, word1)
        displayNormal(labelLine1, word2)
        window.update()
    return result

def showCalculation(a, b, label):
    xor = int(a)^int(b)
    out = f'{a} ^ {b} = {xor}'
    label.config(text=out)
    return str(xor)

def showResult(label, result):
    label.config(text=binaryReadabilityHelper(result))


def recoverPlain():
    global xorString
    inp2 = input_variable2.get()
    if(xorString != ''):
        if(inp2 != ''): out2 = binaryReadabilityHelper(binaryTransform(inp2))
        xorString = animateXor(binaryReadabilityHelper(xorString),out2)


# -------- Input Section --------
input_variable1 = tk.StringVar()
input_variable2 = tk.StringVar()
tk.Label(window, text='Plaintext').grid(column=0, row=0, pady='5', padx='5')
tk.Label(window, text='Initialization Vector').grid(column=0, row=1, pady='5', padx='5')
input1 = tk.Entry(window, textvariable=input_variable1)
input2 = tk.Entry(window, textvariable=input_variable2)
input1.grid(column=1, row=0,padx=10)
input2.grid(column=1, row=1, padx=10)
# -------- Input Section --------


# -------- Button Section --------
confirmButton = tk.Button(window, 
                        text = "Confirm",  
                        command = confirmInput) 
confirmButton.grid(column=5, row=5)

reXorButton = tk.Button(window,
                        text="Recover Plaintext",
                        command= recoverPlain)
reXorButton.grid(column=5, row=6)
# -------- Button Section --------

# -------- Plaintext label --------
plaintext = tk.Label(window, font=(font,12))
plaintext.grid(column=5,row=0)

# -------- Labelline 1 --------
outputLabel0 = tk.Label(window, padx=0,font=(font,fontSize))
outputLabel0.grid(column=2, row=2)
outputLabel1 = tk.Label(window, padx=0, font=(font,fontSize))
outputLabel1.grid(column=3, row=2)
outputLabel2 = tk.Label(window, padx=0, font=(font,fontSize))
outputLabel2.grid(column=4, row=2)
labelLine0 = [outputLabel0,outputLabel1,outputLabel2]
# -------- Labelline 1 --------


# -------- Labelline 2 --------
outputLabel3 = tk.Label(window, padx=0, font=(font,fontSize))
outputLabel3.grid(column=2, row=3)
outputLabel4 = tk.Label(window, padx=0, font=(font,fontSize))
outputLabel4.grid(column=3, row=3)
outputLabel5 = tk.Label(window, padx=0, font=(font,fontSize))
outputLabel5.grid(column=4, row=3)
labelLine1 = [outputLabel3,outputLabel4,outputLabel5]
# -------- Labelline 2 --------

# -------- Calculation --------
outputCalculation = tk.Label(window, font=(font, fontSize))
outputCalculation.grid(column=2, row=4)
# -------- Calculation --------

# -------- Result --------
outputXor = tk.Label(window, font=(font,fontSize))
outputXor.grid(column=2, row=5)
# -------- Result --------


window.mainloop()
