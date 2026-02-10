import streamlit as st
import base64
import os
import fitz  # PyMuPDF
from io import BytesIO

# Function to convert PDF to image (base64)
@st.cache_data
def get_pdf_as_image(pdf_path, rotate=0):
    if os.path.exists(pdf_path):
        try:
            doc = fitz.open(pdf_path)
            page = doc[0]  # First page
            if rotate:
                page.set_rotation(rotate)
            # Render at higher resolution for clarity
            mat = fitz.Matrix(3, 3)  # 3x zoom for larger image
            pix = page.get_pixmap(matrix=mat)
            img_bytes = pix.tobytes("png")
            doc.close()
            return base64.b64encode(img_bytes).decode('utf-8')
        except Exception as e:
            print(f"Error loading {pdf_path}: {e}")
            return None
    return None

# Load certificate PDFs - use certificates folder in same directory as app.py
app_dir = os.path.dirname(os.path.abspath(__file__))
cert_dir = os.path.join(app_dir, "certificates")

cert_files = {
    "jpmorgan": os.path.join(cert_dir, "jpmorgan.pdf"),
    "sql_basic": os.path.join(cert_dir, "sql_basic.pdf"),
    "sql_int": os.path.join(cert_dir, "sql_intermediate.pdf"),
    "python": os.path.join(cert_dir, "python.pdf"),
    "gitex": os.path.join(cert_dir, "gitex.pdf")
}

# Page configuration
st.set_page_config(
    page_title="Dhruv Naveen - Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1E3A8A;
        border-bottom: 3px solid #3B82F6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .skill-badge {
        display: inline-block;
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        margin: 0.2rem;
        font-size: 0.9rem;
    }
    .contact-info {
        background-color: #EFF6FF;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    
    /* Hover tooltip for projects */
    .project-hover {
        position: relative;
        background-color: #F8FAFC;
        border-left: 4px solid #3B82F6;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 0 8px 8px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        z-index: 1;
    }
    .project-hover:hover {
        background-color: #EFF6FF;
        transform: translateX(5px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 1000;
    }
    .project-hover .tooltip {
        visibility: hidden;
        opacity: 0;
        position: absolute;
        left: 0;
        bottom: 100%;
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        z-index: 9999;
        transition: all 0.3s ease;
        font-size: 0.9rem;
        line-height: 1.5;
        box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.3);
    }
    .project-hover:hover .tooltip {
        visibility: visible;
        opacity: 1;
    }
    
    /* Hover tooltip for certifications with PDF preview */
    .cert-hover {
        position: relative;
        background-color: #F0FDF4;
        border-left: 4px solid #22C55E;
        padding: 1rem;
        margin-bottom: 0.8rem;
        border-radius: 0 8px 8px 0;
        color: #166534;
        cursor: pointer;
        transition: all 0.3s ease;
        z-index: 1;
    }
    .cert-hover:hover {
        background-color: #DCFCE7;
        transform: translateX(5px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 1000;
    }
    .cert-hover .cert-preview {
        visibility: hidden;
        opacity: 0;
        position: fixed;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        max-width: 90vw;
        max-height: 85vh;
        background-color: white;
        border-radius: 12px;
        z-index: 99999;
        transition: all 0.3s ease;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        padding: 15px;
    }
    .cert-hover:hover .cert-preview {
        visibility: visible;
        opacity: 1;
    }
    .cert-hover .cert-preview img {
        max-width: 85vw;
        max-height: 80vh;
        border-radius: 8px;
        object-fit: contain;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar - Profile Section
with st.sidebar:
    st.markdown("### 📷 Profile")
    st.markdown("""
    <div style="width: 150px; height: 150px; background-color: #E5E7EB; 
                border-radius: 50%; display: flex; align-items: center; 
                justify-content: center; margin: auto;">
        <span style="color: #6B7280; font-size: 3rem;">👤</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Contact Info in Sidebar
    st.markdown("### 📬 Contact")
    st.markdown("📧 **Email:**")
    st.code("dhruv.bs25ddx019@spjain.org", language=None)
    st.markdown("📱 **Phone:**")
    st.code("+91 9066677794", language=None)
    st.markdown("🔗 **LinkedIn:**")
    st.markdown("[Connect on LinkedIn](https://linkedin.com)")

# Main Content
# Header
st.markdown('<p class="main-header">DHRUV NAVEEN</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Data Science Graduate | Python Developer | ML Enthusiast</p>', unsafe_allow_html=True)

# Summary Section
st.markdown('<p class="section-header">📋 Summary</p>', unsafe_allow_html=True)
st.markdown("""
Results-driven Data Science graduate with **Distinction** in Bachelor's degree, equipped with strong skills in 
**Python, machine learning, and data analysis**. Gained hands-on experience through academic projects and 
internships involving predictive modelling, data wrangling, and data visualization. Eager to apply data-driven 
insights to solve real-world problems and contribute to a dynamic, collaborative team environment.
""")

# Two columns for Education and Skills
col1, col2 = st.columns(2)

with col1:
    # Education Section
    st.markdown('<p class="section-header">🎓 Education</p>', unsafe_allow_html=True)
    st.markdown("""
    **SP Jain School of Global Management**  
    📍 Sydney, Australia  
    📅 Sept 2025 - Jun 2028  
    
    🎯 **Bachelor of Data Science**
    
    **Relevant Coursework:**
    - ⭐ 5 Star in HackerRank Python
    """)

with col2:
    # Skills Section
    st.markdown('<p class="section-header">🛠️ Skills</p>', unsafe_allow_html=True)
    
    st.markdown("**Programming & Tools:**")
    skills_prog = ["Python", "SQL", "Excel", "Git", "Java", "Maven"]
    st.markdown(" ".join([f'<span class="skill-badge">{skill}</span>' for skill in skills_prog]), unsafe_allow_html=True)
    
    st.markdown("**Libraries:**")
    skills_lib = ["Pandas", "NumPy", "Keras", "Matplotlib", "Spring", "Spring Framework"]
    st.markdown(" ".join([f'<span class="skill-badge">{skill}</span>' for skill in skills_lib]), unsafe_allow_html=True)
    
    st.markdown("**Databases & Cloud:**")
    skills_db = ["MySQL", "AWS", "Azure", "SQL Database"]
    st.markdown(" ".join([f'<span class="skill-badge">{skill}</span>' for skill in skills_db]), unsafe_allow_html=True)
    
    st.markdown("**System Design:**")
    skills_sys = ["Kafka", "REST API"]
    st.markdown(" ".join([f'<span class="skill-badge">{skill}</span>' for skill in skills_sys]), unsafe_allow_html=True)
    
    st.markdown("**Soft Skills:**")
    skills_soft = ["Communication", "Problem Solving", "Project Management", "Research"]
    st.markdown(" ".join([f'<span class="skill-badge">{skill}</span>' for skill in skills_soft]), unsafe_allow_html=True)

# Projects Section
st.markdown('<p class="section-header">💼 Projects</p>', unsafe_allow_html=True)

# Project cards with hover tooltips
st.markdown("""
<div class="project-hover">
    <strong>📚 Attendance Management System</strong> - Class 12 Project
    <div class="tooltip">
        <strong>Key Features:</strong><br>
        • Digitized attendance records for easy accessibility<br>
        • Grade viewing functionality<br>
        • Fee tracking system<br>
        • Assignment management<br><br>
        <strong>Impact:</strong> Simplified administrative tasks for teachers and enhanced transparency for students.
    </div>
</div>

<div class="project-hover">
    <strong>🔬 Physics Research Paper</strong> - Archimedes Principle
    <div class="tooltip">
        <strong>Extended Essay (~4,000 words)</strong><br><br>
        <em>Investigating the factors affecting the displaced volume and apparent weight in an Archimedes principle experiment</em><br><br>
        • Primary data collected manually<br>
        • Analysis of nearly 125 distinct datasets<br>
        • Rigorous data collection with systematic analysis
    </div>
</div>

<div class="project-hover">
    <strong>📊 Math Internal Assessment</strong> - Bayesian Weather Prediction
    <div class="tooltip">
        <strong>Research Question:</strong><br>
        <em>How accurately can Bayesian probability predict rainfall in Bengaluru?</em><br><br>
        • Analyzed historical weather forecast data<br>
        • Applied Bayes' theorem principles<br>
        • Constructed probabilistic prediction model
    </div>
</div>

<div class="project-hover">
    <strong>💻 JPMorgan Chase</strong> - Software Engineering Simulation (Forage, Jan 2026)
    <div class="tooltip">
        <strong>Technical Implementation:</strong><br>
        ✅ Integrated Kafka into Spring Boot microservice<br>
        ✅ Implemented transaction validation with Spring Data JPA<br>
        ✅ Connected to external REST Incentive API<br>
        ✅ Developed REST endpoint for querying user balances<br>
        ✅ Verified system behavior using Maven test suites<br><br>
        <strong>Tech:</strong> Spring Boot, Kafka, H2 SQL, REST API, Maven
    </div>
</div>
""", unsafe_allow_html=True)

# Certifications Section
st.markdown('<p class="section-header">🏆 Certifications</p>', unsafe_allow_html=True)

cert_col1, cert_col2 = st.columns(2)

# Load PDFs as images (JPMorgan rotated 90 degrees)
jpmorgan_img = get_pdf_as_image(cert_files["jpmorgan"], rotate=90)
sql_basic_img = get_pdf_as_image(cert_files["sql_basic"])
sql_int_img = get_pdf_as_image(cert_files["sql_int"])
python_img = get_pdf_as_image(cert_files["python"])
gitex_img = get_pdf_as_image(cert_files["gitex"])

with cert_col1:
    if jpmorgan_img:
        st.markdown(f'''
        <div class="cert-hover">
            <strong>🏅 JPMorgan Chase</strong> - Software Engineering (2026)
            <div class="cert-preview">
                <img src="data:image/png;base64,{jpmorgan_img}" alt="JPMorgan Certificate">
            </div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="cert-hover">
            <strong>🏅 JPMorgan Chase</strong> - Software Engineering (2026)
        </div>
        ''', unsafe_allow_html=True)
    
    if sql_basic_img:
        st.markdown(f'''
        <div class="cert-hover">
            <strong>🏅 HackerRank</strong> - SQL Basic (2025)
            <div class="cert-preview">
                <img src="data:image/png;base64,{sql_basic_img}" alt="SQL Basic Certificate">
            </div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="cert-hover">
            <strong>🏅 HackerRank</strong> - SQL Basic (2025)
        </div>
        ''', unsafe_allow_html=True)
    
    if sql_int_img:
        st.markdown(f'''
        <div class="cert-hover">
            <strong>🏅 HackerRank</strong> - SQL Intermediate (2025)
            <div class="cert-preview">
                <img src="data:image/png;base64,{sql_int_img}" alt="SQL Intermediate Certificate">
            </div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="cert-hover">
            <strong>🏅 HackerRank</strong> - SQL Intermediate (2025)
        </div>
        ''', unsafe_allow_html=True)

with cert_col2:
    if python_img:
        st.markdown(f'''
        <div class="cert-hover">
            <strong>🏅 Edcept</strong> - Python (2023)
            <div class="cert-preview">
                <img src="data:image/png;base64,{python_img}" alt="Python Certificate">
            </div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="cert-hover">
            <strong>🏅 Edcept</strong> - Python (2023)
        </div>
        ''', unsafe_allow_html=True)
    
    if gitex_img:
        st.markdown(f'''
        <div class="cert-hover">
            <strong>🏅 GITEX Global 2025</strong> - Student Delegate
            <div class="cert-preview">
                <img src="data:image/png;base64,{gitex_img}" alt="GITEX Certificate">
            </div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="cert-hover">
            <strong>🏅 GITEX Global 2025</strong> - Student Delegate
        </div>
        ''', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; padding: 1rem;">
    <p>📧 dhruv.bs25ddx019@spjain.org | 📱 +91 9066677794</p>
</div>
""", unsafe_allow_html=True)
