# Court-Data Fetcher

- **Court chosen:** Delhi High Court (https://delhihighcourt.nic.in/)
- **Stack:** Python Flask, SQLite, Playwright for scraping.
- **CAPTCHA handling:** Uses Playwright for automated browser; if CAPTCHA not solvable, prompt manual entry.
- **Run steps:** 
    1. `python3 -m venv venv && source venv/bin/activate`
    2. `pip install -r requirements.txt`
    3. `python app.py`
- **Sample .env variables:** (none for now; set `SECRET_KEY`)
- **Scraping law:** For demo only; respect court site terms.

## To Do:
- Dockerfile.
- Pagination for multiple orders.
- More robust CAPTCHA/JS logic.
