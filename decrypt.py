import cv2
# hi this is Rishita

class Decrypt:
    def __init__(self, file):
        try:
            self.image = cv2.imread(file, 1)
            self.b, self.g, self.r = cv2.split(self.image)
        except:
            print("Encrypted file not found!!!")
            return
        self.f = open('output.txt', 'w')
        self.CleanFile()
        self.wordCount = self.FindNumber(0)
        if self.wordCount > self.image.shape[0] - 2:
            print("msg can't be decrypted")
            return
        self.WordSearch()
        self.CleanFile()
        print("\n")

    def WordSearch(self):
        print("Decrypted Text : ", end="")
        for row in range(self.wordCount):
            wordlength = self.FindNumber(row + 1)
            # print(f"{wordlength} {wordlength*8} {self.image.shape[1]}")
            if wordlength * 8 >= self.image.shape[1]:
                print("can't decrypt the file")
                return
            self.FindWords(wordlength, row + 1)

    def CleanFile(self):
        self.f.write("")
        self.f.close()
        self.f = open('output.txt', 'a')

    def FindNumber(self, row=0):
        power_of_2 = 128
        num = 0
        # print(self.g[row, 0:8])
        for i in range(8):
            if self.g[row, i] % 2 == 1:
                num += power_of_2
            power_of_2 //= 2
        # print(self.g[row, 0:8])
        # print(f"word count : {num}")
        return num

    def FindWords(self, letter_count, row):
        power_of_2 = 128
        word = ""
        num = 0
        # print(self.r[row, 0:(letter_count * 8)])
        for col in range(letter_count * 8):
            if col % 8 == 0 and not (col == 0):
                power_of_2 = 128
                word += chr(int(num))
                num = 0
            if self.r[row, col] % 2 == 1:
                # print(col)
                num += power_of_2
            power_of_2 //= 2
        word += chr(int(num))
        print(word, end=" ")
        self.f.write(word + " ")
        # self.f.write(word + " ")

    def CloseFile(self):
        self.f.close()
