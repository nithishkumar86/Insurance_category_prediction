# 🛡️ Insurance Premium Category Prediction  

## 🔹 Overview  
The **Insurance Premium Category Prediction** system is a machine learning–powered **FastAPI application** that predicts the **premium category** of users based on personal and lifestyle attributes such as **age, BMI, occupation, income, and lifestyle risk**.  

It provides REST APIs for **prediction** and **system health checks**, making it suitable for **enterprise insurance platforms** or standalone usage.  
The project ensures **data validation, feature engineering, and robust error handling** with Dockerized deployment support.  

---

## 🔹 Features  
- 📂 **User Input Validation** → Age, height, weight, income, occupation, and smoking habits checked with Pydantic  
- ⚖️ **Automatic Feature Engineering** →  
  - BMI calculation  
  - Age-group classification (`youth`, `adult`, `middle_aged`, `senior`)  
  - Lifestyle risk assessment (`low`, `medium`, `high`)  
- 🤖 **Model Prediction API** → Returns predicted premium category  
- 🛡️ **Robust Error Handling** → Managed with FastAPI responses  
- 🚀 **Containerized Deployment** → Docker-ready  

---

## 🔹 Tech Stack  
- **FastAPI** → RESTful API framework  
- **Pydantic** → Data validation & schema definitions  
- **ML Model** → Custom-trained model (`model/predict.py`)  
- **Logging & Custom Exceptions**  
- **Docker** → Deployment  

---

## 🔹 API Endpoints  

### ✅ Home  
```http
GET /home
Response:

json
Copy code
{
  "message": "Insurance_premium_category"
}
✅ Model Check
http
Copy code
GET /check
Response:

json
Copy code
{
  "status": "ok",
  "version": "v1.0",
  "model": true
}
✅ Predict Premium Category
http
Copy code
POST /predict
Request Body:

json
Copy code
{
  "age": 32,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 8.5,
  "smoker": true,
  "occupation": "private_job"
}
Response:

json
Copy code
{
  "prediction": "Premium_Category_A"
}
🔹 Setup & Usage
1️⃣ Clone Repository
bash
Copy code
git clone https://github.com/your-username/insurance-category-prediction.git
cd insurance-category-prediction
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run Locally
bash
Copy code
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
4️⃣ Run with Docker
bash
Copy code
docker build -t insurance-prediction .
docker run -d -p 8000:8000 insurance-prediction
🔹 Example Flow
mermaid
Copy code
flowchart LR
    A[User Input] --> B[Pydantic Validation]
    B --> C[Feature Engineering]
    C --> D[ML Model Prediction]
    D --> E[API Response: Premium Category]
🚀 Roadmap
🔮 Improve model accuracy with additional features

📑 User-friendly report generation

☁️ CI/CD pipeline with Jenkins + AWS

📊 Streamlit dashboard for premium predictions

✨ With this system, insurance providers can automatically classify premium categories for users, improving efficiency and reducing manual effort