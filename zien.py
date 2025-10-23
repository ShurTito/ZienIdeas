import sys
import requests
import json
import time

def generar_texto(prompt):
    # Usar un modelo en español más adecuado para generar historias
    API_URL = "https://api-inference.huggingface.co/models/bertin-project/bertin-gpt-j-6B"
    headers = {
        "Authorization": "Bearer token_de_acceso_aqui",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": f"Escribe una historia corta sobre: {prompt}",
        "parameters": {
            "max_length": 200,
            "temperature": 0.7,
            "top_p": 0.9
        }
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        if response.status_code == 503:
            print("El modelo se está cargando, espere por favor...")
            time.sleep(20)
            response = requests.post(API_URL, headers=headers, json=payload)
            
        result = response.json()
        
        if isinstance(result, list) and result:
            return result[0]['generated_text']
        elif isinstance(result, dict):
            return result.get('generated_text', 'No se pudo generar el texto')
        else:
            return "Error: Formato de respuesta no esperado"
            
    except requests.exceptions.RequestException as e:
        return f"Error de conexión: {str(e)}"
    except json.JSONDecodeError:
        return "Error: No se pudo decodificar la respuesta JSON"
    except Exception as e:
        return f"Error inesperado: {str(e)}"

def main():
    if len(sys.argv) != 2:
        print("Modo de uso: python3 zien.py <palabras clave>")
        sys.exit(1)

    prompt = sys.argv[1]
    print(f"Generando texto a partir del prompt: {prompt}")
    texto_generado = generar_texto(prompt)
    print("\nTexto generado:")
    print(texto_generado)

if __name__ == "__main__":
    main()