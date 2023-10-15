import streamlit as st
from utils import read_image, preprocess_image, predict

st.title('Scientists Face Detection')
st.markdown('Coded with :heart: by [@mu57f2](https://github.com/mu57f4)')

col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header('Alan Turing')
   st.image('application\sample_images\image_1.jpg')

with col2:
   st.header('Albert Einstein')
   st.image('application\sample_images\image_2.jpg')

with col3:
   st.header('Issac Newton')
   st.image('application\sample_images\image_3.jpg')

with col4:
    st.header('Marie Curie')
    st.image('application\sample_images\image_4.jpg')

# file uploader
# https://github.com/streamlit/streamlit/issues/888
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # read and process image
    img = read_image(uploaded_file)
    X = preprocess_image(img)
    try:
        y, y_proba = predict(X)
        col1, col2 = st.columns(2)
        with col1:
            st.image(uploaded_file, channels='RBG')
        with col2:
            st.header(y)
            st.header(f'Probability: {y_proba}%')
    except:
        st.error("Something went wrong, Please upload a photo with clear human face", icon="🚨")
