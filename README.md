# JobMate

_Your personal WhatsApp job search assistant powered by GPT and real-time scraping._

---

## 🚀 Overview
**JobMate** is a conversational WhatsApp bot that helps users search for jobs in real time using keywords like:

```
frontend developer in Berlin
```

It scrapes job listings from sources like **Indeed**, uses **ChatGPT** to intelligently parse user input, and allows job saving. This bot is built with:

- **Python + Flask** for backend interaction
- **Twilio** for WhatsApp messaging
- **OpenAI (ChatGPT)** for natural language understanding
- **Google Jobs/LinkedIn scraping** (custom modules)

---

## 💡 Features

- 🔍 **Job Search** via WhatsApp
- 💬 **Natural Language Understanding** (via GPT)
- 💾 **Save Jobs** and Backups
- 🌍 Supports locations (e.g., "in Berlin")
- 🧠 Auto classifies job titles via ChatGPT

---

## 📦 Project Structure

```
JobMate/
├── app.py                   # Main Flask app & Twilio integration
├── incoming_msg.py          # Core WhatsApp message handler
├── api_files/
│   ├── ChatGPT.py           # GPT prompt formatting and API call
│   ├── LinkedIn.py          # LinkedIn job search module (optional)
│   └── Google_job.py        # Google/Indeed job scraper
├── save_jobs.py             # Module to save/retrieve job results
├── .env                     # Secrets (Twilio, GPT keys)
```

---

## ⚙️ Installation

1. **Clone the repo**:
```bash
git clone https://github.com/yourname/jobmate.git
cd jobmate
```

2. **Create and activate virtual environment**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up `.env`** with your credentials:
```env
MS_TWILIO_ACCOUNT_SID=...
MS_TWILIO_API_KEY_SID=...
MS_TWILIO_SECRET=...
MS_TWILIO_DEFAULT_SERVICE_SID=...
MS_NUMBER=whatsapp:+14155238886
PHONE_NUMBER=whatsapp:+491234567890
OPENAI_KEY=sk-...
```

---

## 🧪 Running the App

```bash
python app.py
```

You’ll see a WhatsApp message sent to your phone. Then you can chat via WhatsApp to:

- Search jobs (`python dev in Paris`)
- Save jobs (`save`)
- Say goodbye (`bye`, `thanks`)

---

## ✉️ Example Commands

```
"Product Manager in Amsterdam"
"Data scientist in Munich"
"Save"
"Show saved jobs"
"Help"
```

---

## 📄 Example Output
```
🔎 Searching for: Frontend Developer in Berlin
✅ Found 12 new jobs:

1. Frontend Engineer @ TechStars
2. React Developer @ AwesomeSoft
...
```

---

## 📌 Notes

- `save_jobs.py` saves to `user_saved_jobs.txt` and backs up on `save` command.
- Jobs are not persisted beyond memory (add DB for persistence).
- LinkedIn scraping can be disabled or mocked (Google Jobs preferred).

---

## 📬 Future Ideas

- ✅ `show saved jobs` command
- 🔄 Pagination support
- 💾 SQLite/PostgreSQL support
- 📈 Job stats / filtering
- 🖼️ Frontend dashboard

---

## 🧑‍💻 Author
**Marco** – _"Job search made conversational."_

---

## 📃 License
MIT License

---

