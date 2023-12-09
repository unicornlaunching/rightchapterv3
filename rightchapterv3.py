import streamlit as st
import openai

# Function to generate chapterized text
def chapterize_text(text):
    try:
        response = openai.Completion.create(
            model="text-davinci-004",  # Use the latest GPT-4 model
            prompt=f"Create a chapter from the following text with a title, a quote related to the chapter, and the body of the chapter:\n\n{text}",
            max_tokens=500  # You can adjust the max tokens as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app layout
def main():
    st.title("Chapterize Your Text")

    # Text area for user input
    user_input = st.text_area("Paste your text here:", height=300)

    # Button to chapterize text
    if st.button("Chapterize"):
        with st.spinner("Generating chapter..."):
            chapterized_text = chapterize_text(user_input)
            st.write(chapterized_text)

if __name__ == "__main__":
    main()
