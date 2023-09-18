from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import streamlit as st

local_path = (
    "/Users/random/.cache/gpt4all/ggml-model-gpt4all-falcon-q4_0.bin"  # replace with your desired local file path
    # "/Users/random/.cache/gpt4all/wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin"  # replace with your desired local file path
)


def retrieve_info(query):
    similar_response = db.similarity_search(query, k=3)

    page_contents_array = [doc.page_content for doc in similar_response]

    # print(page_contents_array)

    return page_contents_array


def generate_response(message):
    context = retrieve_info(message)
    response = llm_chain.run(message=message, context=context)
    return response


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    length_function=len,
    add_start_index=True,
)

loader = TextLoader("mlops.txt")
documents = loader.load()
texts = text_splitter.split_documents(documents)

from langchain.embeddings.gpt4all import GPT4AllEmbeddings

embedder = GPT4AllEmbeddings()
db = FAISS.from_documents(texts, embedding=embedder)
# db = FAISS.from_embeddings
print("embeddings generated!")

callbacks = [StreamingStdOutCallbackHandler()]

llm = GPT4All(
    model=local_path,
    backend="llama",
    verbose=True,
    streaming=True,
    callbacks=callbacks,
)

template = """You are a helpful AI assistant and provide the answer for the question based on the given context.
Context:{context}
>>QUESTION<<{message}
>>ANSWER<<"""

prompt = PromptTemplate(input_variables=["context", "message"], template=template)

llm_chain = LLMChain(llm=llm, prompt=prompt)
print("model loaded!")


def main():
    st.set_page_config(page_title="Customer response generator", page_icon=":bird:")

    st.header("Customer response generator :bird:")
    message = st.text_area("customer message")

    if message:
        st.write("Generating best practice message...")

        result = generate_response(message)

        st.info(result)


if __name__ == "__main__":
    main()
