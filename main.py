import streamlit as st
import pandas as pd
import sqlite3
import os

st.title("Monthly Records Of Lakhanpur Health Post")


# caste_dict={'01':'Dalit','02':'Janjati','03':'Madheshi','04':'Muslim','05':'Brahman','06':'Other'}

st.header("Cards are:")

# --- Summary Cards for Total Male, Female, and TV Patients ---
if os.path.exists("manshir_records.csv"):
    df_summary1 = pd.read_csv("manshir_records.csv")
    choose_num=st.selectbox("choose type:",['All','Old','New',])
    if choose_num=='All':
        
         col0,col1, col2= st.columns(3)

         total_count=len(df_summary1)
         total_male = df_summary1[df_summary1['Gender'] == 'Male'].shape[0]
         total_female = df_summary1[df_summary1['Gender'] == 'Female'].shape[0]
         

         with col0:
            st.metric(label="Today Total Records  :", value=total_count)

         with col1:
            st.metric(label="Total Male Patients", value=total_male)

         with col2:
            st.metric(label="Total Female Patients", value=total_female)
        
    elif choose_num=='Old':
        st.header("Old Records:")
        col11,col12,col13=st.columns(3)

        total_old=len(df_summary1[df_summary1["OPD Type"]=="Old"])

        total_old_male = df_summary1[(df_summary1["OPD Type"] == "Old") & (df_summary1["Gender"] == "Male")].shape[0]

        total_old_female = df_summary1[(df_summary1["OPD Type"] == "Old") & (df_summary1["Gender"] == "Female")].shape[0]

        with col11:
            st.metric(label="Total:",value=total_old)
        with col12:
            st.metric(label="Total Male:",value=total_old_male)
        with col13:
            st.metric(label="Total Female:",value=total_old_female)
        
    else:
            st.header("New Records:")
            col21,col22,col23=st.columns(3)

            total_old=len(df_summary1[df_summary1["OPD Type"]!="Old"])

            total_old_male = df_summary1[(df_summary1["OPD Type"] != "Old") & (df_summary1["Gender"] == "Male")].shape[0]

            total_old_female = df_summary1[(df_summary1["OPD Type"] != "Old") & (df_summary1["Gender"] == "Female")].shape[0]

            with col21:
                st.metric(label="Total:",value=total_old)
            with col22:
                st.metric(label="Total Male:",value=total_old_male)
            with col23:
                st.metric(label="Total Female:",value=total_old_female)




    choose_num1=st.selectbox("choose type:",['All','Male','Female',])

    df_summary = pd.read_csv("manshir_records.csv")

    total_Dalit=df_summary[df_summary['Cast Code']=='Dalit'].shape[0]
    total_Janjati=df_summary[df_summary['Cast Code']=='Janjati'].shape[0]
    total_Madheshi=df_summary[df_summary['Cast Code']=='Madheshi'].shape[0]
    total_Muslim=df_summary[df_summary['Cast Code']=='Muslim'].shape[0]
    total_Brahman=df_summary[df_summary['Cast Code']=='Brahman'].shape[0]
    total_Other=df_summary[df_summary['Cast Code']=='Other'].shape[0]

    

    

    if choose_num1=='All':
        st.subheader("Total  ( 1.Dalit 2.Janjati 3.Madheshi 4.Muslim 5.Brahman 6.Other)")

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
    
    elif choose_num1=='Male':
        st.subheader("Male ( 1.Dalit 2.Janjati 3.Madheshi 4.Muslim 5.Brahman 6.Other)")
        total_male_dalit = df_summary1[(df_summary1["Cast Code"] == "Dalit") & (df_summary1["Gender"] == "Male")].shape[0]

        total_male_janjati = df_summary1[(df_summary1["Cast Code"] == "Janjati") & (df_summary1["Gender"] == "Male")].shape[0]

        total_male_madheshi = df_summary1[(df_summary1["Cast Code"] == "Madheshi") & (df_summary1["Gender"] == "Male")].shape[0]

        total_male_muslim = df_summary1[(df_summary1["Cast Code"] == "Muslim") & (df_summary1["Gender"] == "Male")].shape[0]

        total_male_brahman = df_summary1[(df_summary1["Cast Code"] == "Brahman") & (df_summary1["Gender"] == "Male")].shape[0]

        total_male_other = df_summary1[(df_summary1["Cast Code"] == "Other") & (df_summary1["Gender"] == "Male")].shape[0]

        col3, col4,col5,col6,col7,col8= st.columns(6)
    
        with col3:
         st.metric(label="1.Total Dalit", value=total_male_dalit)

        with col4:
             st.metric(label="2.Total Janjati", value=total_male_janjati)

        with col5:
         st.metric(label="3.Total Madheshi", value=total_male_madheshi)

        with col6:
            st.metric(label="4.Total Muslim", value=total_male_muslim)

        with col7:
            st.metric(label="5.Total Brahman", value=total_male_brahman)

        with col8:
         st.metric(label="6.Other", value=total_male_other)

    

    
    elif choose_num1=='Female':
        st.subheader("Female ( 1.Dalit 2.Janjati 3.Madheshi 4.Muslim 5.Brahman 6.Other)")
        total_female_dalit = df_summary1[(df_summary1["Cast Code"] == "Dalit") & (df_summary1["Gender"] == "Female")].shape[0]

        total_female_janjati = df_summary1[(df_summary1["Cast Code"] == "Janjati") & (df_summary1["Gender"] == "Female")].shape[0]

        total_female_madheshi = df_summary1[(df_summary1["Cast Code"] == "Madheshi") & (df_summary1["Gender"] == "Female")].shape[0]

        total_female_muslim = df_summary1[(df_summary1["Cast Code"] == "Muslim") & (df_summary1["Gender"] == "Female")].shape[0]

        total_female_brahman = df_summary1[(df_summary1["Cast Code"] == "Brahman") & (df_summary1["Gender"] == "Female")].shape[0]

        total_female_other = df_summary1[(df_summary1["Cast Code"] == "Other") & (df_summary1["Gender"] == "Female")].shape[0]

        col3, col4,col5,col6,col7,col8= st.columns(6)
    
        with col3:
         st.metric(label="1.Total Dalit", value=total_female_dalit)

        with col4:
             st.metric(label="2.Total Janjati", value=total_female_janjati)

        with col5:
         st.metric(label="3.Total Madheshi", value=total_female_madheshi)

        with col6:
            st.metric(label="4.Total Muslim", value=total_female_muslim)

        with col7:
            st.metric(label="5.Total Brahman", value=total_female_brahman)

        with col8:
         st.metric(label="6.Other", value=total_female_other)
         
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




st.subheader("Delete Specific Record")

delete_by = st.radio(
    "Delete record using:",
    ["Patient Name"]
)

delete_value = st.text_input(f"Enter {delete_by}")

if st.button("Delete Record"):
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)

        if delete_by == "Patient Name":
            df_new = df[df["Patient Name"] != delete_value]

        if len(df) == len(df_new):
            st.warning("No matching record found!")
        else:
            df_new.to_csv(csv_file, index=False)
            st.success("Record deleted successfully!")
    else:
        st.error("CSV file not found!")


st.subheader("Update Record (Using Patient Name)")

update_name = st.text_input("Enter Patient Name to Update")

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)

    if update_name in df["Patient Name"].values:
        st.success("Record found! Update details below 👇")

        row = df[df["Patient Name"] == update_name].iloc[0]

        new_age = st.number_input(
            "Age", 0, 120, int(row["Age"])
        )

        new_gender = st.selectbox(
            "Gender",
            ["Female", "Male", "Other"],
            index=["Female", "Male", "Other"].index(row["Gender"])
        )

        new_cast = st.selectbox(
            "Cast Code",
            ["Dalit", "Janjati", "Madheshi", "Muslim", "Brahman", "Other"],
            index=["Dalit","Janjati","Madheshi","Muslim","Brahman","Other"].index(row["Cast Code"])
        )

        new_tv = st.radio("Expect TV Patients",["No", "Yes"],key="update_expect_tv")

        if st.button("Update Record"):
            df.loc[df["Patient Name"] == update_name, [
                "Age", "Gender", "Cast Code", "Expect TV"
            ]] = [new_age, new_gender, new_cast, new_tv]

            df.to_csv(csv_file, index=False)
            st.success("✅ Record updated successfully!")

    else:
        st.warning("❌ Patient name not found!")
else:
    st.error("CSV file not found!")


st.subheader("Clear All Records")

if st.button("Clear Records"):
    if os.path.exists(csv_file):
        os.remove(csv_file)
        st.success("All records cleared successfully!")
    else:
        st.warning("CSV file does not exist!")
