import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def main():
    st.title("Image Analysis App")

    image_url = st.text_input("Enter the pre-signed URL of your image:")

    if st.button("Analyze Image"):
        if image_url:
            description = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Explain the architecture proposed in the provided diagram in a paragraph",
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_url,
                                },
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )
            st.write(description.choices[0].message.content)
        else:
            st.write("Please enter a valid URL.")


if __name__ == "__main__":
    main()
