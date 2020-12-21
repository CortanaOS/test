from Crypto.Cipher import DES3

import base64

import json

BS = DES3.block_size

def pad(s):

    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def unpad(s):

    return s[0:-ord(s[-1])]

class prpcrypt():

    def __init__(self, key):

        self.key = key

        self.mode = DES3.MODE_ECB

    def encrypt(self, text):

        text = pad(text)

        cryptor = DES3.new(self.key, self.mode)

        x = len(text) % 8

        if x != 0:

            text = text + '\0' * (8 - x)

        text=text.encode("utf-8")

        self.ciphertext = cryptor.encrypt(text)

        return base64.standard_b64encode(self.ciphertext).decode("utf-8")

    def decrypt(self, text):

        cryptor = DES3.new(self.key, self.mode

        de_text = base64.standard_b64decode(text)

        plain_text = cryptor.decrypt(de_text)

        st = str(plain_text.decode("utf-8")).rstrip('\0')

        out = unpad(st)
        return out

code = json.dumps(text)  //加密的内容

key = "L!$G}Dn7E9Z=]'cU_4~c{f!F"  //盐

print(prpcrypt(key).encrypt(code))
import pyDes 

import base64 

from Crypto.Cipher import DES3 

import codecs 

import base64 

class EncryptDate: 

      def __init__(self, key): 

            self.key = key # 初始化密钥 

            self.length = DES3.block_size # 初始化数据块大小 

            self.des3 = DES3.new(self.key, DES3.MODE_ECB) # 初始化AES,CBC模式的实例 # 截断函数，去除填充的字符 

            self.unpad = lambda date: date[0:-ord(date[-1])] 

      

      def pad(self, text): 

            """ 

            #填充函数，使被加密数据的字节码长度是block_size的整数倍 

            """ 

            count = len(text.encode('utf-8')) 

            add = self.length - (count % self.length) 

            entext = text + (chr(add) * add) 

            return entext 

            

      def encrypt(self, encrData): # 加密函数 

            res = self.des3.encrypt(self.pad(encrData).encode("utf8")) 

            msg = str(base64.b64encode(res), encoding="utf8") 

            # msg = res.hex() 

            return msg 

            

      def decrypt(self, decrData): # 解密函数 

            res = base64.decodebytes(decrData.encode("utf8")) 

            # res = bytes.fromhex(decrData) 

            msg = self.des3.decrypt(res).decode("utf8") 

            return self.unpad(msg) 

            

eg = EncryptDate("L!$G}Dn7E9Z=]'cU_4~c{f!F") # 这里密钥的长度必须是16的倍数 

res = eg.encrypt("13918238353") 

print(res) 

eg1 = EncryptDate("L!$G}Dn7E9Z=]'cU_4~c{f!F") 

print(eg1.decrypt(res))
