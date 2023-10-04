import streamlit as st
# from pdf_wrapper import PDFWrapper
# from digest_paper import PaperDigest
# from llm_wrapper import LLMWrapper
import os
# from pdfminer.high_level import extract_text
# Assuming the necessary imports for your question answering system

CACHE_DIR = "./cache/"
def is_digested(uploaded_filename):
    '''
    check if uploaded pdf has been digested and stored in cache
    '''
    path = os.path.join(CACHE_DIR, f"paper_digest_{uploaded_filename}.pkl")
    return os.path.exists(path)


# 1. Upload PDF

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

previous_qa = []

if uploaded_file:
    # 2. Parse the PDF
    with st.spinner('Extracting text from the uploaded PDF...'):
        uploaded_filename = uploaded_file.name
        cache_path = os.path.join(CACHE_DIR, f"paper_digest_{uploaded_filename}.pkl")
        if is_digested(uploaded_filename):
            # paper_digest = PaperDigest.load_from_local(cache_path)
            st.success("File existed, loaded digest from cache")
        else:
            # pdf_wrapper = PDFWrapper.from_byte_stream(uploaded_file)
            # paper_digest = PaperDigest(pdf_wrapper)
            # paper_digest.save_to_local(store_path=cache_path)
            st.success("File successfully digested and cached")

    st.success("Finished processing. Ask me anything about this doc!")


    
    # 3. Input queries from user
    user_query = st.text_input("Enter your question:")

    if user_query:
        # 4. Generate answer
        with st.spinner('Generating an answer...'):
            # docs = paper_digest.get_best_doc(query=user_query)
            # answer = LLMWrapper.ask(query=user_query,docs = docs)
            answer = f"DEMO|the answer for question {user_query} is ..."
            # TODO - potential questions
            # next_question = LLMWrapper.generate_next_question(prev_query=user_query,
            #                                prev_ans = answer,
            #                                docs = docs)
            next_question = '<DEMO|next question>'
            

            # Check if 'previous_qa' exists in session_state, if not, create it
            if 'previous_qa' not in st.session_state:
                st.session_state.previous_qa = []
            
            # Store this Q&A to previous_qa in session_state
            st.session_state.previous_qa.append((user_query, answer))

        # 5. Show the answer
        st.subheader("Answer:")
        st.write(answer)
        st.subheader("You may want to ask...")
        st.write(next_question)



    # Display previous questions and answers in the sidebar
    st.sidebar.title("Previous Questions & Answers")
    for question, answer in st.session_state.get('previous_qa', []):
        st.sidebar.markdown(f"**Q:** {question}")
        st.sidebar.markdown(f"**A:** {answer}")
        st.sidebar.markdown("---")