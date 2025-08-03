import requests
from bs4 import BeautifulSoup

def fetch_case_metadata(case_type, case_number, filing_year):
    # Delhi HC site has viewstate/CAPTCHA. For demo, scrape first page (simulate result).
    payload = {
        'case_type': case_type,
        'case_no': case_number,
        'case_year': filing_year,
        # Add all necessary params as in the actual POST
    }
    # In prod, you would use Playwright to render JS and handle CAPTCHA. Here we mock response.
    url = "https://delhihighcourt.nic.in/case.asp"

    session = requests.Session()
    try:
        resp = session.get(url)
        # Parse ViewState if needed (hidden inputs)
        # ...extract, add to payload
        # For simplicity, assuming direct POST
        resp2 = session.post(url, data=payload)
        soup = BeautifulSoup(resp2.text, "html.parser")
        # Parse - fill selectors as per actual site (here, placeholders)
        parties = soup.find("span", id="parties").get_text(strip=True)
        filing_date = soup.find("span", id="filing_date").get_text(strip=True)
        next_hearing = soup.find("span", id="next_hearing").get_text(strip=True)
        order_links = [
            a['href'] for a in soup.find_all("a") if a['href'].endswith('.pdf')
        ]
        latest_order = order_links[-1] if order_links else None
        return {
            'parties': parties,
            'filing_date': filing_date,
            'next_hearing': next_hearing,
            'latest_order': latest_order,
            'raw_html': resp2.text
        }

    except Exception as e:
        return {'error': str(e), 'raw_html': ''}

