import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key
genai.configure(api_key=google_gemini_api_key)


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

#setting the model
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)




#layout
st.set_page_config(layout="wide")

#title of our app
st.title('✍️🤖 BlogWrite : Your AI Writing Assistant')

#subheader
st.subheader("Thoughts, Stories, and Ideas for the Curious Mind")

#sidebar

with st.sidebar:
    st.title("Add Your Blog's Details ")
    st.subheader("Enter The Deatils of the Blog you want to Generate ")
    
    #Blog title
    blog_title=st.text_input("Blog title")

    #keywords input 
    keywords = st.text_area("Keywords ( comma-separated)")

    # no. of words
    num_words = st.slider("Number of words", min_value=100, max_value=2000, step=500)

    
    prompt_parts =[
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.",
      ]
    response = model.generate_content(prompt_parts)


    submit_button = st.button("Generate Blog")

if submit_button:
  
        st.title("YOUR BLOG POST :")
        st.write(response.text)
        
