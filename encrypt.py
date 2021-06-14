import cv2


class Encrypt:
    def __init__(self, file):
        try:
            self.img = cv2.imread(file, 1)
            self.b, self.g, self.r = cv2.split(self.img)
        except:
            print("cover image not found")
            return
        try:
            self.f = open('input.txt', 'r')
        except:
            print("Encryption file not found 'input.txt'")
            return
        self.message = self.f.read()
        self.f.close()
        self.message = self.message.split()
        self.wordCount = len(self.message)
        # print(self.img.shape[0])
        if self.wordCount >= 253 and self.img.shape[0] - 3 < self.wordCount:
            print("'msg' is 'too long'")
            return
        self.StoreNumber(self.wordCount, 0)
        row = 1
        for word in self.message:
            # print(len(word))
            if len(word) * 8 >= self.img.shape[1]:
                print("word is too long : " + word)
                return
            self.StoreNumber(len(word), row)
            self.StoreWord(word, row)
            row += 1
        self.SaveFile()

    def StoreNumber(self, num, row):
        # print(f"num : {num}")
        # print(self.g[row, 0:8])
        for i in range(8):
            if num % 2 == 1 and self.g[row, 7 - i] % 2 == 0:
                self.g[row, 7 - i] += 1
            elif num % 2 == 0 and self.g[row, 7 - i] % 2 == 1:
                self.g[row, 7 - i] -= 1
            num //= 2
        # print(self.g[row ,0:8])

    def StoreWord(self, word, row):
        # print(word)
        # print(self.r[col, 0:(len(word) * 8)])
        # print(f"length {len(word)}")
        for index in range(len(word)):
            letter_ascii = ord(word[index])
            col = index * 8 + 7
            for _ in range(8):
                if letter_ascii % 2 == 1 and self.r[row, col] % 2 == 0:
                    self.r[row, col] += 1
                elif letter_ascii % 2 == 0 and self.r[row, col] % 2 == 1:
                    self.r[row, col] -= 1
                letter_ascii //= 2
                col -= 1
        # print(self.r[col, 0:(len(word) * 8)])

    def SaveFile(self):
        self.img = cv2.merge((self.b, self.g, self.r))
        cv2.imwrite("encrypted.png", self.img)
        print("Encrypted file created...")
