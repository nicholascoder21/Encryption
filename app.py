import streamlit as st

st.title("🔐 Encryption Simulator")

st.write("Encrypt and decrypt messages using a secret key.")

# Caesar Cipher Functions
def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26

            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, key):
    return encrypt(text, -key)


option = st.selectbox(
    "Choose an action",
    ["Encrypt Message", "Decrypt Message"]
)

message = st.text_area("Enter your message")

key = st.number_input(
    "Enter secret key",
    min_value=1,
    max_value=25,
    value=3
)

if st.button("Run"):

    if option == "Encrypt Message":
        encrypted = encrypt(message, key)

        st.success("Message Encrypted!")
        st.code(encrypted)

    else:
        decrypted = decrypt(message, key)

        st.success("Message Decrypted!")
        st.code(decrypted)
