import streamlit as st

from interface import display_frequency_table, process_frequency_analysis, display_ngraphs

def main():
    st.set_page_config(layout="centered", page_title="Frequency Analysis")
    st.title("Mono-alphabetic cipher decoder\n"
             "Developer: Ceban Vasile FAF-223")
    st.write("### Enter the cipher text")

    if 'input_text' not in st.session_state:
        st.session_state['input_text'] = None

    # Text input for cipher text
    input_text = st.text_area(label="Enter the encrypted text:", placeholder="Encrypted text...", height=300)

    # Start frequency analysis on button click
    if st.button('Start Frequency Analysis'):
        st.session_state['input_text'] = input_text

    # Retrieve the cipher text from session state
    input_text = st.session_state['input_text']

    # If input_text is available, display the frequency analysis
    if input_text:
        st.divider()
        col1, col2, col3 = st.columns([1.5, 3.5, 0.6])

        # Display standard letter frequencies and user input frequency analysis
        display_frequency_table(col1)
        process_frequency_analysis(input_text, col2, col3, input_text)

        # Display digraphs, trigraphs, and doubles analysis
        display_ngraphs(input_text)

if __name__ == "__main__":
    main()
