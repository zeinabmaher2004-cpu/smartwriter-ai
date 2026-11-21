
import streamlit as st
import re

st.set_page_config(
    page_title="SmartWriter AI",
    page_icon="✍️",
    layout="centered"
)

# إعدادات التصميم
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.stApp {
    direction: rtl;
    text-align: right;
}

.main-title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #5B4BDB;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 17px;
}

.stButton button {
    width: 100%;
    border-radius: 12px;
    background-color: #5B4BDB;
    color: white;
    font-weight: bold;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# العنوان
st.markdown(
    '<div class="main-title">✍️ SmartWriter AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">مساعدك الذكي لإنشاء المحتوى المهني</div>',
    unsafe_allow_html=True
)

st.divider()

st.write("### 📝 ماذا تريد أن تكتب اليوم؟")

content_type = st.selectbox(
    "نوع المحتوى",
    [
        "منشور تسويقي",
        "إعلان تجاري",
        "منشور مهني",
        "إعادة صياغة نص",
        "تحسين وتدقيق نص"
    ]
)

tone = st.selectbox(
    "أسلوب الكتابة",
    [
        "احترافي",
        "رسمي",
        "ودّي",
        "إبداعي",
        "مختصر"
    ]
)

audience = st.text_input(
    "الجمهور المستهدف",
    placeholder="مثلاً: العملاء، الموظفون، الطلاب..."
)

user_text = st.text_area(
    "اكتبي الفكرة أو النص هنا",
    placeholder="اكتبي تفاصيل المحتوى الذي تريدين إنشاءه أو تحسينه...",
    height=180
)

def improve_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def create_content(kind, tone, audience, text):

    if kind == "إعادة صياغة نص":
        return (
            f"إعادة صياغة بأسلوب {tone}:\n\n"
            f"{improve_text(text)}"
        )

    if kind == "تحسين وتدقيق نص":
        return (
            f"النص بعد التحسين الأولي:\n\n"
            f"{improve_text(text)}"
        )

    if kind == "إعلان تجاري":
        return (
            f"📢 إعلان تجاري\n\n"
            f"{text}\n\n"
            f"✨ اكتشفوا المزيد واستفيدوا من عروضنا!\n"
            f"الجمهور المستهدف: {audience or 'العملاء'}"
        )

    if kind == "منشور تسويقي":
        return (
            f"🌟 منشور تسويقي\n\n"
            f"{text}\n\n"
            f"لا تفوتوا الفرصة، تابعونا للمزيد!\n"
            f"الجمهور المستهدف: {audience or 'الجمهور العام'}"
        )

    return (
        f"📌 منشور مهني\n\n"
        f"{text}\n\n"
        f"مع تمنياتنا لكم بالتوفيق والنجاح."
    )

if st.button("✨ إنشاء المحتوى"):

    if not user_text.strip():
        st.warning("يرجى كتابة الفكرة أو النص أولاً.")

    else:
        result = create_content(
            content_type,
            tone,
            audience,
            user_text
        )

        st.success("تم تجهيز المحتوى بنجاح!")

        st.markdown("### 📄 المحتوى الناتج")

        st.text_area(
            "يمكنك نسخ المحتوى وتعديله",
            value=result,
            height=220
        )

        st.download_button(
            label="⬇️ تحميل المحتوى",
            data=result,
            file_name="smartwriter_content.txt",
            mime="text/plain"
        )

st.divider()

st.caption("SmartWriter AI | Professional Content Assistant")
