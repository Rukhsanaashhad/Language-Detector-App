import streamlit as st  
from langdetect import detect, DetectorFactory  


DetectorFactory.seed = 0  

 
language_names = {  
    'en 📖': 'English',  
    'it 🍝': 'Italian',  
    'es 🌮': 'Spanish',  
    'fr 🥖': 'French',  
    'de 🍺': 'German',  
    'ar 🕌': 'Arabic',
}  
st.set_page_config(page_title="Language Detector", page_icon="🌐")
st.title("Language Detection App🏷️ ")  
st.write("Enter any text to detect the language:")  

  
text_input = st.text_area("Input text here:")  

if st.button("Detect Language"):  
    if text_input:  
        language_code = detect(text_input)  
        language_full_name = language_names.get(language_code, "Unknown language")  
        st.success(f"The detected language is: {language_code} ({language_full_name})")  
    else:  
        st.warning("Please enter some text to detect the language.") 
     
 
st.write("---------------------")

st.write ("©️Developed and Created by [Muhammad Ashhad Khan](https://github.com/Rukhsanaashhad/Language-Detector-App)")
