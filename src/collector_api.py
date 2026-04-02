import requests
import pandas as pd
import os
from datetime import datetime

# GANTI INI dengan API Key lu yang baru
API_KEY = '38c29567ed2e60ce3329c403' 
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

def fetch_exchange_rates():
    try:
        print("--- Memulai Pengambilan Data API ---")
        response = requests.get(BASE_URL)
        
        if response.status_code == 200:
            data = response.json()
            rates = data['conversion_rates']
            
            # Buat DataFrame
            df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Rate'])
            df['Last_Updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Pastiin folder data ada
            if not os.path.exists('data'):
                os.makedirs('data')
                
            # Simpan ke CSV
            output_path = 'data/currency_rates_api.csv'
            df.to_csv(output_path, index=False)
            
            print(f"✅ SUKSES! Data berhasil disimpan di: {output_path}")
            print("\nPreview Data (5 Baris Pertama):")
            print(df.head())
        else:
            print(f"❌ GAGAL! Status Code: {response.status_code}")
            print(f"Pesan Error: {response.text}")
            
    except Exception as e:
        print(f"⚠️ TERJADI ERROR: {e}")

if __name__ == "__main__":
    fetch_exchange_rates()