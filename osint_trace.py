import requests
import re

def banner():
    print("""
    ===========================================
       OSINT TRACE + MAPS - BY DEWEYS-S12
    ===========================================
    """)

def check_system_ip():
    try:
        # Usamos la API de ipquery.io que entrega coordenadas
        r = requests.get("https://api.ipquery.io/?format=json")
        data = r.json()
        
        ip = data.get('ip', 'N/A')
        isp = data['isp'].get('isp', 'N/A')
        city = data['location'].get('city', 'N/A')
        country = data['location'].get('country', 'N/A')
        
        # Extracción de coordenadas para Google Maps
        lat = data['location'].get('latitude')
        lon = data['location'].get('longitude')
        
        print(f"[*] Datos de Red Detectados:")
        print(f"    IP: {ip}")
        print(f"    Proveedor: {isp}")
        print(f"    Ubicación: {city}, {country}")
        
        if lat and lon:
            # Generamos el enlace de Google Maps
            maps_url = f"https://www.google.com/maps?q={lat},{lon}"
            print(f"    Coordenadas: {lat}, {lon}")
            print(f"    Google Maps: {maps_url}")
        print("-" * 43 + "\n")
        
    except Exception as e:
        print(f"[!] Error al conectar con la API de IP: {e}\n")

def trace_tiktok(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        print(f"[+] Rastreando identidad del emisor...")
        response = requests.get(url, headers=headers, allow_redirects=True)
        final_url = response.url
        
        match = re.search(r'@([a-zA-Z0-9._-]+)', final_url)
        
        if match:
            username = match.group(1)
            print("\n[IDENTIDAD ENCONTRADA]")
            print(f"User: @{username}")
            print(f"Perfil: https://www.tiktok.com/@{username}")
        else:
            print("\n[-] No se detectó usuario en el enlace (link limpio).")
            
    except Exception as e:
        print(f"\n[!] Error en el rastreo: {e}")

if __name__ == "__main__":
    banner()
    check_system_ip()
    target = input("Introduce el link de TikTok: ")
    trace_tiktok(target)

