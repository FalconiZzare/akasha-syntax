import os


def load_documents(directory):
    documents = []

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    documents.append(file.read())

    return documents