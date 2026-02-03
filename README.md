🕵️ Agentic Honey-Pot for Scam Detection & Intelligence Extraction
<p align="center"> <img src="https://img.shields.io/badge/AI-Agentic-blue" /> <img src="https://img.shields.io/badge/Hackathon-GUVI-orange" /> <img src="https://img.shields.io/badge/Domain-Cybersecurity-red" /> <img src="https://img.shields.io/badge/Status-Active-success" /> <img src="https://img.shields.io/badge/License-MIT-green" /> </p>

Open-source, AI-powered agentic honeypot that detects scam intent, autonomously engages scammers, extracts intelligence, and reports structured results — without exposing detection.

📌 Overview

Agentic Honey-Pot is a security-focused AI system designed to outsmart adaptive scammers.
Unlike rule-based filters, it uses agentic reasoning and multi-turn conversational intelligence to extract actionable scam data.

Use cases

Scam research & intelligence

Fraud prevention systems

Security analytics platforms

Hackathons & AI agent demos

📑 Table of Contents

Problem Statement

Objectives

Architecture

Tech Stack

Getting Started

API Reference

Agent Behavior

Evaluation & Callback

Roadmap

Contributing

License

🚀 Problem Statement

Online scams (bank fraud, UPI fraud, phishing, fake offers) evolve rapidly and adapt to user responses.

Traditional detection systems fail against:

Multi-turn manipulation

Social engineering

Adaptive scam strategies

This project builds an Agentic Honey-Pot to detect, engage, and extract intelligence from scammers in real time.

🎯 Objectives

Detect scam or fraudulent intent

Activate an autonomous AI agent

Maintain a believable human-like persona

Handle multi-turn conversations

Extract scam intelligence

Expose a public REST API

Secure access using API keys

Report final intelligence to GUVI evaluation endpoint

🧠 High-Level Architecture
Incoming Message
       ↓
Scam Intent Detection
       ↓
Agent Activation (LLM Persona)
       ↓
Multi-Turn Engagement
       ↓
Intelligence Extraction
       ↓
Structured API Response
       ↓
Final Callback to GUVI

🧰 Tech Stack

Backend: FastAPI / Flask

AI Layer: LLM-based Agentic Orchestration

NLP: Scam intent classification

Security: API-key authentication

Deployment: Docker / Cloud-ready

Integration: REST + Callback API

🚀 Getting Started
Prerequisites

Python 3.9+

Git

API key (environment variable)

Installation
git clone https://github.com/ksinghs/agentic-honeypot.git
cd agentic-honeypot
pip install -r requirements.txt

Run Locally
uvicorn app.main:app --reload

📡 Public REST API
Endpoint
POST /api/honeypot/message

Authentication Headers
x-api-key: YOUR_SECRET_API_KEY
Content-Type: application/json

🤖 Agent Behavior Expectations

The AI agent:

Handles multi-turn conversations

Adapts responses dynamically

Never reveals scam detection

Behaves like a real human

Self-corrects when needed

Maximizes intelligence extraction

🧪 Extracted Intelligence

🏦 Bank account numbers

💳 UPI IDs

🔗 Phishing links

📞 Phone numbers

⚠️ Suspicious keywords

🧠 Behavioral scam patterns

🔁 Mandatory Final Result Callback (CRITICAL)

After engagement completion, the system must send results to:

POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult


If this callback is not sent, the solution will not be evaluated.

(Callback payload remains exactly as provided in the problem statement.)

🗺️ Roadmap

 Scam intent detection

 Multi-turn agent engagement

 Intelligence extraction

 Intelligence analytics dashboard

 Multi-language support

 Scam network correlation

 Threat actor profiling

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a feature branch

Commit your changes

Open a Pull Request

Please follow ethical AI and security guidelines.

📜 License

This project is licensed under the MIT License.

👤 Author

Kundan Singh
AI • Data • Security • Agentic Systems

