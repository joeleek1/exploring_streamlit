import streamlit as st

def main():
    # Title
    st.title('Testin Ui')

    # Text
    st.text('Welcome to the application!')

    # Buttons
    if st.button('Hello Button'):
        st.text('Hello, you just pressed a button!')

    if st.button('Goodbye Button'):
        st.text('Goodbye, you just pressed a different button!')

    # Input fields
    input_text = st.text_input('Type here')
    if st.button('Submit'):
        result = input_text
        st.success(f'You typed: {result}')

    # Another way to get text input
    another_input_text = st.text_input('Type here as well')
    st.write(f'You typed: {another_input_text}')

if __name__ == '__main__':
    main()
