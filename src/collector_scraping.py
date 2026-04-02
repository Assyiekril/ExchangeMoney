import pandas as pd
from datetime import datetime
import os
import warnings

# Bungkam peringatan SSL biar terminal bersih
warnings.filterwarnings("ignore")

def scrape_yahoo_finance():
    try:
        print("--- Memulai Pengambilan Data (Yahoo Finance - IDR Kurs) ---")
        
        # URL Yahoo Finance untuk Currency Converter (USD to IDR)
        # Kita ambil tabel 'Top Currencies' yang biasanya ada di halaman market
        url = "https://finance.yahoo.com/currencies"
        
        # Headers biar dikira browser beneran
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Gunakan read_html langsung dengan storage_options untuk header
        # Ini cara paling 'Big Data' karena efisien
        tables = pd.read_html(url, storage_options=headers)
        
        if tables:
            df = tables[0] # Ambil tabel utama
            
            # Preprocessing sederhana
            df['Source'] = 'Yahoo Finance'
            df['Scrape_Time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Pastiin folder data ada
            if not os.path.exists('data'):
                os.makedirs('data')
                
            output_path = 'data/currency_rates_scraping.csv'
            df.to_csv(output_path, index=False)
            
            print(f"✅ AKHIRNYA SUKSES! Data disimpan di: {output_path}")
            print("\nPreview Data:")
            print(df.head())
        else:
            print("❌ Tabel tetap tidak ditemukan.")
            
    except Exception as e:
        print(f"⚠️ TERJADI ERROR: {e}")
        print("Tips: Pastiin internet lu lancar ya Nul.")

if __name__ == "__main__":
    scrape_yahoo_finance()