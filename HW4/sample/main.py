import time
from Crypto.Cipher import AES
import base64

def encrypt_ecb(plaintext, key):
    # 將 key 使用 '\0' 補齊到 16 字節
    key = key.ljust(16, '\0').encode('utf-8')
    
    # 明文使用 ZeroPadding 補足到 16 的倍數
    padded_plaintext = plaintext.ljust(16, '\0').encode('utf-8')
    
    # 建立 AES ECB 加密器
    cipher = AES.new(key, AES.MODE_ECB)
    
    # 加密並進行 Base64 編碼
    encrypted_bytes = cipher.encrypt(padded_plaintext)
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_base64

def decrypt_ecb(encrypted_base64, key):
    # 將 key 使用 '\0' 補齊到 16 字節
    key = key.ljust(16, '\0').encode('utf-8')
    
    # 將密文從 Base64 解碼
    encrypted_bytes = base64.b64decode(encrypted_base64)
    
    # 建立 AES ECB 解密器
    cipher = AES.new(key, AES.MODE_ECB)
    
    # 解密並移除 ZeroPadding
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_text = decrypted_bytes.decode('utf-8').rstrip('\0')
    return decrypted_text

def crack_ECB():
    guess_counter = 0
    for i in range(32, 127):
        for j in range(32, 127):
            for k in range(32, 127):
                for l in range(32, 127):
                    guess_counter += 1
                    key = f"Hj{chr(i)}N){chr(j)}tgZ{chr(k)}9wrc{chr(l)}m"
                    try:
                        return decrypt_ecb(encrypted_text, key), key, guess_counter
                    except UnicodeDecodeError:
                        pass
    return "", "", ""
# 測試範例
# key = "123456789"
# plaintext = "security"

# # 加密
# encrypted_text = encrypt_ecb(plaintext, key)
# print("加密後的密文:", encrypted_text)

encrypted_text = "Wj3RQTGXWvIeIu5nEt2qYuYbHRhoNtJawk07R0oZWnI="
key = ""
decrypted_text = ""

print("黃睿淞 F74124757，密碼破解")
print("密文:", encrypted_text)
print("="*20)   

start_time = time.time()

decrypted_text, correct_key, guess_counter = crack_ECB()
                
end_time = time.time()
    
print("正確金鑰:", correct_key)
print("解密後的明文:", decrypted_text)
print(f"花費時間: {end_time-start_time:.2f}s")
print(f"猜測次數: {guess_counter}/81450625")