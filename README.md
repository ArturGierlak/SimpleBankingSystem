# SimpleBankingSystem

## 📘 Project Description

This project is a lightweight FastAPI application designed to manage simple financial transactions, such as deposits and withdrawals, for individual clients.  
The codebase is structured around a clean, modular architecture built on top of **SQLAlchemy**, **Pydantic**, and **FastAPI’s dependency injection** model.

The application is split into clear layers:

*   **Models** – database entities defining clients and transactions
*   **Repositories** – low‑level data access logic, isolated from the rest of the system
*   **Services** – the core business logic, responsible for validation and transaction processing
*   **API layer** – FastAPI routers exposing clean HTTP endpoints

This separation keeps the code easy to maintain, reason about, and extend over time.

The API includes an interactive **Swagger UI** available at `/docs`, allowing you to test all endpoints directly from the browser.

The project also contains a focused test suite covering the full transaction workflow.  
Tests are written for:

*   the **repository layer** (database operations using SQLite in‑memory),
*   the **service layer** (business logic with mocked repositories),
*   and the **API layer** (FastAPI endpoints using dependency overrides).

At the moment, the tests cover only transaction-related functionality - client-related operations are not yet included.

Overall, this project provides a compact, basic but realistic example of building a small domain-focused backend using FastAPI.