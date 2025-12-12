import pandas as pd
import time
import tldextract
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ================= CONFIG =================
INPUT_FILE = "urls.xlsx"      # your file
OUTPUT_FILE = "urlsdata.xlsx"     # overwrite same file
WAIT_TIME = 20
# ==========================================

# Read your Excel
df = pd.read_excel(INPUT_FILE)

# Make sure correct columns exist
assert "url" in df.columns, "ERROR: Excel must have a column named 'url'"
assert "no of ads" in df.columns, "ERROR: Excel must have a column named 'no of ads'"

# Selenium options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for index, row in df.iterrows():

    full_url = row["url"]

    # Extract domain cleanly
    extracted = tldextract.extract(full_url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    print(f"\n🔎 Scraping ads for: {domain}")

    # Build Google Ads Transparency URL
    target = f"https://adstransparency.google.com/?region=US&domain={domain}&preset-date=Last+7+days"
    driver.get(target)

    try:
        wait = WebDriverWait(driver, WAIT_TIME)
        element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.ads-count.ads-count-searchable")
            )
        )
        ads_text = element.text.strip()
        ads_count = ads_text.split()[0]

        print(f"➡ Ads Count: {ads_count}")

    except:
        print("❌ Could not load ads count")
        ads_count = "N/A"

    # Store result back into DataFrame
    df.at[index, "no of ads"] = ads_count

    time.sleep(2)

driver.quit()

# Save results back to the same file
df.to_excel(OUTPUT_FILE, index=False)

print("\n✅ FINISHED! Ads count saved into 'urls.xlsx'")