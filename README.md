# Bike Rentals - Proyek Analisis Data 
Ini adalah tugas akhir dari Dicoding pada mata kuliah “Belajar Analisis Data Dengan Python” untuk membuat analisa dan membuat dashboard dari dataset bike sharing. Pada file buku catatan saya lampirkan cara saya melakukan analisis dari Data Wrangling, Exploratory Data Analysis, dan Data Visualization. Selain itu saya juga membuat dashboardnya menggunakan streamlit, dan anda bisa mengeceknya dengan mengklik link di sidebar kanan atau [di sini](https://dashboardpy-i5ffhdxqgn4zfthtrqpghc.streamlit.app/).
## File Structures
```
.
├── Dashboard
│   ├── img
|   |   └──Logo.png
│   ├── dashboard.py
│   └── day.csv
├── Data
│   ├── Bike-sharing-dataset.zip
│   ├── day.csv
|   └── hour.csv
├── README.md
├── notebook.ipynb
└── requirements.txt
└── url.txt
```
## Setup environment
1. Install Python di [Situs Resmi](https://www.python.org/downloads/) atau [Microsoft Store](https://apps.microsoft.com/detail/9NRWMJP3717K?hl=en-US&gl=US)
2. Install Text Editor [Vscode](https://code.visualstudio.com/download) atau [Microsoft Store](https://apps.microsoft.com/detail/XP9KHM4BK9FZ7Q?hl=en-us&gl=US)
3. Ektensi di Vscode yang di perlukan 
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
4. Install library di dalam terminal atau install di sell kode jupyter notebook :
```python
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install streamlit
pip install DateTime
pip install zip-files
```
## Jalankan aplikasi streamlit
```Python
python -m streamlit run c:/Users/DELL/Desktop/Submission/Dashboard/dashboard.py
```