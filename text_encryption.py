from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
import base64
import rsa
import sys

# ========== AES FUNCTIONS ==========
def pad_aes(text):
    return text + (16 - len(text) % 16) * ' '

def aes_encrypt(text, key):
    try:
        key = key[:16].ljust(16).encode()
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad_aes(text).encode())
        return base64.b64encode(iv + encrypted).decode()
    except Exception as e:
        return f"[AES Error] {str(e)}"

def aes_decrypt(ciphertext, key):
    try:
        key = key[:16].ljust(16).encode()
        data = base64.b64decode(ciphertext)
        iv, ct = data[:16], data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.decrypt(ct).decode().strip()
    except Exception as e:
        return f"[AES Decryption Error] {str(e)}"

# ========== DES FUNCTIONS ==========
def pad_des(text):
    return text + (8 - len(text) % 8) * ' '

def des_encrypt(text, key):
    try:
        key = key[:8].ljust(8).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        encrypted = cipher.encrypt(pad_des(text).encode())
        return base64.b64encode(encrypted).decode()
    except Exception as e:
        return f"[DES Error] {str(e)}"

def des_decrypt(ciphertext, key):
    try:
        key = key[:8].ljust(8).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        decrypted = cipher.decrypt(base64.b64decode(ciphertext))
        return decrypted.decode().strip()
    except Exception as e:
        return f"[DES Decryption Error] {str(e)}"

# ========== RSA FUNCTIONS ==========
(pub_key, priv_key) = rsa.newkeys(512)

def rsa_encrypt(text):
    try:
        encrypted = rsa.encrypt(text.encode(), pub_key)
        return base64.b64encode(encrypted).decode()
    except Exception as e:
        return f"[RSA Error] {str(e)}"

def rsa_decrypt(ciphertext):
    try:
        decrypted = rsa.decrypt(base64.b64decode(ciphertext), priv_key)
        return decrypted.decode()
    except Exception as e:
        return f"[RSA Decryption Error] {str(e)}"

# ========== UI & MAIN ==========
def print_header():
    print("="*60)
    print("      TEXT ENCRYPTION SYSTEM (AES | DES | RSA)        ")
    print("           Developed by Yuva Prasath")
    print("="*60)

def get_choice():
    print("\nChoose Encryption Algorithm:")
    print("1. AES (Advanced Encryption Standard)")
    print("2. DES (Data Encryption Standard)")
    print("3. RSA (Asymmetric Encryption)")
    print("4. Exit")
    return input("Enter choice (1/2/3/4): ").strip()

def get_action():
    return input("Do you want to Encrypt or Decrypt? (e/d): ").strip().lower()

def main():
    print_header()

    while True:
        algo = get_choice()
        if algo == '4':
            print("\nThank you for using the tool. Goodbye!")
            break

        action = get_action()
        if action not in ['e', 'd']:
            print("❌ Invalid action! Please enter 'e' or 'd'.")
            continue

        if algo in ['1', '2']:  # AES or DES
            text = input("\nEnter the text: ").strip()
            key = input("Enter the encryption key: ").strip()

            if algo == '1':  # AES
                result = aes_encrypt(text, key) if action == 'e' else aes_decrypt(text, key)
            else:  # DES
                result = des_encrypt(text, key) if action == 'e' else des_decrypt(text, key)

        elif algo == '3':  # RSA
            if action == 'e':
                text = input("\nEnter the text to encrypt: ").strip()
                result = rsa_encrypt(text)
            else:
                ciphertext = input("\nEnter the RSA ciphertext to decrypt: ").strip()
                result = rsa_decrypt(ciphertext)
        else:
            print("❌ Invalid selection! Try again.")
            continue

        print("\n✅ Result:")
        print("-" * 60)
        print(result)
        print("-" * 60)

        next_step = input("\nDo you want to perform another operation? (y/n): ").strip().lower()
        if next_step != 'y':
            print("\n👋 Exiting the tool. Stay secure!")
            break

    print("\nTool Developed by Yuva Prasath")
    print("="*60)

if __name__ == "__main__":
    main()
