# -*- coding: utf-8 -*-

#RSA 解密器
#利用生成的私鑰進行解密操作

class RSADecrytor():
    def __init__(self, cipherText, privateKey, divisorKey):
        '''
        blockText = self.blockSlice(str(cipherText), len(str(divisorKey)))  #對密文進行分塊
        '''
        self.plainText = ''
        for block in cipherText:     #逐塊解密，並合併得到明文
            self.plainText += str(self.msgDecryption(block, privateKey, divisorKey))
            
            #An alternative for the above line of code:
            #self.cipherText += str(self.repetiveSquareModulo(self.convertUnicode2Number(stringText), publicKey, divisorKey)).rjust(len(str(divisorKey)), '0')

    #獲取明文
    def getPlainText(self):
        return self.plainText

    '''
    #密文分塊
    def blockSlice(self, cipherText, blockSize):
        blockText = []

        start = 0
        end = blockSize
        while end <= len(cipherText):
            blockText.append(int(cipherText[start:end]))
            start = end
            end += blockSize
        '''     '''
        else:
            if start != len(plainText):
                blockText.append(plainText[start:])
        '''     '''
        #print blockText
        return blockText
    '''

    #密文解密
    def msgDecryption(self, cipherText, privateKey, divisorKey):
        numberText = self.convertUnicode2Number(cipherText)
        plainText = self.repetiveSquareModulo(numberText, privateKey, divisorKey)
        #print cipherText, ' ', numberText
        #print cipherText, ' ', plainText
        return plainText

    #將字串轉化爲數字（Unicode碼）
    def convertUnicode2Number(self, stringText):
        ctr = 0
        numberText = 0
        for letter in stringText:
            numberText += (ord(unicode(letter))-32) * (96**ctr)
            ctr += 1
            '''
            numberText += str(ord(unicode(letter))-32).rjust(2,'0')
            '''
        #print 'cipherNumber=', numberText
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

        #print 'numberText=', a
        plainText = self.convertNumber2Unicode(a)

        return plainText
    
    #將數字轉化爲字串（Unicode串）
    def convertNumber2Unicode(self, numberText):
        numberList = self.convertNumbericSystem(numberText)

        stringText = ''
        for number in numberList:
            #print number, ' ', str(unichr(number))
            stringText += str(unichr(number+32))
        #print stringText

        return stringText

    #將願數字展開為96進制的數
    def convertNumbericSystem(self, inputNumber):
        inNumCache = inputNumber
        outputNumber = []
        #print 'iN=', inputNumber

        while inputNumber != 0:
            outputNumber.append(inputNumber % 96)
            inputNumber /= 96

        if inNumCache <= 9312: 
            outputNumber.append(0)

        #print 'oN=', outputNumber[::-1]
        return outputNumber

    '''
    #數字分塊
    def numberSlice(self, numberText):
        numberList = []

        end = None
        start = -2
        while start >= -1 * len(numberText):
            numberList.append(int(numberText[start:end]))
            end = start
            start -= 2
        else:
            if end != -1 * len(numberText):
                numberList.append(int(numberText[:end]))

        print numberList
        return numberList
    '''

if __name__ == '__main__':
    import RSA_Generator
    import RSA_Encryptor

    rsa_keys = RSA_Generator.RSAGenerator()
    (publicKey, divisorKey, blockSize) = rsa_keys.getPublicKey()

    print '-*- Key Generated -*-\n'

    plainText = 'Mathematic Fundation of Information security 20170323 515030910023'
    #plainText = 'Mathematic'

    rsa_cipher = RSA_Encryptor.RSAEncrytor(plainText, publicKey, divisorKey, blockSize)
    cipherText = rsa_cipher.getCipherText()
    #print cipherText

    print '-*- Text Ciphered -*-\n'

    (privateKey, divisorKey) = rsa_keys.getPrivateKey()

    rsa_plain = RSADecrytor(cipherText, privateKey, divisorKey)
    plainText = rsa_plain.getPlainText()

    print 'The original message is %s' %plainText
