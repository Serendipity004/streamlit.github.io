import streamlit as st
st.title('my web app:coffee:')
st.header('显示Markdown文本')
text = """
**Markdown**是一种文本格式的*标记语言*，能够使文本按照一定的格式进行显示。类似于:blue[HTML]文档，但标签比:blue[HTML]简单。
"""
st.markdown(text)
