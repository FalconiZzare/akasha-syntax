from langchain_community.embeddings import HuggingFaceEmbeddings
import numpy as np
import faiss

def index_documents(documents):
    # Initialize the embeddings model
    embeddings_model = HuggingFaceEmbeddings()

    # Embed all documents and flatten the list of embeddings
    document_embeddings = []
    for doc in documents:
        embeddings = embeddings_model.embed_documents(doc)
        # Assuming embed_documents returns a list of embeddings, ensure they're all the same shape
        for embedding in embeddings:
            document_embeddings.append(np.array(embedding).astype('float32'))

    # Convert the list of embeddings into a numpy array
    document_embeddings = np.array(document_embeddings)

    # Create and populate the FAISS index
    index = faiss.IndexFlatL2(document_embeddings.shape[1])  # L2 distance index
    index.add(document_embeddings)

    return index, embeddings_model