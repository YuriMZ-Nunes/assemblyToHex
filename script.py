import tkinter as tk
from tkinter import messagebox

map_instruction_format_3 = {
    'LDA': '000000',
    'LDB': '011010',
    'LDL': '001000',
    'LDS': '011011',
    'LDT': '011101',
    'LDX': '000100',
    'STA': '001100',
    'ADD': '011000',
    'SUB': '011100',
    'MUL': '100000',
    'DIV': '100100',
    'AND': '010000',
    'OR': '010001',
    'J': '111100',
    'JEQ': '110000',
    'JGT': '110100',
    'JLT': '111000',
    'JSUB': '010010',
    'RSUB': '010011',
    'HLT': '111111',
    'COMP': '101000',
    'STB': '011110',
    'STL': '010100',
    'STS': '011111',
    'STT': '100001',
    'STX': '010000',
    'TIX': '001011',
    'ADDR': '10010000',
    'CLEAR': '00000100',
    'COMPR': '10100000',
    'DIVR': '10011100',
    'MULTR': '10011000',
    'RMO': '10101100',
    'SHIFTL': '10100100',
    'SHIFTR': '10101000',
    'SUBR': '10010100',
    'TIXR': '10111000',
}

flag_mapping = {
    'FLAG 1': '110000',
    'FLAG 2': '110001',
    'FLAG 3': '110010',
    'FLAG 4': '110100',
    'FLAG 5': '111000',
    'FLAG 6': '111001',
    'FLAG 7': '111010',
    'FLAG 8': '111100',
    'FLAG 9': '100000',
    'FLAG 10': '100001',
    'FLAG 11': '100010',
    'FLAG 12': '100100',
    'FLAG 13': '010000',
    'FLAG 14': '010001',
    'FLAG 15': '010010',
    'FLAG 16': '010100',
}

registers_map = {
    'A': '0000',
    'X': '0001',
    'L': '0010',
    'B': '0011',
    'S': '0100',
    'T': '0101',
    'PC': '1000',
    'SW': '1001'
}

def popUp(message):
    root = tk.Tk()
    root.withdraw()
    
    messagebox.showinfo("Concluido", message)

def getInstruction(instruction):
    return map_instruction_format_3.get(instruction, "Instrução não encontrada")

def getFlag(flag):
    return flag_mapping.get(flag, "Flag não encontrada.")

def getRegister(register):
    return registers_map.get(register, "Registrador não encontrado")

def generateBin(value, numBits):
        return bin(value)[2:].zfill(numBits)[-numBits:]

def processLine(line):
    
    try:
        instruction, value, _, flag, format = line.strip().split()
    except:
        instruction, r1, r2 = line.strip().split()
        format = "2"

    binCount = 0
    
    if format == "4":
        binCount = 20
    elif format == "3":
        binCount = 12
    else: 
        binCount = 8
    opCodeBin = getInstruction(instruction)
    
    if format == "4" or format == "3":
        flagBin = getFlag(f'FLAG {flag}')
        binValue = generateBin(int(value), binCount)
        completBin = f'{opCodeBin}{flagBin}{binValue}'
    else:
        r1bin = getRegister(r1)
        r2bin = getRegister(r2)
        completBin = f'{opCodeBin}{r1bin}{r2bin}'
    
    
    decimal = int(completBin, 2)
    hexa = hex(decimal)[2:]
    
    return hexa.upper() + '\n'
    
def getArchive(filePathIn, filePathOut):
    with open(filePathIn, 'r') as fileIn:
        lines = fileIn.readlines()
    
    with open(filePathOut, 'w') as fileOut:
        for line in lines:
            fileOut.write(processLine(line))
        fileOut.write("9900")
    print("finish")

filePathIn = 'assembly.txt'
filePathOut = 'program.txt'

getArchive(filePathIn, filePathOut)

popUp("Arquivo gerado!")