import requests
import re

def banner():
    print("""
    ===================================
       OSINT TRACE - BY DEWEYS-S12
    ===================================
    """)

def check_system_ip():
    # Usando la API de ipquery.io que compartiste
    try:
        r = requests.get("https://api.ipquery.io/?format=json")
        data = r.json()
        print(f"[*] Tu IP: {data['ip']} | ISP: {data['isp']['isp']}")
        print(f"[*] Ubicación: {data['location']['city']}, {data['location']['country']}\n")
    except:
        print("[!] No se pudo conectar con IPQuery\n")

def trace_tiktok(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        print(f"[+] Analizando enlace...")
        response = requests.get(url, headers=headers, allow_redirects=True)
        final_url = response.url
        
        # Extraer el ID de usuario mediante Regex
        match = re.search(r'@([a-zA-Z0-9._-]+)', final_url)
        
        if match:
            username = match.group(1)
            print("\n[SUCCESS] Identidad extraída:")
            print(f"-------------------------------")
            print(f"Perfil: https://www.tiktok.com/@{username}")
            print(f"Username: {username}")
            print(f"URL Final: {final_url}")
            print(f"-------------------------------")
        else:
            print("\n[-] No se encontraron metadatos de identidad en el enlace.")
    except Exception as e:
        print(f"\n[!] Error en el rastreo: {e}")

if __name__ == "__main__":
    banner()
    check_system_ip()
    target = input("Introduce el link de TikTok: ")
    trace_tiktok(target)

