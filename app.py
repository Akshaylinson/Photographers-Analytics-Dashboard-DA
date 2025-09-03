
import os
import pandas as pd
from flask import Flask, render_template, jsonify, request
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime, timedelta
import random

APP_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(APP_DIR, "Photographers 18957.xlsx")

app = Flask(__name__)

# Load dataset
df = pd.read_excel(EXCEL_FILE)
df = df.rename(columns=lambda c: c.strip())

# Try to detect key columns
col_city = next((c for c in df.columns if "city" in c.lower()), None)
col_state = next((c for c in df.columns if "state" in c.lower()), None)
col_name = next((c for c in df.columns if "name" in c.lower()), df.columns[0])
col_phone = next((c for c in df.columns if "phone" in c.lower() or "mobile" in c.lower()), None)
col_email = next((c for c in df.columns if "email" in c.lower()), None)
col_website = next((c for c in df.columns if "website" in c.lower() or "url" in c.lower()), None)
col_zip = next((c for c in df.columns if "zip" in c.lower() or "postal" in c.lower()), None)

# Generate mock data for demonstration
def generate_mock_data():
    # Mock revenue data by month
    months = []
    revenue = []
    current_date = datetime.now()
    for i in range(12):
        month_date = current_date - timedelta(days=30*i)
        months.append(month_date.strftime("%b %Y"))
        revenue.append(random.randint(8000, 20000))
    
    # Mock equipment distribution
    equipment = [
        {"category": "Canon", "value": random.randint(30, 45)},
        {"category": "Nikon", "value": random.randint(25, 40)},
        {"category": "Sony", "value": random.randint(15, 30)},
        {"category": "Fujifilm", "value": random.randint(5, 15)},
        {"category": "Other", "value": random.randint(5, 10)}
    ]
    
    # Mock photography types
    photography_types = [
        {"type": "Portrait", "count": random.randint(100, 200)},
        {"type": "Wedding", "count": random.randint(80, 150)},
        {"type": "Landscape", "count": random.randint(70, 130)},
        {"type": "Commercial", "count": random.randint(60, 120)},
        {"type": "Event", "count": random.randint(90, 160)}
    ]
    
    # Mock customer satisfaction
    satisfaction = [
        {"month": "Jan", "score": random.randint(80, 95)},
        {"month": "Feb", "score": random.randint(82, 94)},
        {"month": "Mar", "score": random.randint(85, 96)},
        {"month": "Apr", "score": random.randint(83, 97)},
        {"month": "May", "score": random.randint(87, 98)},
        {"month": "Jun", "score": random.randint(88, 97)},
        {"month": "Jul", "score": random.randint(86, 96)},
        {"month": "Aug", "score": random.randint(84, 95)},
        {"month": "Sep", "score": random.randint(85, 96)},
        {"month": "Oct", "score": random.randint(87, 97)},
        {"month": "Nov", "score": random.randint(89, 98)},
        {"month": "Dec", "score": random.randint(90, 99)}
    ]
    
    return {
        "revenue_trend": {"months": months, "revenue": revenue},
        "equipment_distribution": equipment,
        "photography_types": photography_types,
        "satisfaction_trend": satisfaction
    }

mock_data = generate_mock_data()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/summary")
def summary():
    return jsonify({
        "total_records": int(len(df)),
        "unique_cities": int(df[col_city].nunique() if col_city else 0),
        "unique_states": int(df[col_state].nunique() if col_state else 0),
        "unique_names": int(df[col_name].nunique()),
        "phones_present": int(df[col_phone].notna().sum()) if col_phone else 0,
        "phones_missing": int(df[col_phone].isna().sum()) if col_phone else 0,
        "emails_present": int(df[col_email].notna().sum()) if col_email else 0,
        "websites_present": int(df[col_website].notna().sum()) if col_website else 0
    })

@app.route("/api/top-cities")
def top_cities():
    g = df.groupby(col_city).size().reset_index(name="count").sort_values("count", ascending=False).head(15)
    return jsonify(g.to_dict(orient="records"))

@app.route("/api/top-states")
def top_states():
    g = df.groupby(col_state).size().reset_index(name="count").sort_values("count", ascending=False).head(15)
    return jsonify(g.to_dict(orient="records"))

@app.route("/api/predictions")
def predictions():
    """Simulate trend prediction (linear regression on city counts)."""
    g = df.groupby(col_city).size().reset_index(name="count").sort_values("count", ascending=False).head(10)
    X = np.arange(len(g)).reshape(-1, 1)
    y = g["count"].values
    model = LinearRegression().fit(X, y)
    future_x = np.arange(len(g), len(g)+5).reshape(-1, 1)
    future_y = model.predict(future_x)
    preds = [{"future_index": int(i), "predicted": float(v)} for i, v in zip(range(len(g), len(g)+5), future_y)]
    return jsonify({"history": g.to_dict(orient="records"), "predictions": preds})

@app.route("/api/mock/revenue")
def mock_revenue():
    return jsonify(mock_data["revenue_trend"])

@app.route("/api/mock/equipment")
def mock_equipment():
    return jsonify(mock_data["equipment_distribution"])

@app.route("/api/mock/photography-types")
def mock_photography_types():
    return jsonify(mock_data["photography_types"])

@app.route("/api/mock/satisfaction")
def mock_satisfaction():
    return jsonify(mock_data["satisfaction_trend"])

@app.route("/api/geographic-distribution")
def geographic_distribution():
    if col_state:
        state_counts = df[col_state].value_counts().reset_index()
        state_counts.columns = ['state', 'count']
        return jsonify(state_counts.to_dict(orient='records'))
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
