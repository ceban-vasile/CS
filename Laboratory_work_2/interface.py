import streamlit as st
import pandas as pd
from analyzer import get_letter_frequencies, replace_letters, count_digraphs, count_trigraphs, count_doubles

letter_freqs = {
    'Letter': ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'],
    'Frequency': [12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3, 4.0, 2.8, 2.8, 2.4, 2.4, 2.2, 2.0, 2.0, 1.9, 1.5, 1.0, 0.8, 0.15, 0.15, 0.10, 0.07]
}

def display_frequency_table(col1):
    col1.write("###### Standard Frequency")
    letter_freqs_df = pd.DataFrame(letter_freqs)
    col1.data_editor(
        letter_freqs_df,
        disabled=True, 
        hide_index=True
    )

def process_frequency_analysis(text, col2, col3, intercept):
    df = get_letter_frequencies(text)
    max_value = int(df['Count'].max())
    col2.write("###### Current Frequency Table")
    edited_df = col2.data_editor(
        df,
        column_config={
            "Count": st.column_config.ProgressColumn(
                label="Count",
                min_value=0,
                max_value=max_value,
                format="%d"
            ),
            "Matching_letter": st.column_config.SelectboxColumn(
                label="Replace",
                options=[chr(i) for i in range(97, 123)]  # a-z
            )
        }, 
        disabled=False,
        hide_index=True
    )

    if col3.button("Apply"):
        replaced_text = replace_letters(text, edited_df)
        st.text_area(label='Ciphertext', value=replaced_text, height=300, disabled=True)

        if not (edited_df['Matching_letter'].isnull().any() or (edited_df['Matching_letter'] == '').any()):
            print("All matching letters are completed.")
            print("Decoded text: \n" + replaced_text)
            st.snow()
    else:
        st.text_area(label='Ciphertext', value=intercept, height=300, disabled=True)

def display_ngraphs(text):
    st.divider()
    with st.expander("Digraphs", expanded=True):
        eng_digraphs = ['TH','HE','AN','IN','ER','ON','RE','ED','ND','HA','AT','EN']
        st.write("The most common **digraphs** in the English language are:")
        st.dataframe(pd.DataFrame(eng_digraphs).T)
        st.write("The most common **digraphs** in the text are:")
        digraph_counts = count_digraphs(text)
        st.dataframe(pd.DataFrame.from_dict(digraph_counts, orient='index', columns=['Count']).T)

    with st.expander("Trigraphs", expanded=True):
        eng_trigraphs = ['THE', 'AND', 'THA', 'ENT', 'ION', 'TIO', 'FOR', 'NDE', 'HAS', 'NCE', 'TIS', 'OFT', 'MEN']
        st.write("The most common **trigraphs** in the English language are:")
        st.dataframe(pd.DataFrame(eng_trigraphs).T)
        st.write("The most common **trigraphs** in the text are:")
        trigraphs_count = count_trigraphs(text)
        st.dataframe(pd.DataFrame.from_dict(trigraphs_count, orient='index', columns=['Count']).T)

    with st.expander("Doubles", expanded=True):
        eng_doubles = ['SS', 'EE', 'TT', 'FF', 'LL', 'MM', 'OO']
        st.write("The most common **double letters** in the English language are:")
        st.dataframe(pd.DataFrame(eng_doubles).T)
        st.write("The most common **double letters** in the text are:")
        doubles_count = count_doubles(text)
        st.dataframe(pd.DataFrame.from_dict(doubles_count, orient='index', columns=['Count']).T)