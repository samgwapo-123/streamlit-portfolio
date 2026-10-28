import io
from datetime import date

import numpy as np
import pandas as pd
import streamlit as st

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Psalm Racaza | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .hero {padding: 1.2rem 1.5rem; border-radius: 16px;
           background: linear-gradient(120deg, #0f766e 0%, #1d4ed8 100%); color: white;}
    .hero h1 {margin: 0; color: white;}
    .hero p {margin: .2rem 0 0 0; opacity: .9;}
    .tag {display:inline-block; padding:2px 10px; margin:2px; border-radius:12px;
          background:#e0f2fe; color:#075985; font-size:.8rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- DATA ----------
NAME = "Psalm Racaza"
COURSE_SECTION = "CS365 · Applied AI · F1"  # EDIT
PROGRAM = "BS Computer Science, 3rd year"                         # EDIT

STAND_IN_PHOTO = """
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0f766e"/><stop offset="1" stop-color="#1d4ed8"/>
  </linearGradient></defs>
  <rect width="400" height="400" rx="40" fill="url(#g)"/>
  <circle cx="200" cy="155" r="62" fill="white" opacity=".9"/>
  <path d="M80 350 Q200 210 320 350 Z" fill="white" opacity=".9"/>
</svg>
"""

skills_df = pd.DataFrame(
    {
        "Skill": ["Next.js / React", "Supabase / SQL", "Python / Flask", "Kotlin / Android",
                  "React Native / Expo", "C# / Blazor", "Java / JavaFX", "PHP / MySQL",
                  "Rust / Tauri", "AI (Gemini API)"],
        "Level": [85, 80, 75, 65, 80, 70, 65, 70, 50, 78],      # EDIT: your honest self-ratings
        "Category": ["Frontend", "Backend", "Backend", "Mobile", "Mobile",
                     "Frontend", "Desktop", "Backend", "Desktop", "AI"],
    }
)

projects_df = pd.DataFrame(
    [
        {
            "Title": "GeneRX",
            "Role": "Lead Developer",  
            "Tools": ["React Native", "Expo", "Supabase"],
            "Outcome": "Mobile app that helps people find affordable generic medicines.",
            "Link": "https://github.com/Leandrozxc/GeneRX.git",  
        },
        {
            "Title": "Jeepney Mobility Intelligence Platform",
            "Role": "Developer / Team Member", 
            "Tools": ["Next.js", "Supabase", "Google Gemini AI"],
            "Outcome": "Crowdsourced jeepney route platform built for the IBPAP AI Competition hackathon.",
            "Link": "",  
        },
        {
            "Title": "Karenderya Management App",
            "Role": "Solo Developer",  
            "Tools": ["Python", "Flask"],
            "Outcome": "Tool to help my mom manage her small karenderya using simple reusable input lists.",
            "Link": "https://github.com/samgwapo-123/MiTinda.git", 
        },
        {
            "Title": "GroupFlow",
            "Role": "Developer & Designer", 
            "Tools": ["C#", "Blazor", "CSS"],
            "Outcome": "Student group project tracker, designed in Figma and built in Blazor.",
            "Link": "https://github.com/samgwapo-123/GroupFlow.git", 
        },
        {
            "Title": "Budget and Liquidation System for student orgs",
            "Role": "Solo Developer",  
            "Tools": ["TypeScript", "Google Gemini AI", "Supabase"],
            "Outcome": "Tracks budgets and liquidations for student organizations, with AI-generated summaries, and OCR for receipts.",
            "Link": "https://github.com/samgwapo-123/budget-and-liquidation-system.git",  
        },
    ]
)

milestones = pd.DataFrame(
    {
        "Year": [2019, 2024, 2024, 2024, 2025, 2026], 
        "Milestone": [
            "Wrote my first lines of code",
            "Started college in Cebu City",
            "Built my first full-stack web app",
            "Joined student orgs and my first hackathon",
            "Built mobile apps with React Native and Kotlin",
            "Built AI-powered projects and applying for internships",
        ],
    }
)

# ---------- SESSION STATE ----------
st.session_state.setdefault("visits", 0)
st.session_state.setdefault("likes", 0)
st.session_state.setdefault("feedback", [])
if "counted" not in st.session_state:
    st.session_state.visits += 1
    st.session_state.counted = True

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("🎛️ Site Controls")
    uploaded = st.file_uploader("Upload your photo", type=["png", "jpg", "jpeg"])
    st.divider()

    st.subheader("Skill Filter")
    categories = st.multiselect(
        "Show categories",
        sorted(skills_df["Category"].unique()),
        default=sorted(skills_df["Category"].unique()),
    )
    min_level = st.slider("Minimum skill level", 0, 100, 40, step=5)
    show_table = st.checkbox("Show skills table", value=True)

    st.divider()
    chart_type = st.radio("Chart style", ["Bar", "Area"], horizontal=True)
    st.divider()
    if st.button("👍 Like this portfolio"):
        st.session_state.likes += 1
        st.toast("Thanks for the like!", icon="💙")
    st.caption(f"Visits this session: {st.session_state.visits} · Likes: {st.session_state.likes}")
    st.link_button("GitHub", "https://github.com/samgwapo-123")  # EDIT

# ---------- HERO ----------
st.markdown(
    f"""
    <div class="hero">
      <h1>👋 Hi, I'm {NAME}</h1>
      <p>{PROGRAM} · Cebu City, Philippines</p>
      <p><b>{COURSE_SECTION}</b></p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

tab_about, tab_auto, tab_skills, tab_projects, tab_contact = st.tabs(
    ["🙋 About", "📖 Autobiography", "🛠️ Skills", "🚀 Projects", "📬 Contact"]
)

# ---------- ABOUT ----------
with tab_about:
    c1, c2 = st.columns([1, 2], gap="large")
    with c1:
        if uploaded:
            st.image(uploaded, caption=NAME, use_container_width=True)
        else:
            st.image(STAND_IN_PHOTO, caption="Stand-in photo", use_container_width=True)
    with c2:
        st.header("About Me")
        st.write(
            "I'm a student developer from Cebu City with a full-stack and backend "
            "background. I like building apps that solve real, local problems, "
            "especially in civic tech, health access, and community infrastructure. "
            "I'm about to graduate and I'm putting together a portfolio of projects "
            "that I built for classes, hackathons, and my own family."  # EDIT in your own words
        )
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Projects", len(projects_df))
        m2.metric("Technologies", len(skills_df))
        m3.metric("Hackathons", 1, delta="+1 this year")  # EDIT
        m4.metric("Top skill", skills_df.loc[skills_df.Level.idxmax(), "Skill"].split(" /")[0])

        st.markdown("**Interests**")
        st.markdown(
            "".join(f'<span class="tag">{t}</span>' for t in
                    ["Civic Tech", "Health Equity", "Mobile Apps", "AI Integration", "Hackathons"]),
            unsafe_allow_html=True,
        )
        st.map(pd.DataFrame({"lat": [10.3157], "lon": [123.8854]}), zoom=10, height=220)
        st.caption("📍 Cebu City, Philippines")

# ---------- AUTOBIOGRAPHY ----------
with tab_auto:
    st.header("My Story")
    a, b = st.columns(2, gap="large")
    with a:
        with st.expander("🏠 Background", expanded=True):
            st.write("Background Music")  # EDIT
        with st.expander("🎓 Education", expanded=True):
            st.write("CIT-U")  # EDIT
        with st.expander("💡 Interests & Motivation"):
            st.write("If you don't know where the wind is favorable, then you don't know what port you are sailing through.")  # EDIT
    with b:
        st.subheader("Milestones")
        year = st.select_slider(
            "Slide through the years",
            options=milestones["Year"].tolist(),
            value=milestones["Year"].iloc[-1],
        )
        row = milestones[milestones.Year == year].iloc[0]
        st.info(f"**{row.Year}** — {row.Milestone}")
        st.dataframe(milestones, hide_index=True, use_container_width=True)

    st.subheader("My learning curve")
    curve = pd.DataFrame(
        {"Skill points": np.cumsum([5, 10, 15, 20, 25, 30])},  # EDIT: illustrative numbers
        index=milestones["Year"],
    )
    st.line_chart(curve)

# ---------- SKILLS ----------
with tab_skills:
    st.header("Skills")
    filtered = skills_df[(skills_df.Category.isin(categories)) & (skills_df.Level >= min_level)]
    left, right = st.columns([1, 1], gap="large")
    with left:
        st.markdown(
            "I work across **frontend, backend, mobile, and desktop**. "
            "My strongest area is web development with Next.js and Supabase, "
            "and I like adding AI features with the Gemini API."
        )
        for _, r in filtered.sort_values("Level", ascending=False).head(5).iterrows():
            st.write(f"**{r.Skill}**")
            st.progress(int(r.Level) / 100)
        if show_table:
            st.dataframe(
                filtered,
                hide_index=True,
                use_container_width=True,
                column_config={
                    "Level": st.column_config.ProgressColumn("Level", min_value=0, max_value=100, format="%d")
                },
            )
    with right:
        chart_df = filtered.set_index("Skill")[["Level"]]
        if chart_df.empty:
            st.warning("No skills match the current sidebar filters.")
        elif chart_type == "Bar":
            st.bar_chart(chart_df)
        else:
            st.area_chart(chart_df)
        st.caption("Self-rated, out of 100.")

# ---------- PROJECTS ----------
with tab_projects:
    st.header("Projects")
    all_tools = sorted({t for tools in projects_df.Tools for t in tools})
    picked = st.multiselect("Filter by tool", all_tools)
    view = st.selectbox("Sort by", ["Title (A–Z)", "Title (Z–A)"])

    shown = projects_df.copy()
    if picked:
        shown = shown[shown.Tools.apply(lambda ts: any(t in ts for t in picked))]
    shown = shown.sort_values("Title", ascending=view.startswith("Title (A"))

    if shown.empty:
        st.warning("No projects use those tools.")
    cols = st.columns(2, gap="large")
    for i, (_, p) in enumerate(shown.iterrows()):
        with cols[i % 2]:
            with st.container(border=True):
                st.subheader(p.Title)
                st.markdown(f"**Role:** {p.Role}")
                st.markdown(
                    "**Tools:** " + "".join(f'<span class="tag">{t}</span>' for t in p.Tools),
                    unsafe_allow_html=True,
                )
                st.write(p.Outcome)
                st.link_button("View project", p.Link)

# ---------- CONTACT ----------
with tab_contact:
    st.header("Contact & Feedback")
    f1, f2 = st.columns([3, 2], gap="large")
    with f1:
        with st.form("feedback_form", clear_on_submit=True):
            name = st.text_input("Your name")
            email = st.text_input("Email")
            topic = st.radio("Topic", ["Feedback", "Collaboration", "Hiring", "Just saying hi"], horizontal=True)
            rating = st.slider("Rate this portfolio", 1, 5, 4)
            message = st.text_area("Message", height=140)
            subscribe = st.checkbox("Notify me about new projects")
            submitted = st.form_submit_button("Send message")

        if submitted:
            if not name.strip() or not message.strip():
                st.error("Please enter your name and a message.")
            else:
                st.session_state.feedback.append(
                    {"Date": date.today().isoformat(), "Name": name, "Email": email,
                     "Topic": topic, "Rating": rating, "Message": message, "Subscribe": subscribe}
                )
                st.success(f"Thanks, {name}! I got your {topic.lower()} message.")
                if rating >= 4:
                    st.balloons()

    with f2:
        st.subheader("Reach me")
        st.write("📧 your.email@example.com")      # EDIT
        st.write("💼 linkedin.com/in/your-profile")  # EDIT
        st.write("📍 Cebu City, Philippines")
        resume = (
            f"{NAME}\n{PROGRAM}\nCebu City, Philippines\n\nSKILLS\n"
            + "\n".join(f"- {r.Skill}: {r.Level}/100" for r in skills_df.itertuples())
            + "\n\nPROJECTS\n"
            + "\n".join(f"- {r.Title} ({r.Role}): {r.Outcome}" for r in projects_df.itertuples())
        )
        st.download_button("⬇️ Download resume summary (.txt)", resume, file_name="racaza_resume.txt")

    if st.session_state.feedback:
        st.subheader("Messages this session")
        fb = pd.DataFrame(st.session_state.feedback)
        st.dataframe(fb, hide_index=True, use_container_width=True)
        buf = io.StringIO()
        fb.to_csv(buf, index=False)
        st.download_button("Download feedback (.csv)", buf.getvalue(), file_name="racaza_feedback.csv")

st.divider()
st.caption(f"© {date.today().year} {NAME} · {COURSE_SECTION} · Built with Streamlit")