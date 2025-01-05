# B244006E_Bike sharing Data Analysis

## Description
In the final project on Data Analysis in Dicoding, I analyzed the **bike-sharing** dataset. This analysis contains the process of Gathering data, Data wrangling, Exploratory Data Analysis, Visualization, and Conclusion. 
I also created a streamlit dashboard to display a graph that shows the trend of bike rentals on the **bike-sharing** dataset -> [ Streamlit Dashboard](https://dashboardpy-b244006ebian.streamlit.app/). 
The complete analysis is contained in the file **B244006E_Submission_Analysis_Data.ipynb**

## Instruction

### Using `B244006E_Submission_Analysis_Data.ipynb`
1. Clone this repository
2. Open it on Google Colab.
3. Create a New Notebook.
4. Upload and select the previously downloaded file with .ipynb extension.
5. Run Import Library 
6. Connecting to Google Drive
   
    ```
    from google.colab import drive
    drive.mount('/content/gdrive')
    ```
    > At The first code section in data wrangling which is connecting to Google Drive. This code will make gdrive folder that contains Mydrive inside it and load csv file from it (With this code you dont have to upload csv file everytime you want to do analysis. It will automatically load .csv file from Google Drive)
   
7. Upload and Load csv file
   ```
   df_hari = pd.read_csv("/content/gdrive/MyDrive/day.csv", delimiter=",")
   df_jam = pd.read_csv("/content/gdrive/MyDrive/hour.csv", delimiter=",")
   df_hari.head()
   ```
   > To Upload **day.csv** and **hour.csv**, find upload section at Below "Daftar Isi" find this icon ![alt text](https://github.com/galahad20/B244006E_analisis_data/blob/main/picture/file_logo.png?raw=true).

  
   >
   ![alt text](https://github.com/galahad20/B244006E_analisis_data/blob/main/picture/drive_pict.png?raw=true).

   > Go to **gdrive** folder, you will find **MyDrive** folder and upload those 2 .csv files to MyDrive.

10. Run the rest of code in file.

### `dashboard/dashboard.py`
1. Clone this repository

2. Install all library from requirements.txt

   ```
   pip install -r requirements.txt
   ```

3. Go to dashboard folder

   ```
   cd dashboard
   ```

4. Run Streamlit dashboard

   ```
   streamlit run dashboard.py
   ```
