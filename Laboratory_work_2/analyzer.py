from collections import Counter
import pandas as pd

def get_letter_frequencies(text):
    letter_counts = Counter(char for char in text if char.isalpha())
    total_letters = sum(letter_counts.values())

    letter_freq = {letter: round((count / total_letters) * 100, 2) for letter, count in letter_counts.items()}

    df = pd.DataFrame({
        'Letter': letter_counts.keys(),
        'Count': letter_counts.values(),
        'Frequency': letter_freq.values(),
        'Matching_letter': [''] * len(letter_counts)
    })

    df = df.sort_values(by='Frequency', ascending=False)

    return df


def get_letter_frequencies(text):
    text = text.upper()
    letter_counts = Counter(char for char in text if char.isalpha())
    total_letters = sum(letter_counts.values())

    letter_freq = {letter: round((count / total_letters) * 100, 2) for letter, count in letter_counts.items()}

    df = pd.DataFrame({
        'Letter': letter_counts.keys(),
        'Count': letter_counts.values(),
        'Frequency': letter_freq.values(),
        'Matching_letter': [''] * len(letter_counts)
    })

    df = df.sort_values(by='Frequency', ascending=False)
    return df

def replace_letters(text, df):
    replacement_map = {row['Letter']: row['Matching_letter'] for _, row in df.iterrows() if row['Matching_letter']}
    new_text = ""

    for char in text.upper():
        if char in replacement_map:
            new_text += replacement_map[char].lower()
        else:
            new_text += char
    return new_text

def count_digraphs(text):
    digraph_counts = {}
    text = text.upper()

    for i in range(len(text) - 1):
        digraph = text[i:i + 2]
        if digraph.isalpha():
            if digraph in digraph_counts:
                digraph_counts[digraph] += 1
            else:
                digraph_counts[digraph] = 1

    sorted_digraphs = sorted(digraph_counts.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_digraphs[:12])

def count_trigraphs(text):
    trigraph_count = {}
    text = text.upper()

    for i in range(len(text) - 2):
        trigraph = text[i:i + 3]
        if trigraph.isalpha():
            if trigraph in trigraph_count:
                trigraph_count[trigraph] += 1
            else:
                trigraph_count[trigraph] = 1

    sorted_trigraphs = sorted(trigraph_count.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_trigraphs[:13])

def count_doubles(text):
    double_count = {}
    text = text.upper()

    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            double = text[i:i + 2]
            if double in double_count:
                double_count[double] += 1
            else:
                double_count[double] = 1

    sorted_doubles = sorted(double_count.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_doubles[:7])
