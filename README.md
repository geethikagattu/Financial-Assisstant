📘 README.md
# 💰 Financial Assistant AI

Your personalized **AI-powered financial coach** built with **Flask + OpenAI**.  
It helps students and young professionals learn how to **budget, track spending, and set financial goals** in a simple and interactive way.

---

## ✨ Features
- 🧾 **Build a Budget** — Learn the 50/30/20 rule and create a spending plan.  
- 📊 **Track Spending** — Monitor expenses with simple methods.  
- 🎯 **Set Goals** — Define SMART (Specific, Measurable, Achievable, Relevant, Time-Bound) goals.  
- 🤖 **AI Chat Coach** — Ask financial questions and get advice powered by OpenAI GPT.  

---

## 🚀 Tech Stack
- **Backend:** Flask (Python)  
- **Frontend:** HTML, TailwindCSS  
- **AI:** OpenAI GPT (Chat Completions API)  
- **Deployment:** Render / Railway / Heroku  

---

## 📂 Project Structure


Financial-Assisstant/
│── app.py # Flask backend with AI chat API
│── index.html # Main homepage with chat interface
│── budget.html # Budgeting page
│── spending.html # Spending tracking page
│── goals.html # Goal setting page
│── requirements.txt # Python dependencies
│── Procfile # Deployment instructions (Render/Heroku)


---

## ⚙️ Setup & Installation

### 1. Clone the repo
git clone https://github.com/geethikagattu/Financial-Assisstant.git
cd Financial-Assisstant

###2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

###3. Install dependencies
pip install -r requirements.txt

###4. Add environment variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here

5. Run locally
python app.py


App will be available at: http://127.0.0.1:5000

##🌍 Deployment
Deploy on Render

Push repo to GitHub.

Connect GitHub repo in Render
.

Add environment variable:

OPENAI_API_KEY=your_api_key

##Deploy 🚀

Deploy on Heroku
heroku login
heroku create financial-assistant
git push heroku main

##📌 Roadmap
🔊 Voice input via OpenAI Whisper

📈 Personalized budget visualizations with charts

📱 Mobile-friendly PWA version

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

📜 License

MIT License © 2025 Geethika Gattu
