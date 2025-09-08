import streamlit as st
from pathlib import Path

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI & 클라우드 스터디 그룹",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Constants ----------
CONTENT_MD_PATH = Path(__file__).with_name("study_group_.md")
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfThvjFczyOJdlmh3k4IVTIlj-eIZkwV_GkJ8ve1va9JVgRoQ/viewform?usp=header"
DISCORD_URL = "https://discord.gg/8PMwmUY7"

# ---------- Styles ----------
CUSTOM_CSS = """
<style>
:root {
  --bg: #f8f9fa;
  --card: #ffffff;
  --accent: #2563eb;
  --accent-2: #0ea5e9;
  --text: #1f2937;
  --muted: #4b5563;
}

/* Background gradient */
.stApp {
  background: linear-gradient(135deg, #f3f4f6 0%, #f9fafb 100%);
}

/* Global text and typography */
html, body, [class*="css"]  { color: var(--text); }
body { font-size: 1.05rem; line-height: 1.7; }
h1, h2 { color: #111827; letter-spacing: .2px; font-weight: 800; }
h3, h4 { color: #1f2937; letter-spacing: .1px; font-weight: 700; }
h3 { font-size: 1.25rem; }
h4 { font-size: 1.1rem; }
p { color: var(--text); }
a { color: var(--accent); }
strong, b { color: #111827; font-weight: 600; }
ul, ol { margin: 0.4rem 0 0.8rem 1.2rem; }
li { margin: 0.15rem 0; }

/* General containers */
.block-container{ max-width: 1100px; }

/* Hero */
.hero {
  padding: 3.2rem 1rem 2.2rem;
  border-radius: 18px;
  background: linear-gradient(180deg, rgba(37, 99, 235, 0.08) 0%, rgba(0,0,0,0) 100%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
}
.hero:before {
  content: "";
  position: absolute;
  top: -40%; left: -10%;
  width: 80%; height: 140%;
  background: radial-gradient(40% 40% at 50% 50%, rgba(37, 99, 235, 0.08) 0%, rgba(0,0,0,0) 80%);
  filter: blur(40px);
}
.hero h1 { font-size: 2.4rem; margin: 0 0 .6rem 0; }
.hero p { color: var(--muted); font-size: 1.05rem; margin: 0; }

/* Badges */
.badges span{
  display: inline-flex; align-items: center; gap: .4rem;
  padding: .35rem .6rem; margin-right: .4rem; margin-bottom: .4rem;
  border: 1px solid rgba(0, 0, 0, 0.1);
  color: #1f2937;
  border-radius: 999px; font-size: .85rem;
  background: rgba(0, 0, 0, 0.02);
}

/* Card */
.card{
  background: var(--card);
  border: 1px solid rgba(0, 0, 0, 0.08);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  border-radius: 14px; padding: 1.1rem 1rem;
}
.card h4{ margin-top: 0; }
.card p{ color: #4b5563; }

/* Expander (1부: 학습 공유 & 집단 회고 등) */
.st-expander{
  border: 1px solid rgba(0, 0, 0, 0.1) !important;
  border-radius: 12px !important;
  background: #ffffff !important;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}
.st-expander > summary {
  color: #1f2937 !important; font-weight: 800; font-size: 1.05rem;
  background: rgba(0, 0, 0, 0.01);
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
  padding: 0.9rem 1rem;
}
.st-expander > summary:hover { background: rgba(0, 0, 0, 0.03); }
.st-expander .streamlit-expanderContent { padding: 0.6rem 1rem 1rem; }

/* CTA buttons */
.cta a{
  text-decoration: none; color: white; font-weight: 600;
  padding: .7rem 1rem; border-radius: 10px; display: inline-flex; gap: .5rem; align-items: center;
}
.cta .primary{ background: linear-gradient(90deg, var(--accent) 0%, #3b82f6 100%); box-shadow: 0 2px 12px rgba(37, 99, 235, 0.2); }
.cta .ghost{ border: 1px solid rgba(0, 0, 0, 0.1); color: var(--text); background: rgba(0, 0, 0, 0.02); }
.cta a:hover{ filter: brightness(1.06); }

/* Tabs (☁️ AWS, 📊 시각화/데이터, 🤖 AI, 🦙 오픈 LLM, 🌐 메타버스) */
.stTabs{
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  padding: .4rem .4rem 0 .4rem;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
.stTabs [data-baseweb="tab-list"]{
  gap: .25rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}
.stTabs [data-baseweb="tab"]{
  color: #4b5563;
  padding: .6rem .9rem;
  border-radius: 8px 8px 0 0;
}
.stTabs [data-baseweb="tab"][aria-selected="true"]{
  background: #eff6ff;
  color: #1d4ed8;
  border: 1px solid #bfdbfe;
  border-bottom-color: transparent;
}
.stTabs [data-baseweb="tab"]:hover{ background: rgba(0, 0, 0, 0.03); }

/* Section title */
.section-title{
  font-size: 1.5rem; margin: 1.8rem 0 .9rem 0; font-weight: 800; color: #111827;
}

/* Footer */
.footer{
  color: #6b7280; font-size: .95rem; text-align: center; padding: 1.2rem 0; opacity: .9;
}
</style>
"""

# ---------- Helpers ----------
@st.cache_data(show_spinner=False)
def load_md() -> str:
    try:
        return CONTENT_MD_PATH.read_text(encoding="utf-8")
    except Exception:
        return ""


def section_from_md(md: str, start: str, end_markers: list[str] | None = None) -> str:
    """Extract a section from markdown by header text.
    - start: header text to start from (e.g., '## 🧭 스터디 소개')
    - end_markers: list of possible next headers to stop at
    """
    if not md:
        return ""
    lines = md.splitlines()
    content_lines = []
    in_section = False
    for ln in lines:
        if not in_section and ln.strip().startswith(start):
            in_section = True
            continue
        if in_section:
            if end_markers and any(ln.strip().startswith(h) for h in end_markers):
                break
            content_lines.append(ln)
    # strip leading/trailing ---
    text = "\n".join(content_lines).strip()
    return text


def bullet_cards(bullets: list[tuple[str, str]], cols=3):
    cols = st.columns(cols)
    for i, (title, desc) in enumerate(bullets):
        with cols[i % len(cols)]:
            st.markdown(f"""
            <div class='card'>
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)


# ---------- App ----------
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

md = load_md()

# Hero
with st.container():
    st.markdown(
        f"""
        <div class="hero">
            <div class="badges">
                <span>🎓 실무형 러닝 커뮤니티</span>
                <span>☁️ 클라우드 & 🤖 AI</span>
                <span>🧩 데이터 & 시각화</span>
            </div>
            <h1>AI & 클라우드 스터디 그룹</h1>
            <p>커리어 전환, 자격증 취득, 최신 기술 실습까지 — 함께 성장하는 실전형 학습 공동체</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Why join
st.markdown(
  """<div class="cta" style="margin-top: 1rem; display:flex; gap:.6rem; flex-wrap: wrap;">
    <a class="primary" href="https://docs.google.com/forms/d/e/1FAIpQLSfThvjFczyOJdlmh3k4IVTIlj-eIZkwV_GkJ8ve1va9JVgRoQ/viewform?usp=header" target="_blank">📋 운영 설문 참여</a>
    <a class="ghost" href="https://discord.gg/8PMwmUY7" target="_blank">💬 디스코드 합류</a>
  </div>
  """,
  unsafe_allow_html=True,
)
st.markdown("<div class='section-title'>🎯 왜 참여해야 할까요?</div>", unsafe_allow_html=True)
why_md = section_from_md(md, "## 🎯 왜 참여해야 할까요?", ["---", "## "]) or ""
if why_md:
    # parse bullet points (lines starting with *)
    bullets = []
    for line in why_md.splitlines():
        if line.strip().startswith("* "):
            title = line.strip().removeprefix("* ").strip()
            if ":" in title:
                t, d = title.split(":", 1)
                bullets.append((t.strip(), d.strip()))
            else:
                bullets.append((title, ""))
    if bullets:
        bullet_cards(bullets, cols=2)

# Operation overview
st.markdown("<div class='section-title'>📅 운영 방식</div>", unsafe_allow_html=True)
ops_md = section_from_md(md, "## 📅 운영 방식", ["---", "## "]) or ""
if ops_md:
    # Display as two-column checklist style
    col1, col2 = st.columns(2)
    items = [ln.strip().removeprefix("* ").strip() for ln in ops_md.splitlines() if ln.strip().startswith("*")]
    for i, item in enumerate(items):
        (col1 if i % 2 == 0 else col2).markdown(f"- {item}")

# Study composition
st.markdown("<div class='section-title'>🧩 스터디 구성</div>", unsafe_allow_html=True)
comp_md = section_from_md(md, "## 🧩 스터디 구성", ["---", "## "]) or ""
with st.expander("🔹 1부: 학습 공유 & 집단 회고", expanded=True):
    part1 = section_from_md(md, "### 🔹 1부: 학습 공유 & 집단 회고", ["---", "## ", "### "]) or ""
    st.markdown(part1)

# Practical learning tabs
st.markdown("<div class='section-title'>🔹 2부: 주제별 실전 학습</div>", unsafe_allow_html=True)
aws_tab, viz_tab, ai_tab, oss_tab, meta_tab = st.tabs([
    "☁️ AWS", "📊 시각화/데이터", "🤖 AI", "🦙 오픈 LLM", "🌐 메타버스"
])

with aws_tab:
    aws_cert = section_from_md(md, "### 📌 AWS 자격증 대비", ["---", "### "]) or ""
    st.markdown("#### 📌 AWS 자격증 대비")
    st.markdown(aws_cert)

    st.divider()
    for tool in ["#### 🔹 Glue", "#### 🔹 Athena", "#### 🔹 Redshift", "#### 🔹 Databricks"]:
        sec = section_from_md(md, tool, ["#### ", "---", "### "]) or ""
        st.markdown(tool.replace("#### ", "#### "))
        st.markdown(sec)
        st.markdown("<br>", unsafe_allow_html=True)

with viz_tab:
    for tool in ["#### 🔹 Power BI", "#### 🔹 Streamlit", "#### 🔹 Spark", "#### 🔹 Airflow"]:
        sec = section_from_md(md, tool, ["#### ", "---", "### "]) or ""
        st.markdown(tool.replace("#### ", "#### "))
        st.markdown(sec)
        st.markdown("<br>", unsafe_allow_html=True)

with ai_tab:
    for tool in ["#### 🔹 HuggingFace", "#### 🔹 LangChain (RAG)", "#### 🔹 Stable Diffusion", "#### 🔹 Whisper"]:
        sec = section_from_md(md, tool, ["#### ", "---", "### "]) or ""
        st.markdown(tool.replace("#### ", "#### "))
        st.markdown(sec)
        st.markdown("<br>", unsafe_allow_html=True)

with oss_tab:
    tool = "#### 🔹 LLaMA"
    sec = section_from_md(md, tool, ["#### ", "---", "### "]) or ""
    st.markdown("#### 🔹 LLaMA")
    st.markdown(sec)
    st.markdown("<br>", unsafe_allow_html=True)

with meta_tab:
    meta = section_from_md(md, "### 🌐 메타버스 & 크리에이티브 도구", ["---", "## "]) or ""
    zep = section_from_md(md, "#### 제페토 (ZEPETO)", ["---", "### ", "## "]) or ""
    st.markdown("### 🌐 메타버스 & 크리에이티브 도구")
    st.markdown(meta)
    st.markdown("#### 제페토 (ZEPETO)")
    st.markdown(zep)
    st.markdown("<br>", unsafe_allow_html=True)

# Operating principles
st.markdown("<div class='section-title'>🛠 운영 원칙</div>", unsafe_allow_html=True)
ops2 = section_from_md(md, "## 🛠 운영 방식 (운영 원칙 추가)", ["---", "## "]) or ""
st.markdown(ops2)

# Plans
st.markdown("<div class='section-title'>🧠 추가 계획</div>", unsafe_allow_html=True)
plans = section_from_md(md, "## 🧠 추가 계획", ["---", "## "]) or ""
st.markdown(plans)

# CTA block
st.markdown("---")
st.markdown(
    f"""
    <div style='display:flex; flex-direction:column; gap:.6rem;'>
        <div style='font-size:1.2rem; font-weight:700;'>✨ 지금 참여하세요!</div>
        <div style='color:var(--muted)'>혼자 학습하는 불안감을 줄이고, 함께 성장하는 경험을 시작하세요.</div>
        <div class='cta' style='margin-top:.4rem; display:flex; gap:.6rem; flex-wrap: wrap;'>
            <a class='primary' href='{GOOGLE_FORM_URL}' target='_blank'>📋 운영 설문 참여</a>
            <a class='ghost' href='{DISCORD_URL}' target='_blank'>💬 디스코드 합류</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# Footer
st.markdown("<div class='footer'>Made with Streamlit · © AI & Cloud Study Group</div>", unsafe_allow_html=True)
