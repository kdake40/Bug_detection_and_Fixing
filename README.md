# 🐍 Bug_Detection_and_Bug_fixing

Build a machine leaming model that can automatically identify bugs (or potential errors) in a given piece of code and 7 suggest fixes. This project requires designing, training and evaluating an ML model that can parse source code. classify bug types and generate fix Build a machine

# 🔍 AI-Powered Bug Detector & Fixer

This project is an AI-powered tool that detects and fixes bugs in Python code. It consists of a **FastAPI** backend (powered by CodeLlama) and a **Streamlit** frontend for easy interaction.

## 📌 Features
- Detects errors in Python code
- Highlights the exact line of error
- Suggests a fixed version of the code
- Provides step-by-step explanations of the fixes
- Simple UI built with Streamlit

---

## 🚀 Getting Started
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kdake40/bug-detector.git
cd bug-detector
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed.
```bash
pip install -r requirements.txt
```

### 3️⃣ Download & Prepare the Model
Before running the app, ensure the **CodeLlama** model is downloaded and stored locally.
```bash
# Run this only once to save the model locally
python app.py
```
This will save the model in `./saved_codellema`.

---

## 🖥️ Running the Application
### Start the Backend (FastAPI)
```bash
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
```

### Start the Frontend (Streamlit)
Open a new terminal and run:
```bash
streamlit run frontend.py
```
Now, open your browser and go to `http://localhost:8501/` to use the UI.

---

## 🛠 API Endpoints
| Method | Endpoint      | Description |
|--------|-------------|-------------|
| POST   | `/analyze`  | Detects bugs in the given Python code |
| POST   | `/fix`      | Fixes detected bugs and provides corrected code |

### Example API Call
```python
import requests

code_snippet = """
def divide(a, b):
    return a / b  # Possible division by zero

print(divide(10, 0))
"""

response = requests.post("http://localhost:8000/analyze", json={"code_snippet": code_snippet})
print(response.json())
```

---

## 📷 Screenshots
### 🔍 **Bug Detection**
![bug detection](https://github.com/user-attachments/assets/fa484bfe-cece-4ec5-8746-98bbfa15b55d)



### ✅ **Fixed**
![WhatsApp Image 2025-04-02 at 15 16 23_ca09297d](https://github.com/user-attachments/assets/20bdcc98-267e-4c14-9f86-0afc80041a26)

![bug fixing](https://github.com/user-attachments/assets/d697b690-288c-4f44-903a-3db126f54985)



---

## 🤝 Contributing
Pull requests are welcome! If you find issues or have suggestions, please open an issue.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact
For any queries, contact [kdake40@gmail.com](mailto:your_kdake40@gmail.com).

