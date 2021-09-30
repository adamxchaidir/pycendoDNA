import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import Bio.Seq
import Bio.SeqUtils
from Bio.Seq import Seq
from Bio.SeqUtils import GC


####################
# Page Title
####################

image = Image.open('Pycendo Logo.png')
st.image(image, use_column_width=True)
st.write("""
# Pycendo: DNA Sequence Analysis
Sequence Length, GC-Content, Nucleotide Count
***
""")

####################
# Input Text Box
####################

#st.sidebar.header('Enter DNA Sequence')
st.header('Enter DNA Sequence')

sequence_input =""

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT')

## 1. Sequence Length
st.subheader('1. Sequence Length & GC-Content')
def DNA_nucleotide_count(seq):
    d = dict([
        ('Sequence Length (bp)',len(seq)),
        ('GC-Content (%)',GC(seq))
        ])
    return d

Y = DNA_nucleotide_count(sequence)

#Y_label = list(Y)
#Y_values = list(Y.values())

Y

## 2. DNA Nucleotide Count
st.subheader('2. DNA Nucleotide Count')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
        ])
    return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(50)
)
st.write(p)
