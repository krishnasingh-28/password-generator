import random
import streamlit as st
import pyperclip


# Define possible characters for the password
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '=']


# Function to generate characters
def generate_characters(count, char_list):
    return random.choices(char_list, k=count)

# Password strength indicator (basic)
def get_password_strength(password):
    length = len(password)
    if length >= 12:
        return "Strong 🔒"
    elif length >= 8:
        return "Medium 🔐"
    else:
        return "Weak 🔓"

# Function to generate password
def generate_password(n_letters, n_symbols, n_numbers):
    password_list = []

    # Add letters, symbols, and numbers
    password_list += generate_characters(n_letters, LETTERS)
    password_list += generate_characters(n_symbols, SYMBOLS)
    password_list += generate_characters(n_numbers, NUMBERS)

    # Shuffle the list and join to create a password string
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


def main():
    # Title of the app
    st.title("🔐 Welcome to Password Generator!")

    # User input
    inp = st.text_input("Enter Your Username:")
    n_letters = st.number_input("How many letters would you like in the password?", min_value=1, max_value=20, step=1, value=5)
    n_symbols = st.selectbox("How many symbols do you want in your password?", [0, 1, 2, 3, 4, 5])
    n_numbers = st.select_slider("How many numbers do you want in your password?", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Show total password length dynamically
    total_length = n_letters + n_symbols + n_numbers
    st.info(f"Total password length: {total_length} characters.")


    # Session state for storing password
    if 'password' not in st.session_state:
        st.session_state.password = ""

    # Generate password
    if st.button("Generate Password"):

        st.session_state.password = generate_password(n_letters, n_symbols, n_numbers)

        # Display the generated password
        st.success("Password generated successfully!")
        st.session_state.generated_password = st.session_state.password
        st.write("**Your Generated Password:**", st.session_state.generated_password)


        # Display password strength
        password_strength = get_password_strength(st.session_state.password)
        st.write("**Password Strength:**", password_strength)

    # Shuffle existing password
    if st.session_state.password:
        if st.button("Shuffle Password"):
            password_list = list(st.session_state.password)
            random.shuffle(password_list)
            shuffled_password = "".join(password_list)
            st.session_state.password = shuffled_password
            st.write("**Your Generated Password:**", st.session_state.generated_password)
            st.success("Password shuffled successfully!")
            st.write("**Your Shuffled Password:**", shuffled_password)
    else:
        st.write("Please generate a password first before shuffling.")

    # Option to copy password to clipboard (for local usage only)
    try:
        if st.session_state.password and st.button("Copy Password to Clipboard"):
            pyperclip.copy(st.session_state.password)
            st.success("Password copied to clipboard!")
    except ImportError:
        st.warning("Install pyperclip to enable copying to clipboard.")

if __name__ == "__main__":
    main()