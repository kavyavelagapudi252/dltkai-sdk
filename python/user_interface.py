import streamlit as st
import dltkai as dl


st.title("Email Analyzer")

st.sidebar.subheader("Select Feature")
sentiment_check = st.sidebar.checkbox("Sentiment", value=True)
tone_check = st.sidebar.checkbox("Tone", value=True)
#toxic_comment_check = st.sidebar.checkbox("Toxic comment", value=True)
sarcasm_check = st.sidebar.checkbox("Sarcasm", value=True)



# create textbox and button & choose model selection
input_text = st.text_area("Email Body")
submit_button = st.button("Analyze")

# on click of analyze button pass through all models
if submit_button:
    if sentiment_check:
        text_sentiment = dl.NaturalLanguage.sentiment_detect(input_text)
        # display output
        st.write('Sentiment Analysis')
        st.write(text_sentiment)
    
    # get model 2 output
    if tone_check:
        text_tone = dl.NaturalLanguage.detect_tonality(input_text)  
        st.write('Tone Analysis')
        st.write(text_tone)
    
    # get model 3 output
    #if toxic_comment_check:
    #    text_toxic = dl.NaturalLanguage.toxic_comment_detect(input_text)
    #   st.write('Message Toxic comment')
    #   st.write(text_toxic)

    # get model 4 output
    if sarcasm_check:
        text_sarcasm = dl.NaturalLanguage.sarcasm_detect(input_text)
        st.write('Sarcasm Detection')
        st.write(text_sarcasm)
    
    
    #"Final Summary"
    if text_sentiment['emotion'] == "NEGATIVE" or text_tone == "SPAM!":
        st.write('Summary')
        st.write('Unprofessional')

    elif text_sentiment['emotion'] == "POSITIVE" and text_tone == "HAM!" and text_sarcasm == "Non sarcastic":
        st.write('Summary')
        st.write('Professional')

    elif text_sentiment['emotion'] == "POSITIVE" and text_tone == "SPAM!" and text_sarcasm == "Sarcastic":
        st.write('Summary')
        st.write('Unprofessional')

    elif text_sentiment['emotion'] == "POSITIVE" and text_tone == "HAM!" and text_sarcasm == "Sarcastic":
        st.write('Summary')
        st.write('Professional')

    elif text_sentiment['emotion'] == "POSITIVE" and text_tone == "HAM!" and text_sarcasm == "Non sarcastic":
        st.write('Summary')
        st.write('Professional')

    elif text_sentiment['emotion'] == "POSITIVE" and text_tone == "SPAM!" and text_sarcasm == " Non sarcastic":
        st.write('Summary')
        st.write('Unprofessional')

    else:
        st.write('Professional')
