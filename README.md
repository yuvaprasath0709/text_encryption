# Text Encryption Tool (AES | DES | RSA)

This project is a command-line interface (CLI) tool developed in Python for encrypting and decrypting text using three different cryptographic algorithms: Advanced Encryption Standard (AES), Data Encryption Standard (DES), and Rivest–Shamir–Adleman (RSA). It serves as a practical demonstration of fundamental concepts in cybersecurity and data protection.

This tool was developed as part of the **Pinnacle Labs 2025 Internship Program - Task 1: Text Encryption**[cite: 1].

## ✨ Features

* **AES Encryption/Decryption:** Securely encrypt and decrypt text using the AES algorithm in CBC (Cipher Block Chaining) mode.
* **DES Encryption/Decryption:** Encrypt and decrypt text using the DES algorithm in ECB (Electronic Codebook) mode.
* **RSA Encryption/Decryption:** Implement asymmetric encryption/decryption using RSA, demonstrating the use of public and private keys.
* **User-Friendly CLI:** An interactive command-line interface guides the user through algorithm selection and encryption/decryption operations.
* **Robust Error Handling:** Includes `try-except` blocks to gracefully handle common errors during cryptographic operations.
* **Clear Output:** Formatted output for encrypted/decrypted results and error messages.

## 📦 Dependencies

This project requires the following Python libraries:

* `pycryptodome`: Provides cryptographic primitives for AES and DES.
* `rsa`: Implements the RSA algorithm.

### Installation

It is highly recommended to use a Python virtual environment to manage dependencies and avoid conflicts with your system's Python packages.

1.  **Navigate to your project directory:**

    ```bash
    cd your_project_directory
    ```

    (Replace `your_project_directory` with the actual path to your project folder, e.g., `~/Desktop/project`)

2.  **Install the required libraries:**

    ```bash
    pip install pycryptodome rsa
    ```

## 🚀 How to Run

Once the dependencies are installed and your virtual environment is active, you can run the script:

```bash
python text_encryption.py
```

## 💡 Usage

The tool will present you with a menu to choose an encryption algorithm and then whether you want to encrypt or decrypt.

```
============================================================
       TEXT ENCRYPTION SYSTEM (AES | DES | RSA)           
         Developed by Yuva Prasath
============================================================

Choose Encryption Algorithm:
1. AES (Advanced Encryption Standard)
2. DES (Data Encryption Standard)
3. RSA (Asymmetric Encryption)
4. Exit
Enter choice (1/2/3/4): 
```

Follow the prompts to enter your text/ciphertext and encryption key (for AES/DES).

## 🔐 Algorithms Explained

### AES (Advanced Encryption Standard)

* **Type:** Symmetric-key algorithm (uses the same key for encryption and decryption).
* **Key Size:** This implementation uses a 128-bit key (16 bytes).
* **Mode:** Cipher Block Chaining (CBC) mode, which provides strong security by chaining blocks together, making it resistant to certain attacks.
* **Use Case:** Widely used for secure data at rest and in transit, such as file encryption, network communication (e.g., HTTPS), and data storage.

### DES (Data Encryption Standard)

* **Type:** Symmetric-key algorithm.
* **Key Size:** This implementation uses a 64-bit key (8 bytes), but effectively 56 bits are used for encryption.
* **Mode:** Electronic Codebook (ECB) mode. Note that ECB is generally **not recommended for most applications** as identical plaintext blocks produce identical ciphertext blocks, which can reveal patterns. It's included here for educational purposes to demonstrate a simpler symmetric mode.
* **Use Case:** Historically significant, but largely superseded by AES due to its smaller key size making it vulnerable to brute-force attacks with modern computing power. Primarily for educational demonstration.

### RSA (Rivest–Shamir–Adleman)

* **Type:** Asymmetric-key algorithm (uses a pair of keys: a public key for encryption and a private key for decryption).
* **Key Size:** This implementation generates a 512-bit key pair.
    * **Note on Security:** For real-world applications, a key size of 2048 bits or higher is recommended for RSA to ensure adequate security against modern computational attacks. The 512-bit key here is for demonstration purposes.
* **Use Case:** Ideal for secure key exchange, digital signatures, and encrypting small amounts of data. It's slower than symmetric algorithms for large data encryption, so it's often used to securely exchange a symmetric key, which then encrypts the bulk of the data.

## 🧑‍💻 Author

Developed by **Yuva Prasath**
