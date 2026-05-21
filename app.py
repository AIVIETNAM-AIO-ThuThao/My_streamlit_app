import streamlit as st      #framework để tạo ứng dụng web tương tác
import pandas as pd
import numpy as np
import seaborn as sns       # thư viện vẽ biểu đồ thống kê 
import matplotlib.pyplot as plt     # pyplot là module chính để tạo figure, axes, và các thành phần đồ họa


st.title("Ứng dụng Streamlit - Day7 của Thảo")
st.write("Chào mừng bạn đến với ứng dụng hết sức sơ sài này!")

# Ví dụ một số thành phần
name = st.text_input("Nhập tên của bạn:")
if name:
    st.success(f"Xin chào {name}!")

# Tạo dữ liệu mẫu
data = pd.DataFrame({
    'Cột A': np.random.randn(50),
    'Cột B': np.random.randn(50)
})
st.line_chart(data)

# Thêm slider
value = st.slider("Chọn giá trị:", 0, 100, 50)
st.write(f"Bạn chọn: {value}")