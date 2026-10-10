from extract import extract_pdf, extract_docx
from match import find_skills
from checks import check_length, check_sections, check_tables, check_tables_docx
import streamlit as st
st.title("Resume ATS Checker")
resume_file=st.file_uploader("upload your resume",type=["pdf","docx"])
jd_text=st.text_area("paste the job description")
analyze=st.button("Analyze")
if analyze:
    if resume_file is None or not jd_text.strip():
        st.warning("input is not valid")
    else:
        if resume_file.name.endswith(".pdf"):
            resume_text=extract_pdf(resume_file)
            is_pdf=True
        else:
            resume_text=extract_docx(resume_file)
            is_pdf=False
        jd_skills=find_skills(jd_text)
        resume_skills=find_skills(resume_text)
        matched=jd_skills & resume_skills
        missing=jd_skills - resume_skills
        if not jd_skills:
            st.warning("No known skills found in this job description")
        else:
            score=len(matched)/len(jd_skills)*100
            st.metric("Match score", f"{round(score)}%")
            st.write("Matched: " + (", ".join(sorted(matched)) or "none"))
            st.write("Missing: " + (", ".join(sorted(missing)) or "none"))
        st.subheader("formatting checks")
        warnings_found=False

        length_warning=check_length(resume_text)
        if length_warning:
            st.warning(length_warning)
            warnings_found=True
        
        missing_section=check_sections(resume_text)
        if missing_section:
            st.warning("Missing sections: " + ", ".join(missing_section))
            warnings_found=True
        resume_file.seek(0)
        if is_pdf:
            table_warning = check_tables(resume_file)
        else:
            table_warning = check_tables_docx(resume_file)
        if table_warning:
            st.warning(table_warning)
            warnings_found=True
        if not warnings_found:
            st.success("No formatting problems found")



