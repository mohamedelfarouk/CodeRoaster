# ☕ The Code Roaster API

**"Code reviews, but make them hurtful."**

A FastAPI backend that uses Google's Gemini 2.5 Flash to automatically review code, detect bugs, and provide a "roast" (sarcastic critique) alongside a serious refactor.

### 🏗 Architecture Decisions

I built this project to demonstrate **Clean Architecture** patterns in modern Python:

- **FastAPI & Pydantic V2:** For strict strict data validation and high-performance async handling.
- **Layered Design:** Separated `Router` (Interface), `Service` (Business Logic), and `Schemas` (Data Contract) to allow for easy testing and swapping of AI providers.
- **Structured AI Output:** Uses prompt engineering to force the LLM into returning strict JSON, ensuring the API never breaks due to "chatty" AI responses.

### 🛠 Tech Stack

- **Framework:** FastAPI
- **AI Engine:** Google Gemini 2.5 Flash (via `google-generativeai`)
- **Dependency Management:** Poetry

### 🚀 How to Run

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/mohamedelfarouk/CodeRoaster.git
    ```
2.  **Install dependencies:**
    ```bash
    poetry install
    ```
3.  **Set up keys:**
    Create a `.env` file and add: `GEMINI_API_KEY=your_key_here`
4.  **Run the server:**
    ```bash
    poetry run uvicorn app.main:app --reload
    ```
5.  **Test:** Open `http://localhost:8000/docs` and roast some code!
