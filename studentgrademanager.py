import streamlit as st
import pandas as pd
from datetime import datetime
from html import escape


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.html(
    """
    <style>

    /* =========================
       MAIN APP
       ========================= */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef2ff 50%,
                #f8fafc 100%
            );
    }

    .main .block-container {
        max-width: 1450px;
        padding-top: 30px;
        padding-bottom: 50px;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* =========================
       HERO HEADER
       ========================= */

    .hero {
        background:
            linear-gradient(
                135deg,
                #4f46e5,
                #7c3aed,
                #9333ea
            );

        padding: 8px;

        border-radius: 26px;

        box-shadow:
            0 25px 60px rgba(79, 70, 229, 0.25);

        margin-bottom: 28px;
    }

    .hero-inner {
        background: rgba(255, 255, 255, 0.97);

        border-radius: 20px;

        padding: 30px 35px;
    }

    .hero-title {
        color: #111827;

        font-size: 34px;

        font-weight: 800;

        margin: 0;
    }

    .hero-description {
        color: #64748b;

        font-size: 15px;

        margin-top: 8px;

        margin-bottom: 0;
    }


    /* =========================
       SECTION TITLE
       ========================= */

    .section-title {
        color: #111827;

        font-size: 24px;

        font-weight: 800;

        margin-top: 10px;

        margin-bottom: 5px;
    }

    .section-description {
        color: #64748b;

        font-size: 14px;

        margin-bottom: 20px;
    }


    /* =========================
       STAT CARDS
       ========================= */

    .stat-card {
        background: white;

        border: 1px solid #e2e8f0;

        border-radius: 20px;

        padding: 22px;

        min-height: 145px;

        box-shadow:
            0 10px 30px rgba(15, 23, 42, 0.06);
    }

    .stat-icon {
        width: 45px;

        height: 45px;

        border-radius: 13px;

        background: #eef2ff;

        display: flex;

        align-items: center;

        justify-content: center;

        font-size: 22px;

        margin-bottom: 14px;
    }

    .stat-label {
        color: #64748b;

        font-size: 11px;

        font-weight: 800;

        text-transform: uppercase;

        letter-spacing: 0.7px;
    }

    .stat-number {
        color: #111827;

        font-size: 30px;

        font-weight: 800;

        margin-top: 5px;
    }


    /* =========================
       CARD
       ========================= */

    .card {
        background: white;

        border: 1px solid #e2e8f0;

        border-radius: 22px;

        padding: 25px;

        margin-top: 22px;

        box-shadow:
            0 10px 30px rgba(15, 23, 42, 0.05);
    }


    /* =========================
       STUDENT RECORD
       ========================= */

    .record-card {
        background: white;

        border: 1px solid #e2e8f0;

        border-radius: 24px;

        overflow: hidden;

        box-shadow:
            0 20px 50px rgba(15, 23, 42, 0.10);

        margin-top: 20px;
    }

    .record-header {
        background:
            linear-gradient(
                135deg,
                #4f46e5,
                #7c3aed
            );

        padding: 30px;
    }

    .record-label {
        color: #c7d2fe;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 1.5px;
    }

    .record-name {
        color: white;

        font-size: 30px;

        font-weight: 800;

        margin-top: 5px;
    }

    .record-subtitle {
        color: #ddd6fe;

        font-size: 14px;

        margin-top: 5px;
    }

    .record-body {
        padding: 28px;
    }


    /* =========================
       INFO BOX
       ========================= */

    .info-box {
        background: #f8fafc;

        border: 1px solid #e2e8f0;

        border-radius: 16px;

        padding: 17px;

        min-height: 85px;
    }

    .info-label {
        color: #64748b;

        font-size: 10px;

        font-weight: 800;

        text-transform: uppercase;

        letter-spacing: 0.6px;
    }

    .info-value {
        color: #111827;

        font-size: 16px;

        font-weight: 750;

        margin-top: 7px;
    }


    /* =========================
       RESULT BOX
       ========================= */

    .result-box {
        background: #f8fafc;

        border: 1px solid #e2e8f0;

        border-radius: 16px;

        padding: 18px;

        min-height: 100px;
    }

    .result-label {
        color: #64748b;

        font-size: 10px;

        font-weight: 800;

        text-transform: uppercase;

        letter-spacing: 0.7px;
    }

    .result-value {
        color: #111827;

        font-size: 25px;

        font-weight: 800;

        margin-top: 8px;
    }


    /* =========================
       PASS
       ========================= */

    .pass-box {
        background: #ecfdf5;

        border: 1px solid #a7f3d0;

        border-radius: 16px;

        padding: 18px;

        min-height: 100px;
    }

    .pass-box .result-label {
        color: #059669;
    }

    .pass-box .result-value {
        color: #047857;
    }


    /* =========================
       FAIL
       ========================= */

    .fail-box {
        background: #fef2f2;

        border: 1px solid #fecaca;

        border-radius: 16px;

        padding: 18px;

        min-height: 100px;
    }

    .fail-box .result-label {
        color: #dc2626;
    }

    .fail-box .result-value {
        color: #b91c1c;
    }


    /* =========================
       EMPTY STATE
       ========================= */

    .empty-state {
        text-align: center;

        background: white;

        border: 1px solid #e2e8f0;

        border-radius: 22px;

        padding: 50px;

        color: #64748b;

        margin-top: 20px;
    }

    .empty-icon {
        font-size: 45px;

        margin-bottom: 10px;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;

        color: #94a3b8;

        font-size: 12px;

        margin-top: 45px;
    }


    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 768px) {

        .hero-title {
            font-size: 25px;
        }

        .record-name {
            font-size: 24px;
        }

        .main .block-container {
            padding-left: 15px;
            padding-right: 15px;
        }

    }

    </style>
    """,
)


# ============================================================
# SESSION STATE
# ============================================================

if "students" not in st.session_state:

    st.session_state.students = [
        {
            "roll": "STU001",
            "name": "Raja Kumar",
            "class_name": "Grade 10",
            "section": "A",
            "gender": "Male",
            "math": 85,
            "science": 90,
            "english": 78,
            "social": 82,
            "computer": 88,
        },
        {
            "roll": "STU002",
            "name": "Priya Sharma",
            "class_name": "Grade 10",
            "section": "A",
            "gender": "Female",
            "math": 92,
            "science": 88,
            "english": 94,
            "social": 90,
            "computer": 96,
        },
        {
            "roll": "STU003",
            "name": "Arun Kumar",
            "class_name": "Grade 10",
            "section": "B",
            "gender": "Male",
            "math": 65,
            "science": 70,
            "english": 62,
            "social": 68,
            "computer": 75,
        },
        {
            "roll": "STU004",
            "name": "Meena Devi",
            "class_name": "Grade 10",
            "section": "B",
            "gender": "Female",
            "math": 45,
            "science": 58,
            "english": 62,
            "social": 55,
            "computer": 60,
        },
    ]


if "selected_roll" not in st.session_state:
    st.session_state.selected_roll = "STU001"


# ============================================================
# FUNCTIONS
# ============================================================

def calculate_result(student):

    marks = [
        student["math"],
        student["science"],
        student["english"],
        student["social"],
        student["computer"],
    ]

    total = sum(marks)

    percentage = total / len(marks)

    passed = all(mark >= 35 for mark in marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 35:
        grade = "E"
    else:
        grade = "F"

    return total, percentage, grade, passed


def find_student(roll_number):

    for student in st.session_state.students:

        if student["roll"].upper() == roll_number.upper():
            return student

    return None


def delete_student(roll_number):

    st.session_state.students = [
        student
        for student in st.session_state.students
        if student["roll"] != roll_number
    ]

    if st.session_state.students:

        st.session_state.selected_roll = (
            st.session_state.students[0]["roll"]
        )

    else:

        st.session_state.selected_roll = None


# ============================================================
# HERO
# ============================================================

Herohtml = """
<div class="hero-inner">
    <div class="hero-title">
       🎓 Student Grade Manager
    </div>
    <div class="hero-description">
       Manage students, marks, grades and academic performance from one modern dashboard.
    </div>
</div>
"""

st.html(Herohtml)


# ============================================================
# CALCULATE DASHBOARD DATA
# ============================================================

students = st.session_state.students

total_students = len(students)

if students:

    results = [
        calculate_result(student)
        for student in students
    ]

    average_percentage = (
        sum(result[1] for result in results)
        / len(results)
    )

    passed_students = sum(
        1
        for result in results
        if result[3]
    )

    failed_students = (
        total_students - passed_students
    )

else:

    average_percentage = 0

    passed_students = 0

    failed_students = 0


# ============================================================
# TABS
# ============================================================

dashboard_tab, details_tab, add_tab = st.tabs(
    [
        "📊 Dashboard",
        "🎓 Student Details",
        "➕ Add Student",
    ]
)


# ============================================================
# DASHBOARD TAB
# ============================================================

with dashboard_tab:

    st.html(
        """
        <div class="section-title">
            Dashboard Overview
        </div>

        <div class="section-description">
            Monitor student performance and academic results.
        </div>
        """,
    )


    # --------------------------------------------------------
    # STATISTICS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        tsudents = f"""
            <div class="stat-card">

                <div class="stat-icon">
                    👨‍🎓
                </div>

                <div class="stat-label">
                    Total Students
                </div>

                <div class="stat-number">
                    {total_students}
                </div>

            </div>
            """ 
        st.html(tsudents)


    with col2:

        html_code1 = f"""
        
            <div class="stat-card">

                <div class="stat-icon">
                    📊
                </div>

                <div class="stat-label">
                    Average
                </div>

                <div class="stat-number">
                    {average_percentage:.1f}%
                </div>

            </div>
            """
        st.html(html_code1)
         


    with col3:

        spass = f"""
            <div class="stat-card">

                <div class="stat-icon">
                    ✅
                </div>

                <div class="stat-label">
                    Passed
                </div>

                <div class="stat-number">
                    {passed_students}
                </div>

            </div>
            """
        st.html(spass)
        


    with col4:

        sresult = f"""
           <div class="stat-card">

                <div class="stat-icon">
                    ❌
                </div>

                <div class="stat-label">
                    Failed
                </div>

                <div class="stat-number">
                    {failed_students}
                </div>

            </div>
            """
        st.html(sresult)


    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    srecord = f"""
        <div class="card">

            <div class="section-title">
                Student Records
            </div>

            <div class="section-description">
                Search students by name or roll number.
            </div>

        </div>
        """ 
    st.html(srecord)


    search_text = st.text_input(
        "Search",
        placeholder="🔍 Search by student name or roll number",
        label_visibility="collapsed",
    )


    if search_text:

        query = search_text.strip().lower()

        filtered_students = [
            student
            for student in students
            if (
                query in student["name"].lower()
                or
                query in student["roll"].lower()
            )
        ]

    else:

        filtered_students = students


    # --------------------------------------------------------
    # TABLE
    # --------------------------------------------------------

    if filtered_students:

        table_rows = []

        for student in filtered_students:

            total, percentage, grade, passed = (
                calculate_result(student)
            )

            table_rows.append(
                {
                    "Roll Number": student["roll"],
                    "Student Name": student["name"],
                    "Class": student["class_name"],
                    "Section": student["section"],
                    "Total": f"{total}/500",
                    "Percentage": f"{percentage:.1f}%",
                    "Grade": grade,
                    "Status": "PASS" if passed else "FAIL",
                }
            )


        table_df = pd.DataFrame(table_rows)


        st.dataframe(
            table_df,
            width="stretch",
            hide_index=True,
        )


        # ----------------------------------------------------
        # SELECT STUDENT
        # ----------------------------------------------------

        st.markdown("### 🔎 Select Student")


        available_rolls = [
            student["roll"]
            for student in filtered_students
        ]


        selected_dashboard_roll = st.selectbox(
            "Roll Number",
            available_rolls,
            key="dashboard_student_select",
        )


        if st.button(
            "🎓 View Student Record",
            width="stretch",
            type="primary",
        ):

            st.session_state.selected_roll = (
                selected_dashboard_roll
            )

            st.success(
                f"Student {selected_dashboard_roll} selected. "
                "Open the Student Details tab."
            )


    else:

        ssearch = f"""
        
            <div class="empty-state">

                <div class="empty-icon">
                    🔍
                </div>

                <strong>
                    No students found
                </strong>

                <br>

                Try another student name or roll number.

            </div>
            """ 
        st.html(ssearch)
          


# ============================================================
# STUDENT DETAILS TAB
# ============================================================

with details_tab:

    st.html(
        """
        <div class="section-title">
            Student Details
        </div>

        <div class="section-description">
            Select a roll number to view the complete
            student record.
        </div>
        """,
    )


    if students:

        roll_numbers = [
            student["roll"]
            for student in students
        ]


        if (
            st.session_state.selected_roll
            in roll_numbers
        ):

            default_index = roll_numbers.index(
                st.session_state.selected_roll
            )

        else:

            default_index = 0


        selected_roll = st.selectbox(
            "Select Roll Number",
            roll_numbers,
            index=default_index,
            key="details_student_select",
        )


        st.session_state.selected_roll = selected_roll


        student = find_student(selected_roll)


        if student:

            total, percentage, grade, passed = (
                calculate_result(student)
            )


            # ------------------------------------------------
            # RECORD CARD
            # ------------------------------------------------

            arecord = f"""
                
                <div class="record-card">

                    <div class="record-header">

                        <div class="record-label">
                            ACADEMIC RECORD
                        </div>

                        <div class="record-name">
                            {escape(str(student["name"]))}
                        </div>

                        <div class="record-subtitle">
                            Roll Number: {escape(str(student["roll"]))}
                            &nbsp; • &nbsp;
                            {escape(str(student["class_name"]))}
                            &nbsp; • &nbsp;
                            Section {escape(str(student["section"]))}
                        </div>

                    </div>

                    <div class="record-body">

                        <div style="
                            display:grid;
                            grid-template-columns:
                            repeat(4, minmax(0, 1fr));
                            gap:15px;
                        ">

                            <div class="info-box">

                                <div class="info-label">
                                    Roll Number
                                </div>

                                <div class="info-value">
                                    {escape(str(student["roll"]))}
                                </div>

                            </div>


                            <div class="info-box">

                                <div class="info-label">
                                    Class
                                </div>

                                <div class="info-value">
                                    {escape(str(student["class_name"]))}
                                </div>

                            </div>


                            <div class="info-box">

                                <div class="info-label">
                                    Section
                                </div>

                                <div class="info-value">
                                    {escape(str(student["section"]))}
                                </div>

                            </div>


                            <div class="info-box">

                                <div class="info-label">
                                    Gender
                                </div>

                                <div class="info-value">
                                    {escape(str(student["gender"]))}
                                </div>

                            </div>

                        </div>

                    </div>

                </div>
                """ 
            st.html(arecord)
            


            # ------------------------------------------------
            # STUDENT INFORMATION
            # ------------------------------------------------

            st.markdown("### 👤 Student Information")


            info1, info2, info3 = st.columns(3)


            with info1:

                st.html(
                    f"""
                    <div class="info-box">

                        <div class="info-label">
                            Student Name
                        </div>

                        <div class="info-value">
                            {escape(str(student["name"]))}
                        </div>

                    </div>
                    """,
                )


            with info2:

                st.html(
                    f"""
                    <div class="info-box">

                        <div class="info-label">
                            Academic Year
                        </div>

                        <div class="info-value">
                            2026 - 2027
                        </div>

                    </div>
                    """,
                )


            with info3:

                st.html(
                    f"""
                    <div class="info-box">

                        <div class="info-label">
                            Report Date
                        </div>

                        <div class="info-value">
                            {datetime.now().strftime("%d %b %Y")}
                        </div>

                    </div>
                    """,
                )


            # ------------------------------------------------
            # SUBJECT PERFORMANCE
            # ------------------------------------------------

            st.markdown("### 📚 Subject Performance")


            subject_rows = [
                {
                    "Subject": "Mathematics",
                    "Marks": student["math"],
                    "Maximum": 100,
                    "Status": (
                        "PASS"
                        if student["math"] >= 35
                        else "FAIL"
                    ),
                },
                {
                    "Subject": "Science",
                    "Marks": student["science"],
                    "Maximum": 100,
                    "Status": (
                        "PASS"
                        if student["science"] >= 35
                        else "FAIL"
                    ),
                },
                {
                    "Subject": "English",
                    "Marks": student["english"],
                    "Maximum": 100,
                    "Status": (
                        "PASS"
                        if student["english"] >= 35
                        else "FAIL"
                    ),
                },
                {
                    "Subject": "Social Science",
                    "Marks": student["social"],
                    "Maximum": 100,
                    "Status": (
                        "PASS"
                        if student["social"] >= 35
                        else "FAIL"
                    ),
                },
                {
                    "Subject": "Computer Science",
                    "Marks": student["computer"],
                    "Maximum": 100,
                    "Status": (
                        "PASS"
                        if student["computer"] >= 35
                        else "FAIL"
                    ),
                },
            ]


            subject_df = pd.DataFrame(subject_rows)


            st.dataframe(
                subject_df,
                width="stretch",
                hide_index=True,
            )


            # ------------------------------------------------
            # RESULT SUMMARY
            # ------------------------------------------------

            st.markdown("### 📊 Result Summary")


            result1, result2, result3, result4 = (
                st.columns(4)
            )


            with result1:

                st.html(
                    f"""
                    <div class="result-box">

                        <div class="result-label">
                            Total Marks
                        </div>

                        <div class="result-value">
                            {total} / 500
                        </div>

                    </div>
                    """,
                )


            with result2:

                st.html(
                    f"""
                    <div class="result-box">

                        <div class="result-label">
                            Percentage
                        </div>

                        <div class="result-value">
                            {percentage:.1f}%
                        </div>

                    </div>
                    """,
                )


            with result3:

                st.html(
                    f"""
                    <div class="result-box">

                        <div class="result-label">
                            Grade
                        </div>

                        <div class="result-value">
                            {grade}
                        </div>

                    </div>
                    """,
                )


            with result4:

                if passed:

                    st.html(
                        """
                        <div class="pass-box">

                            <div class="result-label">
                                RESULT
                            </div>

                            <div class="result-value">
                                ✓ PASS
                            </div>

                        </div>
                        """,
                    )

                else:

                    st.html(
                        """
                        <div class="fail-box">

                            <div class="result-label">
                                RESULT
                            </div>

                            <div class="result-value">
                                ✕ FAIL
                            </div>

                        </div>
                        """,
                    )


            # ------------------------------------------------
            # ACTIONS
            # ------------------------------------------------

            st.markdown("---")


            action1, action2 = st.columns(2)


            with action1:

                if st.button(
                    "🖨️ Print / Save Record",
                    width="stretch",
                ):

                    st.info(
                        "Press Ctrl + P in your browser "
                        "to print or save the record as PDF."
                    )


            with action2:

                if st.button(
                    "🗑️ Delete Student",
                    width="stretch",
                ):

                    delete_student(selected_roll)

                    st.success(
                        "Student deleted successfully."
                    )

                    st.rerun()


    else:

        st.html(
            """
            <div class="empty-state">

                <div class="empty-icon">
                    🎓
                </div>

                <strong>
                    No students available
                </strong>

                <br>

                Add a student using the
                <strong>Add Student</strong> tab.

            </div>
            """,
        )


# ============================================================
# ADD STUDENT TAB
# ============================================================

with add_tab:

    st.html(
        """
        <div class="section-title">
            Add New Student
        </div>

        <div class="section-description">
            Enter student details and subject marks.
        </div>
        """,
    )


    with st.form("student_form"):

        st.markdown("### 👤 Student Information")


        col1, col2, col3 = st.columns(3)


        with col1:

            roll = st.text_input(
                "Roll Number",
                placeholder="Example: STU005",
            )


        with col2:

            name = st.text_input(
                "Student Name",
                placeholder="Enter full name",
            )


        with col3:

            gender = st.selectbox(
                "Gender",
                [
                    "Male",
                    "Female",
                    "Other",
                ],
            )


        col4, col5 = st.columns(2)


        with col4:

            class_name = st.selectbox(
                "Class",
                [
                    "Grade 6",
                    "Grade 7",
                    "Grade 8",
                    "Grade 9",
                    "Grade 10",
                    "Grade 11",
                    "Grade 12",
                ],
            )


        with col5:

            section = st.selectbox(
                "Section",
                [
                    "A",
                    "B",
                    "C",
                    "D",
                ],
            )


        st.markdown("### 📚 Subject Marks")


        mark1, mark2, mark3 = st.columns(3)


        with mark1:

            math = st.number_input(
                "Mathematics",
                min_value=0,
                max_value=100,
                value=0,
                step=1,
            )


        with mark2:

            science = st.number_input(
                "Science",
                min_value=0,
                max_value=100,
                value=0,
                step=1,
            )


        with mark3:

            english = st.number_input(
                "English",
                min_value=0,
                max_value=100,
                value=0,
                step=1,
            )


        mark4, mark5 = st.columns(2)


        with mark4:

            social = st.number_input(
                "Social Science",
                min_value=0,
                max_value=100,
                value=0,
                step=1,
            )


        with mark5:

            computer = st.number_input(
                "Computer Science",
                min_value=0,
                max_value=100,
                value=0,
                step=1,
            )


        st.markdown("")


        submitted = st.form_submit_button(
            "➕ Add Student",
            width="stretch",
            type="primary",
        )


        if submitted:

            clean_roll = roll.strip().upper()

            clean_name = name.strip()


            if not clean_roll:

                st.error(
                    "Please enter the Roll Number."
                )


            elif not clean_name:

                st.error(
                    "Please enter the Student Name."
                )


            elif find_student(clean_roll):

                st.error(
                    f"Roll number {clean_roll} already exists."
                )


            else:

                new_student = {
                    "roll": clean_roll,
                    "name": clean_name,
                    "class_name": class_name,
                    "section": section,
                    "gender": gender,
                    "math": math,
                    "science": science,
                    "english": english,
                    "social": social,
                    "computer": computer,
                }


                st.session_state.students.append(
                    new_student
                )


                st.session_state.selected_roll = (
                    clean_roll
                )


                st.success(
                    f"🎉 {clean_name} added successfully!"
                )


# ============================================================
# FOOTER
# ============================================================

html_code = """
    
    <div class="footer">
        🎓 Student Grade Manager
        &nbsp; • &nbsp;
        Modern Academic Management Dashboard
        &nbsp; • &nbsp;
        Built with Streamlit
    </div>
    """
    
st.html(html_code)
