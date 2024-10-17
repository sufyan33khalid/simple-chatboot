# Step 1: Install Streamlit if not installed
# !pip install streamlit

import streamlit as st

# Step 2: Define AI-related questions and answers
ai_knowledge = {
    "what is artificial intelligence": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think, learn, and problem-solve like humans.",
    "what are the types of ai": "AI can be categorized into three types: Narrow AI, General AI, and Super AI.",
    "what is narrow ai": "Narrow AI, also known as Weak AI, is designed to perform a narrow task, such as facial recognition or internet searches.",
    "what is general ai": "General AI, or Strong AI, refers to systems that possess the ability to perform any intellectual task that a human being can do.",
    "what is machine learning": "Machine Learning is a subset of AI that involves the use of algorithms and statistical models to allow computers to improve their performance on tasks over time without explicit programming.",
    "what is deep learning": "Deep Learning is a subset of machine learning that uses neural networks with many layers (hence 'deep') to model complex patterns in data.",
    "how is ai used in real life": "AI is used in various applications such as virtual assistants (e.g., Siri, Alexa), autonomous driving, healthcare diagnostics, and more.",
    "what is neural network": "A Neural Network is a series of algorithms that attempt to recognize relationships in a set of data through a process that mimics the way the human brain operates.",
    "who is the father of ai": "John McCarthy is considered the father of AI. He coined the term 'Artificial Intelligence' in 1956."
}

# Step 3: Define the chatbot function
def get_ai_response(user_input):
    return ai_knowledge.get(user_input.lower().strip(), "Sorry, I can only answer AI-related questions. Please ask something about AI.")

# Step 4: Streamlit app layout and interaction
def main():
    # Display the header with red color text
    st.markdown("<h1 style='color: red;'>Created by Sufyan Khalid</h1>", unsafe_allow_html=True)

    # Add a title for the app
    st.title("AI Chatbot")

    # Input field for the user
    user_input = st.text_input("Ask me anything about AI:")

    # If user provides input, fetch the chatbot's response
    if user_input:
        response = get_ai_response(user_input)
        st.text_area("Chatbot Response:", value=response, height=150)

# Run the app
if __name__ == "__main__":
    main()
