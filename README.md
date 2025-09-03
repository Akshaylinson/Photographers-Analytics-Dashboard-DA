 📊 Photographers Analytics Dashboard

A professional analytics dashboard built with **Python, Flask, Pandas, and Plotly.js**, designed to analyze photographer records from an Excel dataset.  
It provides interactive charts, KPIs, and even simple predictive insights.

---

## 🚀 Features

- **KPI Summary Cards**  
  Total records, unique cities, states, owners, phones present/missing, duplicates.

- **Interactive Charts**
  - Top States by Photographer Count (bar chart)
  - Top Cities by Photographer Count (horizontal bar chart)
  - Phone Data Completeness (donut chart)
  - Duplicates vs Unique (donut chart)
  - Trend Line (Top States)
  - Phones Present Rate by State
  - Treemap of State Distribution
  - Heatmap (State × City)

- **Search & Filters**  
  Search by name, city, state, or phone. Adjust page size.

- **Data Table Explorer**  
  Paginated table with server-side filtering.

- **Basic Predictions**  
  Simulated future counts for top states.

---

## 📂 Project Structure

photographers_analytics/
│── app.py # Flask backend
│── Photographers 18957.xlsx # Input dataset
│── templates/
│ └── index.html # Main dashboard (UI + charts)
│── static/
│ └── (optional JS/CSS if needed)
│── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the project
```bash
git clone <your-repo-url> photographers_analytics
cd photographers_analytics
2. Create a virtual environment
bash
Copy code
python -m venv .venv
Activate it:

Windows (PowerShell):

powershell
Copy code
.\.venv\Scripts\activate
Linux / macOS (bash/zsh):

bash
Copy code
source .venv/bin/activate
3. Install dependencies (separately as required)
bash
Copy code
pip install Flask==3.0.3
pip install pandas==2.2.2
pip install openpyxl==3.1.5
4. Place dataset
Ensure the Excel file is present in the same folder as app.py:

nginx
Copy code
Photographers 18957.xlsx
5. Run the Flask app
bash
Copy code
python app.py
Flask will start at:

cpp
Copy code
http://127.0.0.1:5000/
📊 Example Dashboard View
KPI Summary Cards

Multiple interactive Plotly.js charts

Searchable, paginated data table

Predictive analytics

🔮 Future Improvements
Add time-series forecasting (ARIMA, Prophet, or sklearn regression).

Enable CSV/Excel upload via UI.

Export filtered data as CSV or PDF.

Add authentication for multiple users.

🛠 Tech Stack
Backend: Flask (Python)

Data Processing: Pandas, OpenPyXL

Frontend: HTML, TailwindCSS, Plotly.js

Dataset: Excel file of photographers

