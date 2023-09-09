"""
Author: owo
Date: 2023/09/09
Post: https://blog.o-w-o.cc/archives/streamlit-chatelements
License: CC BY-NC-SA 4.0
"""
import streamlit as st
import numpy as np

MODE = st.sidebar.selectbox("選擇展示模式", ['chat_input用法', 'chat_message用法', '組合', '組合(含紀錄)'])

if MODE == 'chat_input用法':
    user_input = st.chat_input("請輸入內容...")
    if user_input:
        st.write(f"使用者輸入了：`{user_input}`")

if MODE == 'chat_message用法':
    with st.chat_message("user"):
        st.write("給我一張圖")
    
    with st.chat_message("assistant"):
        st.bar_chart(np.random.randn(30, 3))

if MODE == '組合':
    if user_input := st.chat_input("請輸入內容..."):
        with st.chat_message("user"):
            st.markdown(user_input)
        
        with st.chat_message("assistant"):
            st.markdown(user_input)

if MODE == '組合(含紀錄)':
    # 初始化session
    if "messages" not in st.session_state:
        st.session_state.messages = []


    # 接收使用者輸入
    if user_input := st.chat_input("請輸入內容..."):
        # 將使用者的輸入加入紀錄
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # 將回應加入紀錄
        st.session_state.messages.append({"role": "assistant", "content": f"Ok, {user_input}"})

    # 顯示所有紀錄
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        