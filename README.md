# Google-Ads-Transparency-scraper
A Selenium-powered scraper that extracts the number of Google Ads displayed by multiple domains over the last 7 days. Reads domain URLs from an Excel file and automatically updates the ad counts back into the same file. Ideal for ad transparency research, competitive analysis, and automated data collection.

# Google Ads Transparency Scraper (Selenium + Python)

This project is a powerful **Selenium-based web scraper** that extracts the **number of ads shown by companies** on the Google Ads Transparency platform.

The script reads a list of company URLs from an Excel file (`urls.xlsx`), automatically converts them to domains, fetches their **7-day ads count**, and writes the results back into the same file.

---

## ✨ Features

- 🚀 Scrapes **Google Ads Transparency** pages using Selenium  
- 📂 Reads company URLs from `urls.xlsx`  
- 🔍 Automatically extracts domain names from full URLs  
- 📊 Collects the **last 7 days' ads count**  
- ✏ Saves results into the **"no of ads"** column  
- 🛡️ Includes robust waits and error handling  
- 🖥 Works on any OS where Python & Chrome are installed  

---

## 📝 Excel File Format

Your `urls.xlsx` must contain two columns:

| url | no of ads |
|-------------------|-----------|
| https://oerb.com | |
| https://nike.com | |

The script fills the **no of ads** column automatically.

---

## 📦 Installation

Install Python dependencies:

```bash
pip install selenium webdriver-manager pandas openpyxl tldextract
