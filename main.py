import streamlit as st
import pandas as pd
import sqlite3
import os

st.title("Monthly Records Of Lakhanpur Health Post")


# caste_dict={'01':'Dalit','02':'Janjati','03':'Madheshi','04':'Muslim','05':'Brahman','06':'Other'}
st.header("Cards are:")

# --- Summary Cards for Total Male, Female, and TV Patients ---
if os.path.exists("manshir_records.csv"):
    df_summary = pd.read_csv("manshir_records.csv")

    total_count=len(df_summary)
    total_male = df_summary[df_summary['Gender'] == 'Male'].shape[0]
    total_female = df_summary[df_summary['Gender'] == 'Female'].shape[0]
    total_Dalit=df_summary[df_summary['Cast Code']=='Dalit'].shape[0]
    total_Janjati=df_summary[df_summary['Cast Code']=='Janjati'].shape[0]
    total_Madheshi=df_summary[df_summary['Cast Code']=='Madheshi'].shape[0]
    total_Muslim=df_summary[df_summary['Cast Code']=='Muslim'].shape[0]
    total_Brahman=df_summary[df_summary['Cast Code']=='Brahman'].shape[0]
    total_Other=df_summary[df_summary['Cast Code']=='Other'].shape[0]

    st.subheader("Total count , Total Male and Total Female:")
    colA,col1, col2= st.columns(3)
    
    with colA:
         st.metric(label="Today Total Records   :", value=total_count)

    with col1:
        st.metric(label="Total Male Patients", value=total_male)


    with col2:
        st.metric(label="Total Female Patients", value=total_female)


    st.subheader("Total No ( 1.Dalit 2.Janjati 3.Madheshi 4.Muslim 5.Brahman 6.Other)")
    col3, col4,col5,col6,col7,col8= st.columns(6)
    
    with col3:
        st.metric(label="1.Total Dalit", value=total_Dalit)

    with col4:
         st.metric(label="2.Total Janjati", value=total_Janjati)

    with col5:
        st.metric(label="3.Total Madheshi", value=total_Madheshi)


    with col6:
        st.metric(label="4.Total Muslim", value=total_Muslim)


    with col7:
        st.metric(label="5.Total Brahman", value=total_Brahman)

    with col8:
         st.metric(label="6.Other", value=total_Other)
        
else:
    st.info("No records available to display summary.")

 



# File name to store records (ensure this is defined before any use)
csv_file = "manshir_records.csv"


# --- Existing code above ---

st.header("Download All Stored Records as CSV")

if os.path.exists(csv_file):
    all_data = pd.read_csv(csv_file)
    st.dataframe(all_data)

    csv_export = all_data.to_csv(index=False).encode()
    st.download_button(
        label="Download Full Records CSV",
        data=csv_export,
        file_name="all_manshir_records.csv",
        mime="text/csv"
    )
else:
    st.info("No records found to download.")



st.header("Enter Today Date:")

# Date selection (Day, Month, Year - Nepali Calendar)
col1, col2, col3 = st.columns(3)

with col1:
    day = st.number_input("Day", min_value=1, max_value=32, step=1)

with col2:
    month = st.selectbox(
        "Month (Nepali Calendar)",
        [
            "Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
            "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"
        ]
    )

with col3:
    year = st.number_input("Year (B.S.)", min_value=2000, max_value=2082, step=1)

st.write(f"### Selected Date: {day} {month}, {year}")

caste_dict={'01:Dalit':'Dalit','02:Janjati':'Janjati','03:Madheshi':'Madheshi','04:Muslim':'Muslim','05:Brahman':'Brahman','06:Other':'Other'}


st.header("Patient Information Form")
# Input fields
master_reg_no = st.text_input("Master Registration Number")
opd_type = st.selectbox("OPD Type", ["Old", "New"])
if opd_type=="New":
    opd_type=st.text_input('Enter New OPD Number:')
patient_name = st.text_input("Patient's Name")
cast_code = st.selectbox("Cast Code", ["01:Dalit","02:Janjati","03:Madheshi","04:Muslim","05:Brahman","06:Other"])
age = st.number_input("Age", min_value=0, max_value=120, step=1,value=25)
gender = st.radio("Gender", ["Female", "Male", "Other"])
municipality = st.selectbox("Municipality", ["Sakhuwa Parshauni"])
expect_tv = st.radio("Expect TV Patients", ["No", "Yes"])

# File name for storing the data
csv_file ="manshir_records.csv"

if st.button("Save Record"):
    data = {
        "Master Registration Number": master_reg_no,
        "OPD Type": opd_type,
        "Patient Name": patient_name,
        "Cast Code": caste_dict[cast_code],
        "Age": age,
        "Gender": gender,
        "Municipality": municipality,
        "Expect TV": expect_tv,
    }

    df = pd.DataFrame([data])

    # Save to CSV
    if not os.path.exists(csv_file):
        df.to_csv(csv_file, index=False)
    else:
        df.to_csv(csv_file, mode='a', header=False, index=False)

    st.success("Record saved successfully!")

st.header("Combine Multiple CSV Files (Using SQL UNION ALL)")
uploaded_files = st.file_uploader("Upload multiple CSV files", type=["csv"], accept_multiple_files=True)

if st.button("Combine Files"):
    if uploaded_files:
        # Create in-memory SQLite DB
        conn = sqlite3.connect(":memory:")
        combined_df = pd.DataFrame()

        for i, file in enumerate(uploaded_files):
            df = pd.read_csv(file)
            table_name = f"table_{i}"
            df.to_sql(table_name, conn, index=False, if_exists='replace')

        # Create SQL UNION ALL query
        query_parts = [f"SELECT * FROM table_{i}" for i in range(len(uploaded_files))]
        final_query = " UNION ALL ".join(query_parts)

        combined_df = pd.read_sql_query(final_query, conn)

        st.write("### Combined Data")
        st.dataframe(combined_df)

        # Export combined CSV
        combined_df.to_csv("combined_records.csv", index=False)
        st.success("Combined CSV created as 'combined_records.csv'")
    else:
        st.error("Please upload at least one CSV file.")
st.subheader("Clear All Records")

if st.button("Clear Records"):
    if os.path.exists(csv_file):
        os.remove(csv_file)
        st.success("All records cleared successfully!")
    else:
        st.warning("CSV file does not exist!")
