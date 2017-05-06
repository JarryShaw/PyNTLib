# -*- coding: utf-8 -*-

#RSA 加密器
#利用生成的公鑰進行加密操作

class RSAEncrytor():
    def __init__(self, plainText, publicKey, divisorKey, blockSize):
        blockText = self.blockSlice(str(plainText), blockSize)  #對明文進行分塊

        self.cipherText = []
        for block in blockText:     #逐塊加密，並合併得到密文
            self.cipherText.append(self.msgEncryption(block, publicKey, divisorKey))
            '''
            self.cipherText += str(self.msgEncryption(block, publicKey, divisorKey)).rjust(len(str(divisorKey)),'0')
            '''
            #An alternative for the above line of code:
            #self.cipherText += str(self.repetiveSquareModulo(self.convertUnicode2Number(stringText), publicKey, divisorKey)).rjust(len(str(divisorKey)), '0')

    #獲取密文
    def getCipherText(self):
        return self.cipherText

    #明文分塊
    def blockSlice(self, plainText, blockSize):
        blockText = []

        start = 0
        end = blockSize
        while end <= len(plainText):
            blockText.append(plainText[start:end])
            start = end
            end += blockSize
        else:
            if start != len(plainText):
                blockText.append(plainText[start:])

        return blockText

    #明文加密
    def msgEncryption(self, stringText, publicKey, divisorKey):
        numberText = self.convertUnicode2Number(stringText)
        cipherText = self.repetiveSquareModulo(numberText, publicKey, divisorKey)
        print stringText, ' ', cipherText
        return cipherText
    
    #將字串轉化爲數字（Unicode碼）
    def convertUnicode2Number(self, stringText):
        ctr = 0
        numberText = 0
        for letter in stringText:
            #print 'letter is \'%s\'' %letter
            numberText += (ord(unicode(letter))-32) * (96**ctr)
            ctr += 1
            '''
            numberText += str(ord(unicode(letter))-32).rjust(2,'0')
            '''
        print 'numberText=', numberText
        return numberText

    #模重複平方法
    def repetiveSquareModulo(self, base, exponent, divisor):
        get_bin = lambda x: format(x, 'b')  #二進制轉化函數

        exp_bin = get_bin(exponent)         #將指數轉為二進制
        ptr = len(exp_bin) - 1

        a = 1           
        b = base        
        n = exp_bin     
        while ptr >= 0:                         #base ^ exponent ≡ a_k-1 (mod divisor)
            a = a * b**int(n[ptr]) % divisor    #a_i ≡ a_i-1 * b_i ^ n_i (mod divisor)
            b = b**2 % divisor                  #b_i ≡ b_i-1 ^ 2 (mod divisor)
            ptr -= 1

        print 'cipherNumber=', a
        cipherText = self.convertNumber2Unicode(a)

        return cipherText

    #將數字轉化爲字串（Unicode串）
    def convertNumber2Unicode(self, numberText):
        numberList = self.convertNumbericSystem(numberText)
        #print numberList

        stringText = ''
        for number in numberList:
            #print number, ' ', str(unichr(number))
            stringText += str(unichr(number+32))

        #print stringText
        return stringText

    #將願數字展開為96進制的數
    def convertNumbericSystem(self, inputNumber):
        outputNumber = []
        #print 'iN=', inputNumber

        while inputNumber != 0:
            outputNumber.append(inputNumber % 96)
            inputNumber /= 96
        
        #print 'oN=', outputNumber[::-1]
        return outputNumber

if __name__ == '__main__':
    import RSA_Generator

    rsa_keys = RSA_Generator.RSAGenerator()
    (publicKey, divisorKey, blockSize) = rsa_keys.getPublicKey()

    plainText = 'Mathematic Fundation of Information security 20170323 515030910023'
    #plainText = 'Mathmatics'

    rsa_cipher = RSAEncrytor(plainText, publicKey, divisorKey, blockSize)
    cipherText = rsa_cipher.getCipherText()

    print 'The plain text is %s' %plainText
    print 'The cipher text is %s' %"".join(cipherText)
    '''
    cipherTextFile = open("cipherText.txt","w")
    cipherTextFile.write("\n".join(cipherText))
    cipherTextFile.close()
    '''
