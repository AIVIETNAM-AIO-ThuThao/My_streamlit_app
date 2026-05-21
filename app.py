import streamlit as st      #framework để tạo ứng dụng web tương tác
import pandas as pd
import numpy as np
import seaborn as sns       # thư viện vẽ biểu đồ thống kê 
import matplotlib.pyplot as plt     # pyplot là module chính để tạo figure, axes, và các thành phần đồ họa

st.set_page_config(
    page_title="🦍 🦍 🦍 Streamlit - Day7 của Thảo",
    page_icon="🚀",
    layout="wide"
)
st.title(":violet[Ứng dụng Streamlit - Day7 của Thảo]")
st.write("Chào mừng bạn đến với ứng dụng hết sức sơ sài này!<br> <br> Xin đội ơn sự đồng hành miệt mài của Deepseek", unsafe_allow_html=True)

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


st.title("Đồ thị hàm số y = sin(x)")
st.markdown("Đoạn [-10, 10]")

# Tạo dữ liệu
x = np.linspace(-10, 10, 1000)
y = np.sin(x)

# Vẽ đồ thị
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2, label='y = sin(x)')

# Đường trục
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.8)

# Lưới
ax.grid(True, alpha=0.3)

# Nhãn
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Đồ thị hàm số y = sin(x)', fontsize=14)

# Giới hạn
ax.set_xlim([-10, 10])
ax.set_ylim([-1.5, 1.5])

# Chú thích
ax.legend(loc='upper right')

# Hiển thị trên Streamlit
st.pyplot(fig)

# Thông tin thêm
with st.expander("Thông tin về hàm sin(x)"):
    st.write("""
    - **Tập xác định:** R (tất cả số thực)
    - **Tập giá trị:** [-1, 1]
    - **Chu kỳ:** 2π ≈ 6.283
    - **Tính chẵn lẻ:** Hàm số lẻ (sin(-x) = -sin(x))
    - **Giá trị đặc biệt:** sin(0) = 0, sin(π/2) = 1, sin(π) = 0
    """)

    st.title("Vẽ 2 đồ thị hàm số y = sin(x) và y = cos(x) trên 1 biểu đồ   ")
    st.title("📈 Đồ thị hàm số y = sin(x) và y = cos(x)")
st.markdown("Đoạn [-10, 10]")

# Tạo dữ liệu
x = np.linspace(-10, 10, 1000)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Vẽ đồ thị
fig, ax = plt.subplots(figsize=(12, 6))

# Vẽ hai đường
ax.plot(x, y_sin, 'b-', linewidth=2, label='y = sin(x)')
ax.plot(x, y_cos, 'r-', linewidth=2, label='y = cos(x)')

# Đường trục
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
ax.axvline(x=0, color='k', linestyle='-', linewidth=0.8)

# Lưới
ax.grid(True, alpha=0.3)

# Nhãn
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Đồ thị hàm số y = sin(x) và y = cos(x)', fontsize=14)

# Giới hạn
ax.set_xlim([-10, 10])
ax.set_ylim([-1.5, 1.5])

# Chú thích
ax.legend(loc='upper right', fontsize=12)

# Hiển thị trên Streamlit
st.pyplot(fig)

# Thông tin thêm
with st.expander("Thông tin về hàm sin(x) và cos(x)"):
    st.write("""
    ### So sánh sin(x) và cos(x)
    
    | Tính chất | sin(x) | cos(x) |
    | :--- | :--- | :--- |
    | **Tập xác định** | R | R |
    | **Tập giá trị** | [-1, 1] | [-1, 1] |
    | **Chu kỳ** | 2π ≈ 6.283 | 2π ≈ 6.283 |
    | **Tính chẵn lẻ** | Hàm lẻ | Hàm chẵn |
    | **Giá trị tại x=0** | sin(0) = 0 | cos(0) = 1 |
    | **Lệch pha** | cos(x) = sin(x + π/2) | sin(x) = cos(x - π/2) |
    """)

# Hiển thị bảng giá trị
with st.expander("Bảng giá trị tại một số điểm"):
    import pandas as pd
    
    x_vals = [-10, -5, -3, -1.57, 0, 1.57, 3, 5, 10]
    data = {
        'x': x_vals,
        'sin(x)': [np.sin(x_val) for x_val in x_vals],
        'cos(x)': [np.cos(x_val) for x_val in x_vals]
    }
    df = pd.DataFrame(data)
    df = df.round(4)
    st.dataframe(df, use_container_width=True)


st.title("Bài 3: Vẽ đồ thị hàm bậc 2")
st.write("Yêu cầu: Nhập hệ số a, b, c cho phương trình y = ax2 + bx + c và vẽ đồ thị tương ứng. Dùng st.slider để điều chỉnh giá trị của a, b, c và cập nhật đồ thị theo thời gian thực.")
col1, col2, col3 = st.columns(3)

with col1:
    a = st.slider("Hệ số a", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
    
with col2:
    b = st.slider("Hệ số b", min_value=-10.0, max_value=10.0, value=0.0, step=0.5)
    
with col3:
    c = st.slider("Hệ số c", min_value=-10.0, max_value=10.0, value=0.0, step=0.5)

# Hiển thị phương trình hiện tại
st.markdown(f"### Phương trình hiện tại: **y = {a}x² + {b}x + {c}**")

# Tạo dữ liệu cho đồ thị
x = np.linspace(-10, 10, 500)
y = a * x**2 + b * x + c

# Tính toán các điểm đặc biệt
delta = b**2 - 4*a*c

# Tìm đỉnh của parabol
if a != 0:
    vertex_x = -b / (2*a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
else:
    vertex_x = None
    vertex_y = None

# Tìm nghiệm (nếu có)
if a != 0 and delta >= 0:
    root1 = (-b - np.sqrt(delta)) / (2*a)
    root2 = (-b + np.sqrt(delta)) / (2*a)
    roots = [root1, root2]
else:
    roots = []

# Tạo figure với 2 cột
left_col, right_col = st.columns([2, 1])

with left_col:
    # Vẽ đồ thị
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Vẽ đường parabol
    ax.plot(x, y, 'b-', linewidth=2.5, label=f'y = {a}x² + {b}x + {c}')
    
    # Vẽ trục
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.8)
    
    # Vẽ lưới
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Đánh dấu đỉnh
    if a != 0 and vertex_x is not None:
        ax.plot(vertex_x, vertex_y, 'ro', markersize=8, label=f'Đỉnh ({vertex_x:.2f}, {vertex_y:.2f})')
        ax.annotate(f'({vertex_x:.2f}, {vertex_y:.2f})', 
                    xy=(vertex_x, vertex_y), xytext=(10, 10),
                    textcoords='offset points', fontsize=9, color='red')
    
    # Đánh dấu nghiệm
    for i, root in enumerate(roots):
        if -10 <= root <= 10:  # Chỉ hiển thị nghiệm trong khung nhìn
            ax.plot(root, 0, 'go', markersize=8, label=f'Nghiệm {i+1}' if i == 0 else "")
            ax.annotate(f'{root:.2f}', 
                       xy=(root, 0), xytext=(5, -15),
                       textcoords='offset points', fontsize=9, color='green')
    
    # Thiết lập giới hạn
    y_min = min(np.min(y), -5)
    y_max = max(np.max(y), 5)
    ax.set_xlim([-10, 10])
    ax.set_ylim([y_min - 2, y_max + 2])
    
    # Nhãn
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Đồ thị hàm số bậc 2', fontsize=14)
    ax.legend(loc='upper right')
    
    st.pyplot(fig)

with right_col:
    st.subheader("Phân tích đồ thị")
    
    # Thông tin về hệ số a
    if a > 0:
        st.success(f"✅ **a = {a} > 0** → Parabol **mở lên trên** (bề lõm hướng lên)")
        st.write("Đồ thị có **giá trị cực tiểu** tại đỉnh")
    elif a < 0:
        st.error(f"❌ **a = {a} < 0** → Parabol **mở xuống dưới** (bề lõm hướng xuống)")
        st.write("Đồ thị có **giá trị cực đại** tại đỉnh")
    else:
        st.warning(f"⚠️ **a = 0** → Đây không còn là hàm bậc 2, mà là đường thẳng")
    
    # Thông tin về đỉnh
    if a != 0 and vertex_x is not None:
        st.write(f"### 🎯 Đỉnh parabol")
        st.write(f"- **x₀ =** {vertex_x:.2f}")
        st.write(f"- **y₀ =** {vertex_y:.2f}")
        
        if a > 0:
            st.write(f"- **GTNN =** {vertex_y:.2f} tại x = {vertex_x:.2f}")
        else:
            st.write(f"- **GTLN =** {vertex_y:.2f} tại x = {vertex_x:.2f}")
    
    # Thông tin về nghiệm
    st.write("### 📌 Nghiệm của phương trình")
    if a == 0:
        if b != 0:
            linear_root = -c / b
            st.write(f"Phương trình bậc nhất: **x = {linear_root:.2f}**")
        else:
            st.write("Không phải phương trình bậc nhất")
    else:
        delta = b**2 - 4*a*c
        st.write(f"**Δ =** {delta:.2f}")
        
        if delta > 0:
            st.success(f"✅ Δ > 0 → **2 nghiệm phân biệt**")
            st.write(f"- x₁ = {roots[0]:.2f}")
            st.write(f"- x₂ = {roots[1]:.2f}")
        elif delta == 0:
            st.info(f"📌 Δ = 0 → **Nghiệm kép**")
            st.write(f"- x = {roots[0]:.2f}")
        else:
            st.error(f"❌ Δ < 0 → **Vô nghiệm thực**")
            st.write("Đồ thị không cắt trục Ox")
    
    # Trục đối xứng
    if a != 0:
        st.write("### 🔄 Trục đối xứng")
        st.write(f"x = {vertex_x:.2f}")

# Thêm phần giải thích
with st.expander("📖 Hướng dẫn và giải thích"):
    st.markdown("""
    ### Cách đọc đồ thị hàm bậc 2
    
    #### Hệ số a (quyết định hình dáng)
    - **a > 0**: Parabol mở lên trên, có điểm cực tiểu
    - **a < 0**: Parabol mở xuống dưới, có điểm cực đại
    - **|a| càng lớn**: Parabol càng "hẹp" (độ cong lớn)
    - **|a| càng nhỏ**: Parabol càng "rộng" (độ cong nhỏ)
    
    #### Hệ số b (ảnh hưởng đến vị trí đỉnh)
    - Công thức đỉnh: **x₀ = -b/(2a)**
    - **b** dịch chuyển đỉnh sang trái hoặc phải
    
    #### Hệ số c (giao điểm với trục Oy)
    - Đồ thị luôn cắt trục Oy tại điểm **(0, c)**
    
    #### Ý nghĩa của Δ (delta) = b² - 4ac
    - **Δ > 0**: 2 nghiệm phân biệt → đồ thị cắt Ox tại 2 điểm
    - **Δ = 0**: Nghiệm kép → đồ thị tiếp xúc với Ox
    - **Δ < 0**: Vô nghiệm → đồ thị không cắt Ox
    """)

st.markdown("---")
st.markdown("~~Bài 5. Dùng sns.heatmap để vẽ biểu đồ nhiệt của hàm z = x2 + y2.~~")

# Tạo lưới giá trị x và y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

# Tạo ma trận lưới
X, Y = np.meshgrid(x, y)

# Tính giá trị z = x² + y²
Z = X**2 + Y**2

# Tạo DataFrame cho heatmap
df_heatmap = pd.DataFrame(Z, index=np.round(y, 2), columns=np.round(x, 2))

# ==================== HIỂN THỊ ====================
col1, col2 = st.columns([2, 1])

with col1:
    # Vẽ heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Tạo heatmap với seaborn
    sns.heatmap(df_heatmap, 
                cmap='hot',        # Bảng màu: hot (đỏ cam vàng)
                annot=False,       # Không hiển thị số ô (vì bảng lớn)
                fmt='.1f',
                linewidths=0,
                cbar_kws={'label': 'Giá trị z = x² + y²', 'shrink': 0.8},
                ax=ax)
    
    ax.set_title('Heatmap của hàm z = x² + y²', fontsize=16, pad=20)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    
    st.pyplot(fig)

with col2:
    st.subheader("📊 Thông tin")
    st.write(f"**Khoảng giá trị của x:** [{x.min()}, {x.max()}]")
    st.write(f"**Khoảng giá trị của y:** [{y.min()}, {y.max()}]")
    st.write(f"**Giá trị nhỏ nhất của z:** {Z.min():.2f}")
    st.write(f"**Giá trị lớn nhất của z:** {Z.max():.2f}")
    
    st.markdown("---")
    st.subheader("🎨 Bảng màu")
    st.write("Sử dụng bảng màu **'hot'**")
    st.write("- Màu **tối** (đen/tím) → z nhỏ")
    st.write("- Màu **sáng** (đỏ/vàng/trắng) → z lớn")

# ==================== HIỂN THỊ MA TRẬN NHỎ ====================
st.subheader("📋 Ma trận giá trị (mẫu 10x10)")

# Lấy mẫu 10x10 để hiển thị
sample_size = 10
step = len(x) // sample_size

X_sample = X[::step, ::step]
Y_sample = Y[::step, ::step]
Z_sample = Z[::step, ::step]

df_sample = pd.DataFrame(Z_sample, 
                         index=np.round(Y_sample[:, 0], 2), 
                         columns=np.round(X_sample[0, :], 2))

st.dataframe(df_sample, use_container_width=True)

# ==================== THANH TRƯỢT TƯƠNG TÁC ====================
st.markdown("---")
st.subheader("🎮 Tương tác: Thay đổi miền giá trị")

col3, col4, col5 = st.columns(3)

with col3:
    x_min = st.slider("x min", -10, 0, -5, 1)
with col4:
    x_max = st.slider("x max", 0, 10, 5, 1)
with col5:
    resolution = st.slider("Độ phân giải", 20, 100, 50, 10)

# Tạo lại dữ liệu với miền mới
x_new = np.linspace(x_min, x_max, resolution)
y_new = np.linspace(x_min, x_max, resolution)
X_new, Y_new = np.meshgrid(x_new, y_new)
Z_new = X_new**2 + Y_new**2

df_heatmap_new = pd.DataFrame(Z_new, index=np.round(y_new, 2), columns=np.round(x_new, 2))

# Vẽ heatmap mới
fig2, ax2 = plt.subplots(figsize=(10, 8))
sns.heatmap(df_heatmap_new, 
            cmap='viridis',      # Bảng màu khác cho đa dạng
            annot=False,
            cbar_kws={'label': 'z = x² + y²'},
            ax=ax2)

ax2.set_title(f'Heatmap với x ∈ [{x_min}, {x_max}], y ∈ [{x_min}, {x_max}]', fontsize=14)
ax2.set_xlabel('x')
ax2.set_ylabel('y')

st.pyplot(fig2)

# ==================== GIẢI THÍCH ====================
with st.expander("📖 Giải thích về biểu đồ nhiệt (Heatmap)"):
    st.markdown("""
    ### Heatmap là gì?
    
    **Heatmap (biểu đồ nhiệt)** là dạng biểu đồ sử dụng màu sắc để biểu diễn giá trị của dữ liệu trên ma trận 2 chiều.
    
    ### Ý nghĩa của hàm z = x² + y²
    
    - **Hình dạng:** Paraboloid tròn xoay (hình cái bát/chén)
    - **Giá trị nhỏ nhất:** z = 0 tại (x=0, y=0)
    - **Tính đối xứng:** Đối xứng qua trục z (qua tâm O)
    - **Càng xa tâm:** Giá trị z càng lớn
    
    ### Cách đọc heatmap
    
    | Màu sắc | Ý nghĩa |
    | :--- | :--- |
    | **Màu tối (đen/tím)** | Giá trị z nhỏ (gần tâm O) |
    | **Màu sáng (vàng/trắng)** | Giá trị z lớn (xa tâm O) |
    
    ### Ứng dụng
    
    - Phân tích tương quan giữa các biến
    - Phát hiện cụm dữ liệu
    - Biểu diễn ma trận hệ số
    - Trực quan hóa dữ liệu không gian 2D
    """)
