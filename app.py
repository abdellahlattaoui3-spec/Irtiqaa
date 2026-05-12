import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الصفحة والتصميم الملكي الاحترافي
st.set_page_config(page_title="إرتقِ - IRTIQA", layout="wide", initial_sidebar_state="collapsed")

# تصميم CSS مخصص لإبهار العين
st.markdown("""
    <style>
    /* الخلفية الملكية المتدرجة */
    .main { 
        background: linear-gradient(180deg, #000000 0%, #1a0033 50%, #000000 100%);
        color: #d4af37;
        font-family: 'Amiri', serif;
    }
    /* الأزرار الذهبية الملكية */
    .stButton>button {
        background: linear-gradient(45deg, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c);
        color: black !important;
        border: none;
        border-radius: 15px;
        padding: 15px;
        font-weight: bold;
        font-size: 18px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
        cursor: pointer;
    }
    /* تصميم بطاقات الأقسام */
    .section-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #d4af37;
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 20px;
        direction: rtl;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; text-shadow: 2px 2px 4px #000; }
    .stCheckbox { color: #d4af37 !important; direction: rtl; font-size: 22px; }
    </style>
    """, unsafe_allow_html=True)

# 2. الهوية البصرية والدعاء المخصص
st.markdown("<h1>🌟 إرتقِ - IRTIQA</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.15); margin-bottom: 30px;'>
        <h2 style='margin: 0; color: #fdfc97;'>اللهم اغفر لي ولوالديّ وللمؤمنين والمؤمنات</h2>
        <p style='color: #d4af37; font-size: 1.5em; margin-top: 10px;'>بإشراف: عبد الله</p>
    </div>
    """, unsafe_allow_html=True)

# 3. إدارة الجلسة (السجل والمسبحة)
if 'total_tasbih' not in st.session_state: st.session_state.total_tasbih = 0
if 'history_log' not in st.session_state: st.session_state.history_log = []

# 4. التنقل بين النوافذ الخمس الرئيسية
choice = st.selectbox("إختر الوجهة:", ["📊 محاسبة النفس", "📿 المسبحة والذكر", "☀️ الأذكار التفاعلية", "📖 القرآن الكريم", "🕋 مواقيت الصلاة"])

st.write("---")

# --- النافذة 1: محاسبة النفس (النظام الذي طلبته بدقة) ---
if choice == "📊 محاسبة النفس":
    st.header("📋 سجل محاسبة النفس")
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌙 العبادات والنمو")
        q1 = st.checkbox("قيام الليل")
        q2 = st.checkbox("البر بالوالدين")
        q3 = st.checkbox("حفظ القرآن الكريم")
        q4 = st.checkbox("طلب العلم الخاص")
        q5 = st.checkbox("صلوات النوافل (الرواتب)")
        
    with col2:
        st.subheader("🕌 صلوات الجماعة")
        s1 = st.checkbox("صلاة الفجر في جماعة")
        s2 = st.checkbox("صلاة الظهر في جماعة")
        s3 = st.checkbox("صلاة العصر في جماعة")
        s4 = st.checkbox("صلاة المغرب في جماعة")
        s5 = st.checkbox("صلاة العشاء في جماعة")

    if st.button("💾 حفظ في سجلك الخاص"):
        entry = {"date": str(datetime.now().strftime("%Y-%m-%d %H:%M")), "status": "تم الإنجاز"}
        st.session_state.history_log.append(entry)
        st.success("تم الحفظ تلقائياً في سجلك. يمكنك العودة لرؤية ما فاتك!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- النافذة 2: المسبحة الذكية (نظام الـ 10,000) ---
elif choice == "📿 المسبحة والذكر":
    st.header("المسبحة الملكية الذكية")
    
    # مكافأة الوصول لـ 10,000 تسبيحة
    if st.session_state.total_tasbih >= 10000:
        st.balloons()
        st.markdown("<div style='text-align: center; color: #00ff00; font-size: 30px; animation: pulse 1s infinite;'>🎉 هنيئاً لك! لقد حققت هدف الـ 10,000 تسبيحة اليوم</div>", unsafe_allow_html=True)

    col_m1, col_m2, col_m3 = st.columns([1,2,1])
    with col_m2:
        st.markdown(f"""
            <div style='text-align: center; border: 10px double #d4af37; border-radius: 50%; padding: 60px; background: rgba(0,0,0,0.6); box-shadow: 0 0 20px #d4af37;'>
                <span style='font-size: 80px; font-weight: bold;'>{st.session_state.total_tasbih}</span><br>
                <span style='font-size: 25px;'>ذكر</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        if st.button("اضغط للتسبيح (سبحان الله وبحمده)"):
            st.session_state.total_tasbih += 1
            st.rerun()
        
        if st.button("تصفير العداد"):
            st.session_state.total_tasbih = 0
            st.rerun()

# --- النافذة 3: الأذكار التفاعلية (صباح ومساء) ---
elif choice == "☀️ الأذكار التفاعلية":
    st.header("أذكار الصباح والمساء")
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.info("نظام الأذكار الذكي: عند ضغطك على إتمام الذكر، سيتم توجيهك تلقائياً للذكر التالي.")
    if st.button("بدء أذكار الصباح ☀️"):
        st.write("الذكر الأول: آية الكرسي...")
    if st.button("بدء أذكار المساء 🌙"):
        st.write("الذكر الأول: أمسينا وأمسى الملك لله...")
    st.markdown("</div>", unsafe_allow_html=True)

# --- النافذة 4: القرآن الكريم ---
elif choice == "📖 القرآن الكريم":
    st.header("المصحف الشريف")
    st.markdown("<div class='section-card' style='text-align: center;'>", unsafe_allow_html=True)
    st.write("هنا قسم تلاوة وحفظ القرآن الكريم.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- النافذة 5: أوقات الصلاة والمنبه ---
elif choice == "🕋 مواقيت الصلاة":
    st.header("مواقيت الصلاة - الجزائر")
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.write("📍 المدينة: الجزائر العاصمة وما جاورها")
    st.button("🔔 تفعيل منبه الأذان (بصوت واحد)")
    st.markdown("</div>", unsafe_allow_html=True)

# التذييل النهائي
st.markdown("<br><hr><center><p style='opacity: 0.6;'>IRTIQA - تم التطوير والبرمجة خصيصاً لعبد الله - 2026</p></center>", unsafe_allow_html=True)
