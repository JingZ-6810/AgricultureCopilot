import io
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter

# https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_text_splitter


class PDFWrapper:
    """
    Wrapper class for loading PDF files
    """

    def __init__(self, reader):
        self.pages = {i: page.extract_text() for i, page in enumerate(reader.pages)}
    
    def get_all_text(self):
        self.all_text = ""
        for page, text in self.pages.items():
           self.all_text += text
        return self.all_text
    
    def create_chunks(self):
        '''
        Split pdf into some chunks
        '''
        text = self.get_all_text()
        # TODO - split by tokens
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=3000,   # split by characters
            chunk_overlap=200,
            length_function=len
            )
        self.chunks = text_splitter.split_text(text=text)
        print(f"chunks created, number of chunks: {len(self.chunks)}")
        return self.chunks

    @staticmethod
    def from_local_file(file_path):
        '''
        load pdf from a path
        '''
        with open(file_path, "rb") as f:
            local_file_bytes = io.BytesIO(f.read())
            reader = PyPDF2.PdfReader(local_file_bytes)
            return PDFWrapper(reader)