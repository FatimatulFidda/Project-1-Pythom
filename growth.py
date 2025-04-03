import streamlit as st
import pandas as pd
import os
from io import Bytesto

st.set_page_config(page title== "Data Sweeper" , layout='wide')

#custom css
st.markdown(
    """"
    <style>
    .stApp{
        background-color: black;
        color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
)

#title and description
st.title("Datasweeper Sterling Integration By Fatima-Tul-Fidda")
st.write("Transform your files between CSV and Excel Formats with built-in data cleaning and visualization Creating te Project for Quater 3!")

#file uploader
uploaded_files = st.file_uploader("Upload your files(accepts CSV or Excel):", type=["cvs", "xlsx"], accept_multiple_files=(True))

if uploaded_files:
    for files in uploaded_files:
        files_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == "xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"unsupportedfile type: {file_ext}")
            continue

        #file details
        st.write(" preview the head of the Dataframe")
        st.dataframe(df.head())

        #Data Cleaning Options
        st.subheader(" Data Cleaning Option")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from the file : {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates removed!")

            with col2:
                if st.button(f"Fill missing value for {file.name}"):
                    numeric_cols = df.select_dtypes(includes=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled!")
                    
        st.subheader("Select Columns to keep")
        columns = st.multiselect(f"Choose columns for {file}", df.columns, default=df.columns)
        df = df[columns]

        #data visualization 

        st.subheader("Data Visualization")
        if st.checkbox(f"Show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(includes='number').iloc[:, :2])

        #Conversion Options

        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["csv" , "Excel"], Key=file.name)
        if st.button(f"Convert{file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to.csv(buffer, index=False) 
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                df.to.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)                     
            
            st.download_butten(
                label=f"Download {file.name} as {conversion_type}" ,
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("All files processed successfully!")
















                