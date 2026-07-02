def CheckVowel(val):
    VowelLits = ["a","e","i","o","u","A","E","I","O","U"]
    if val in VowelLits:
        return True
    else:
        return False
    
def main():
    text = input("Enter the charactor: ")
    ret = CheckVowel(text)
    if ret == True:
        print("Its a Vowel")
    else:
        print("Not Vowel")
        
if __name__ == "__main__":
    main()