# Hard coded key matrix implementation of the Hill cipher
# Daniel Wandeler CS4920 HW1 Problem 4

import time

matrixKeyRows = 2
matrixKeyColumns = 2
keyMatrix = [[0 for x in range(matrixKeyRows)] for y in range(matrixKeyColumns)]

keyMatrix[0][0] = 9
keyMatrix[0][1] = 4  # |9  4|
keyMatrix[1][0] = 5  # |5  7|
keyMatrix[1][1] = 7

inputString = 'cryptoclassisatthreeoclockbutitisvirtual'
inputLength = len(inputString)
ciphertext = ''
inputArray = [0 for x in range(inputLength)]
outputArray = [0 for x in range(inputLength)]
num = 0
firstMultiplier = 0
secondMultiplier = 0

if __name__ == '__main__':
    # Conversion of plaintext input to an array with numeric values for each character
    for y in range(inputLength):
        if inputString[y] == 'a':
            num = 0
        elif inputString[y] == 'b':
            num = 1
        elif inputString[y] == 'c':
            num = 2
        elif inputString[y] == 'd':
            num = 3
        elif inputString[y] == 'e':
            num = 4
        elif inputString[y] == 'f':
            num = 5
        elif inputString[y] == 'g':
            num = 6
        elif inputString[y] == 'h':
            num = 7
        elif inputString[y] == 'i':
            num = 8
        elif inputString[y] == 'j':
            num = 9
        elif inputString[y] == 'k':
            num = 10
        elif inputString[y] == 'l':
            num = 11
        elif inputString[y] == 'm':
            num = 12
        elif inputString[y] == 'n':
            num = 13
        elif inputString[y] == 'o':
            num = 14
        elif inputString[y] == 'p':
            num = 15
        elif inputString[y] == 'q':
            num = 16
        elif inputString[y] == 'r':
            num = 17
        elif inputString[y] == 's':
            num = 18
        elif inputString[y] == 't':
            num = 19
        elif inputString[y] == 'u':
            num = 20
        elif inputString[y] == 'v':
            num = 21
        elif inputString[y] == 'w':
            num = 22
        elif inputString[y] == 'x':
            num = 23
        elif inputString[y] == 'y':
            num = 24
        elif inputString[y] == 'z':
            num = 25
        else:
            print('Invalid character detected')
        inputArray[y] = num

    x = 0
    y = 0
    for x in range(0,inputLength):
        z = x + 1
        if x % 2 == 0:
        # This code will create a new string of ciphertext by performing matrix multiplication first
        # Secondly, the code will convert the new calculated numbers and convert them back to text
            calculations1 = ((keyMatrix[0][0] * inputArray[x]) + (keyMatrix[0][1] * inputArray[z]))
            calculations2 = ((keyMatrix[1][0] * inputArray[x]) + (keyMatrix[1][1] * inputArray[z]))
            print(keyMatrix[0][0], 'x', inputArray[x], '+', keyMatrix[0][1], '*', inputArray[z], '=', calculations1)
            print(calculations1, '%', 26, '=', calculations1 % 26)
            print(keyMatrix[1][0], 'x', inputArray[x], '+', keyMatrix[1][1], '*', inputArray[z], '=', calculations2)
            print(calculations2, '%', 26, '=', calculations2 % 26, '\n')
            outputArray[x] = calculations1 % 26
            outputArray[z] = calculations2 % 26

    x = 0
    for x in range(inputLength):
        if outputArray[x] == 0:
            ciphertext += 'a'
        elif outputArray[x] == 1:
            ciphertext += 'b'
        elif outputArray[x] == 2:
            ciphertext += 'c'
        elif outputArray[x] == 3:
            ciphertext += 'd'
        elif outputArray[x] == 4:
            ciphertext += 'e'
        elif outputArray[x] == 5:
            ciphertext += 'f'
        elif outputArray[x] == 6:
            ciphertext += 'g'
        elif outputArray[x] == 7:
            ciphertext += 'h'
        elif outputArray[x] == 8:
            ciphertext += 'i'
        elif outputArray[x] == 9:
            ciphertext += 'j'
        elif outputArray[x] == 10:
            ciphertext += 'k'
        elif outputArray[x] == 11:
            ciphertext += 'l'
        elif outputArray[x] == 12:
            ciphertext += 'm'
        elif outputArray[x] == 13:
            ciphertext += 'n'
        elif outputArray[x] == 14:
            ciphertext += 'o'
        elif outputArray[x] == 15:
            ciphertext += 'p'
        elif outputArray[x] == 16:
            ciphertext += 'q'
        elif outputArray[x] == 17:
            ciphertext += 'r'
        elif outputArray[x] == 18:
            ciphertext += 's'
        elif outputArray[x] == 19:
            ciphertext += 't'
        elif outputArray[x] == 20:
            ciphertext += 'u'
        elif outputArray[x] == 21:
            ciphertext += 'v'
        elif outputArray[x] == 22:
            ciphertext += 'w'
        elif outputArray[x] == 23:
            ciphertext += 'x'
        elif outputArray[x] == 24:
            ciphertext += 'y'
        elif outputArray[x] == 25:
            ciphertext += 'z'
        else:
            continue

    print('The original plaintext is:', inputString)
    print('The newly encoded ciphertext is:', ciphertext)
    time.sleep(300) #5 minutes of time to browse before terminal window closes
