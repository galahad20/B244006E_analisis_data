# B244006E_Analisis data Bike sharing

## Description
In the final project on Data Analysis in Dicoding, I analyzed the **bike-sharing** dataset. This analysis contains the process of Gathering data, Data wrangling, Exploratory Data Analysis, Visualization, and Conclusion. 
I also created a dashboard to display a graph that shows the trend of bike rentals on the **bike-sharing** dataset. [Dashboard](https://dashboardpy-b244006ebian.streamlit.app/). The complete analysis is contained in the file **B244006E_Submission_Analysis_Data.ipynb**

## Instruction

### Using `B244006E_Submission_Analysis_Data.ipynb`
1. Download this repository
2. Open it on Google Colab.
3. Create a New Notebook.
4. Upload and select the previously downloaded file with .ipynb extension.
5. Run Import Library 
6. At The first code section in data wrangling which is connecting to Google Drive. This code will make gdrive folder that contains Mydrive inside it and load csv file from it (With this code you dont have to upload csv file everytime you want to do analysis. It will automatically load .csv file from Google Drive)
   Connecting to Google Drive
 '''
 from google.colab import drive
 drive.mount('/content/gdrive')
 '''  
8. To Upload day.csv and hour.csv, find upload section at Below "Daftar Isi" find this icon ![alt text](https://github.com/galahad20/B244006E_analisis_data/blob/main/picture/file_logo.png)?raw=true). Go to gdrive folder, you will find MyDrive folder and upload those 2 .csv files to MyDrive.

   
    Load csv file
   '''
   df_hari = pd.read_csv("/content/gdrive/MyDrive/day.csv", delimiter=",")
   df_jam = pd.read_csv("/content/gdrive/MyDrive/hour.csv", delimiter=",")
   df_hari.head()
   '''
10. Run the rest of code in file.

### `dashboard/dashboard.py`
1. Download this project.
2. Install the Streamlit in your terminal or command prompt using `pip install streamlit`. Install another libraries like pandas, numpy, scipy, matplotlib, and seaborn if you haven't.
3. Please note, don't move the csv file because it acts a data source. keep it in one folder as dashboard.py
4. Open your VSCode and run the file by clicking the terminal and write it `streamlit run dashboard.py`.

