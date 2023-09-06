import streamlit as st
from pdf_wrapper import PDFWrapper

# upload pdf
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

previous_qa = []

if uploaded_file:
    with st.spinner('Extracting text from the uploaded PDF...'):
        uploaded_filename = uploaded_file.name
    st.success("Finished processing. Ask me anything about this doc!")

    # Input queries from user
    user_query = st.text_input("Enter your question:")

    if user_query:
        # Generate answer
        with st.spinner('Generating an answer...'):
            answer="test answer"
        # Show the answer
        st.subheader("Answer:")
        st.write(answer)