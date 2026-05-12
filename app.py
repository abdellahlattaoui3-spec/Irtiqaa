import streamlit as st
import pandas as pd

# إعدادات الصفحة (العنوان والألوان)
st.set_page_config(page_title="برنامج إرتقاء", layout="centered")

# تطبيق التنسيق الأسود والذهبي (CSS)
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    h1, h2, h3 { color: #d4af37 !important; text-align: right; }
    .stButton>button { background-color: #d4af37; color: black; width: 100%; border-radius: 10px; }
    p { text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

# إضافة اللوجو (إذا كان عندك رابط الصورة، نضعه هنا)
st.title("برنامج إرتقاء irtiqaa")
st.write("مرحباً بك في منصتك الخاصة للمحاسبة والقرآن الكريم")

# القائمة الجانبية للتنقل
menu = ["المحاسبة اليومية", "المصحف الشريف", "إحصائيات النمو"]
choice = st.sidebar.selectbox("اختر القسم", menu)

if choice == "المحاسبة اليومية":
    st.header("📊 سجل المحاسبة")
    col1, col2 = st.columns(2)
    with col1:
        item = st.text_input("البيان (شراء/بيع)", placeholder="مثلاً: شراء سلع")
    with col2:
        amount = st.number_input("المبلغ (دج)", min_value=0)
    
    if st.button("إضافة العملية"):
        st.success(f"تم تسجيل: {item} بمبلغ {amount} دج")

elif choice == "المصحف الشريف":
    st.header("📖 الورد اليومي")
    st.write("هنا يمكنك متابعة قراءتك للقرآن الكريم.")
    surah = st.selectbox("اختر السورة", ["الفاتحة", "البقرة", "آل عمران"])
    st.info(f"أنت الآن تقرأ في سورة {surah}")

elif choice == "إحصائيات النمو":
    st.header("📈 إحصائيات إرتقاء")
    # مثال بسيط لرسم بياني
    data = pd.DataFrame({'أيام الأسبوع': ['الأحد', 'الإثنين', 'الثلاثاء'], 'الإنجاز': [10, 20, 15]})
    st.line_chart(data.set_index('أيام الأسبوع'))

st.write("---")
st.caption("irtiqaa - تم التطوير بكل فخر")
