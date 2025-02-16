from langchain_text_splitters import RecursiveCharacterTextSplitter


def text_splitter(doc):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,  # Size of each chunk
        chunk_overlap=50,  # Overlap between chunks to maintain context
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_text(doc)
    return chunks
