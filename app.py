import streamlit as st
from simtrain_eco_mini_app_streamlit_sdk.sdk import SimtrainEcoMiniAppStreamlitSdk
import pandas as pd

sdk = SimtrainEcoMiniAppStreamlitSdk()

st.title("Simtrain Eco Streamlit SDK Demo")

# ===================================== Navigate Page ====================================

if st.button("Go to Student Page"):
    sdk.ui.navigate_to("managestudents")


# ================================= Open On Screen Form ==================================

if st.button("Open Student On Screen Add New Form"):
    sdk.student.openOnScreenForm()


# ===================================== Student List =====================================

if st.button("Get Students"):
    sdk.student.list()

students = sdk.student.response("list")
if students:
    df = pd.DataFrame(students)[
        ["_id", "studentCode", "studentName", "alternateName", "gender"]
    ]
    st.table(df)
else:
    st.info("No found students.")


# ==================================== Student Detail ====================================

if st.button("Get Student 1"):
    sdk.student.detail(
        id="a2278689-7812-425d-a604-de27322cc2c1",
        options={"api_key": "student1"},
    )

student = sdk.student.response(
    action="detail",
    options={"api_key": "student1"},
)
if student:
    st.write(student)


if st.button("Get Student 2"):
    sdk.student.detail(
        id="da3b5fad-898e-45c1-a689-05585ebaac72",
        options={"api_key": "student2"},
    )

student = sdk.student.response(
    action="detail",
    options={"api_key": "student2"},
)
if student:
    st.write(student)

# ==================================== Create Student ====================================

if st.button("Create Student"):
    sdk.student.create(
        data={
            "studentName": "Student Create By Plugin",
            "alternateName": "MNLT7CM",
            "gender": "F",
            "email": "",
            "mobileNo": "+60123123423423",
            "icNumber": "123123897123",
            "barcode": "",
            "dob": "2025-05-16",
            "joinDate": "2025-05-16",
            "leaveDate": "",
            "status": "active",
            "stopDescription": "",
            "planReturnDate": "",
            "studentGroup": {
                "_id": "be8e961d-c5fc-4bd7-aaa1-5e2ee462f27d",
                "label": "Group 1",
                "code": "GRP-001",
            },
            "level": {
                "_id": "f81eef10-bbf5-4a9c-9106-1274aa5beb64",
                "code": "001",
                "label": "Level 1",
            },
            "race": {
                "_id": "b3967e7a-b80b-4304-a141-760cd8d988ed",
                "label": "Chinese",
                "code": "CHN",
            },
            "religion": {
                "_id": "b3dac518-d0c7-44b0-b9d3-5b604c89fbe8",
                "label": "Buddhism",
                "code": "BUD",
            },
            "school": {
                "_id": "c957b7fb-3337-4641-b42f-6366aab363b2",
                "label": "School 1",
                "code": "SCH-001",
            },
            "address": {
                "_id": "",
                "street1": "17 Jalan AAA",
                "street2": "Taman AAA",
                "postCode": "81100",
                "city": "Johor Bahru",
                "region": "Johor",
                "country": "Malaysia",
            },
            "area": {
                "_id": "4697493f-e465-468d-8473-587a611b8fd6",
                "label": "Area 1",
                "code": "AREA-001",
            },
            "parents": [],
            "docNoFormat": {
                "_id": "6349d2e7-b798-46d1-b7bb-407b3df34bcf",
                "label": "Default STU - HQ",
                "value": {
                    "_id": "6349d2e7-b798-46d1-b7bb-407b3df34bcf",
                    "label": "Default STU - HQ",
                },
            },
        }
    )

createStudent = sdk.student.response(
    action="create",
)
if createStudent:
    st.write(createStudent)

# ==================================== Delete Student ====================================

if st.button("Delete Student"):
    sdk.student.delete(id="6100f695-de04-4a62-95b5-627dc09fdd9d")

deleteStudent = sdk.student.response(
    action="delete",
)
if deleteStudent:
    st.write(deleteStudent)

# ==================================== Update Student ====================================

if st.button("Patch Student"):
    sdk.student.patch(
        id="43f15ddb-65db-41a6-a40c-e7e52658fc7c",
        data={"studentName": "[Updated] Student Create By Plugin"},
    )

patchStudent = sdk.student.response(
    action="patch",
)
if patchStudent:
    st.write(patchStudent)


# ================================ Student Auto Complete =================================

if st.button("Get Student Auto Complete"):
    sdk.student.autoComplete(query="T")

studentAutoComplete = sdk.student.response(
    action="autoComplete",
)
if studentAutoComplete:
    st.write(studentAutoComplete)


# =================================== Student Summary ====================================

if st.button("Get Student Summary"):
    sdk.student.getStudentSummary(id="43f15ddb-65db-41a6-a40c-e7e52658fc7c")

getStudentSummary = sdk.student.response(
    action="getStudentSummary",
)
if getStudentSummary:
    st.write(getStudentSummary)


# ================================== Teacher Commision ===================================

if st.button("Get Teacher Commision"):
    sdk.teacher.getTeacherCommissionResult("2025-05")

getTeacherCommissionResult = sdk.teacher.response(
    action="getTeacherCommissionResult",
)
if getTeacherCommissionResult:
    st.write(getTeacherCommissionResult)
