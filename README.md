# Automobile Parts Network Platform 🚗🛠️

An interconnected B2B and B2C marketplace designed to streamline the procurement of automobile parts locally within Qatar. This platform bridges the gap between local parts shops, automobile workshops, and everyday retail customers through dynamic pricing tiers, third-party logistics (3PL) integration, and automated notification systems.

---

## 🏗️ System Architecture

This repository is organized into a monorepo structure containing both the mobile application frontend and the API backend.

*   **[`/frontend`](./frontend/)**: Cross-platform mobile application built with Flutter (Dart).
*   **[`/backend`](./backend/)**: RESTful API and core business logic built with Python and MySQL.

## ✨ Core Platform Modules

1.  **End-Customer Portal (B2C):** Public-facing retail interface with standard pricing and real-time order tracking.
2.  **Workshop Portal (B2B):** Secure, password-protected portal granting access to wholesale pricing and the ability to submit custom requests for unlisted parts.
3.  **Parts Shop Portal (Sellers):** Inventory management, dynamic pricing tier controls, and custom order quoting.
4.  **Logistics & Notifications:** Automated payment webhooks and API integrations with external B2B delivery channels (3PL).

---

## 🗺️ Roadmap (Qatar Phase 1)

*   **Months 1-6 (Development):** UI development, API integrations, and core feature mapping.
*   **Months 7-8 (Testing):** System integration testing, focusing on pricing tier security and 3PL data flows.
*   **Months 9-10 (Audits):** Penetration testing on payment gateways and database load testing.
*   **Months 11-12 (Deployment):** UAT, staging deployment, and production launch.

*For specific setup instructions, please refer to the README files within the `frontend` and `backend` directories.*
