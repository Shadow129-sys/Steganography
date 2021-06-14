import encrypt
import decrypt

if __name__ == '__main__':
    print("e - encryption\nd - decryption")
    choice = input("Choice : ")
    print("processing started.....")
    if choice == 'e' or choice == 'E':
        file = input("coverfile : ")
        ob = encrypt.Encrypt(file)
        # print("Encrypted file created...")
    elif choice == 'd' or choice == 'D':
        file = input("encrypted file : ")
        ob1 = decrypt.Decrypt(file)
        # print("Decrypted file created...")
    else:
        print("Wrong Choice")
    print("process ended...")
