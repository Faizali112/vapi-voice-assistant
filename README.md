<h1 align="center"> Voice AI Agent</h1>
<p align="center">
  <i>“Your own smart assistant that listens, talks back, and even schedules meetings!”</i>
</p>

---

### 🌟 Overview

This is an AI-powered voice assistant built using:
- 🗣️ [VAPI.ai](https://vapi.ai) for real-time voice interaction
- 🤖 OpenAI for smart conversation
- 🧠 Flask & Node.js as backend
- 📅 Google Calendar API to schedule meetings
- 🔗 Ngrok to connect your local server to the internet

---

## 📁 Project Structure

```bash
voice-ai-agent/
├── app.py                    # Flask backend
├── index.js                  # Node.js webhook (VAPI handler)
├── package.json              # Node dependencies
├── requirements.txt          # Python dependencies
├── .env                      # API keys (DO NOT UPLOAD)
├── credentials.json          # Google Calendar OAuth (DO NOT UPLOAD)
├── token.json                # Generated after OAuth (DO NOT UPLOAD)
└── README.md                 # You're reading it!
```

---

## 🚀 Getting Started (Run Locally in 10 Minutes)

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/voice-ai-agent.git
cd voice-ai-agent
```

---

### 2. 📥 Install Dependencies

#### 👉 For Python (Flask backend)

```bash
pip install -r requirements.txt
```

#### 👉 For Node.js (Webhook backend)

```bash
npm install
```

---

### 3. 🔐 Add API Keys & Credentials

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

Then place these in the root folder:
- `credentials.json` → Download from Google Cloud Console
- `token.json` → Will be auto-generated on first OAuth login

> ✅ Make sure `.env`, `credentials.json`, and `token.json` are all listed in `.gitignore`.

---

### 4. 🌐 Start the Flask Server

```bash
python app.py
```

By default, it runs on: `http://127.0.0.1:3000`

---

### 5. 🛜 Expose Your Server with Ngrok

```bash
ngrok http 3000
```

Copy the `https://` forwarding link (e.g., `https://abcd1234.ngrok.io`).

---

### 6. 🧠 Set Up Your VAPI Workflow

1. Go to [VAPI.ai dashboard](https://app.vapi.ai)
2. Create a new **Voice Agent**
3. In the Workflow:
   - Add a **"Start" block**
   - Then add a **Webhook block**
   - Paste your Ngrok URL (e.g., `https://abcd1234.ngrok.io/webhook`)
4. (Optional) Add an OpenAI block if needed
5. Click **Publish**

---

### 7. 🗣️ Start Talking to Your Assistant

1. Click "Start Call" on VAPI
2. Say "Hello" and start the conversation
3. Ask it to **schedule a Google Meet**, and it will!

---

## 💡 Features

- 🔊 Real-time voice chat powered by VAPI
- 🧠 Natural conversations via OpenAI
- 📅 Schedules Google Meet links with your specified time
- 🔒 Secure API key handling with `.env` and `.gitignore`

---

## 👤 Make It Yours

If someone else wants to use this project:
- They must insert their own **OpenAI key** and **Google credentials**
- Everything is set up for plug-and-play 🚀

---

## 🛡️ Security Tips

- ✅ Never upload `.env`, `credentials.json`, or `token.json`
- ✅ Your `.gitignore` should include:
  ```bash
  .env
  credentials.json
  token.json
  node_modules/
  ```

---

## 💬 Questions?

Message me on GitHub or open an issue if you get stuck.  
Happy coding 💻🎧!
