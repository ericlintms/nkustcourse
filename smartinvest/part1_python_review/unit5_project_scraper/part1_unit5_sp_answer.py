import requests
from bs4 import BeautifulSoup

def scrape_heading(url):
    """
    從給定的 URL 爬取 H1 標題。
    """
    try:
        response = requests.get(url, timeout=5)
        # 如果狀態碼是 4xx 或 5xx，則引發例外
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        heading = soup.find('h1')

        if heading:
            print(f"The main heading is: '{heading.text.strip()}'")
        else:
            print("No H1 heading found on the page.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the web request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# 範例
scrape_heading('http://example.com')

# 要執行此腳本，請先安裝必要的函式庫：
# pip install requests beautifulsoup4
