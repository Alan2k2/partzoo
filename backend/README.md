# ⚙️ Backend: Automobile Parts API

This repository contains the backend core for the **Automobile Parts Network Platform**. It is a RESTful API built with Python and MySQL, designed to handle complex B2B/B2C logic, dynamic pricing tiers, inventory management, and third-party API integrations (Payments & 3PL Logistics).

---

## 🛠️ Tech Stack

*   **Language:** Python 3.9+
*   **Database:** MySQL
*   **Environment Management:** `python-dotenv`
*   **Authentication:** JWT (JSON Web Tokens) - *Planned*
*   **Framework:** *(Insert your chosen framework, e.g., FastAPI, Flask, or Django)*

---

## ✨ Core Backend Features

*   **Dual-Tiered Pricing Engine:** Serves distinct data to the frontend based on user authentication (Standard Retail vs. Wholesale B2B).
*   **Secure Authentication:** Role-based access control (RBAC) ensuring everyday consumers cannot access workshop pricing.
*   **Custom Order Workflow:** API routes dedicated to handling unlisted part requests, quotes, and approvals.
*   **Webhook Handlers:** Asynchronous endpoints ready to catch and process triggers from payment gateways and external 3PL delivery services.
*   **Database Isolation:** Robust MySQL relational models separating B2C orders, B2B orders, and custom requests.

---

## 📂 Project Structure

```text
backend/
│
├── config/                 # Database configuration and connection scripts
├── controllers/            # Core business logic for endpoints (auth, inventory, orders)
├── models/                 # Database schema definitions and ORM models
├── routes/                 # API endpoint routing definitions
├── utils/                  # Helper functions (password hashing, notifications)
├── .env.example            # Template for environment variables
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
└── README.md               # Backend documentation (You are here)
