from Crypto.Cipher import DES
import binascii

# 翻轉最後一位的位元
def flip_last_bit(data):
    flipped_data = bytearray(data.encode('utf-8'))
    flipped_data[-1] ^= 1  # 翻轉最後一位的 bit
    return flipped_data.decode('utf-8')

# 使用 DES 加密
def des_encrypt(key, plaintext):
    # des = DES.new(key.encode('utf-8'), DES.MODE_ECB) #使用ECB可能會讓key差1位加密後的差異不明顯
    des = DES.new(key.encode('utf-8'), DES.MODE_CBC)
    ciphertext = des.encrypt(plaintext.encode('utf-8'))
    return ciphertext

# 比較兩個加密結果的不同，並以二進位格式顯示差異
def compare_results(result1, result2):
    diff = bin(int.from_bytes(result1, byteorder='big') ^ int.from_bytes(result2, byteorder='big')).count('1')
    return f"bit差異數量: {diff} ({diff/64:.2%})"

# 主函數
def main():
    plaintext1 = input("請輸入明文(8字元): ")
    key1 = input("請輸入金鑰(8字元): ")

    # 確保明文和 key 是 8 bytes
    if len(plaintext1) != 8:
        print("明文長度必須為8字元 (64 bits for DES).")
        return
    if len(key1) != 8:
        print("金鑰長度必須為8字元 (64 bits for DES).")
        return
    
    # 明文最後的位元+1
    plaintext2 = flip_last_bit(plaintext1)  # 明文轉為位元組後翻轉
    # 金鑰最後的位元+1
    key2 = flip_last_bit(key1)  # 保持位元組格式，不轉換回字串
    
    # 原始加密結果
    original_ciphertext = des_encrypt(key1, plaintext1)
    print("原始加密結果: ", binascii.hexlify(original_ciphertext))

    # 明文差 1 bit，加密後結果
    flipped_plaintext_ciphertext = des_encrypt(key1, plaintext2)
    print("明文差 1 bit 結果: ", binascii.hexlify(flipped_plaintext_ciphertext))
    print(compare_results(original_ciphertext, flipped_plaintext_ciphertext))

    print()
    # Key 差 1 bit，加密後結果
    flipped_key_ciphertext = des_encrypt(key2, plaintext1)
    print("key 差 1 bit 結果: ", binascii.hexlify(flipped_key_ciphertext))
    print(compare_results(original_ciphertext, flipped_key_ciphertext))

if __name__ == "__main__":
    main()
