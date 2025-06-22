
# 🤖 Post Generator for LinkedIn

![App Screenshot](https://github.com/anurag192/post-generator-linkedin/blob/main/image.png)

## 📝 Project Overview

**Mohan** is a LinkedIn influencer who wants to streamline the process of writing high-quality posts that align with his past content style. This tool helps Mohan by analyzing his past LinkedIn posts and generating new ones using AI — tailored to specific topics, language preferences, and desired length.

### ✨ Key Features

- 🔍 Extracts key topics from past LinkedIn posts
- 🧠 Uses few-shot learning to maintain personal writing style
- 🗣️ Supports multiple languages (English, Hinglish, etc.)
- 📏 Post length customization: Short, Medium, or Long
- 🧠 Powered by Groq LLM and Streamlit interface

---

## 🚀 How It Works

### ✅ Stage 1: Analyze Past Posts
- User uploads previous LinkedIn posts
- Tool automatically extracts:
  - Topic
  - Language
  - Length

### ✅ Stage 2: Generate New Post
- User selects:
  - Topic
  - Language
  - Desired Length
- The tool uses few-shot learning based on similar past posts to generate a new post in the same style.

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/anurag192/post-generator-linkedin.git
cd post-generator-linkedin
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up the API Key

- Go to [Groq Console](https://console.groq.com/keys) and generate an API key.
- Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

### 4. Run the App

```bash
streamlit run main.py
```

---

## 📦 Project Structure

```
📁 post-generator-linkedin
 ┣ 📄 main.py               # Streamlit frontend
 ┣ 📄 post_gen.py           # Post generation logic
 ┣ 📄 few_shot.py           # Few-shot learning helper
 ┣ 📄 requirements.txt      # Dependencies
 ┣ 📄 .env                  # API key config (not committed)
 ┣ 📄 image.png             # App screenshot
 ┗ 📁 data/
     ┗ 📄 processed_posts.json   # Sample past post data
```



