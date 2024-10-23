import requests
import socket
import json

# Función para obtener información WHOIS usando la librería whois
def obtener_info_whois(dominio):
    try:
        # Consultar información WHOIS del dominio usando la librería whois
        info = whois.query(dominio)

        # Verificar si se pudo obtener la información
        if info is None:
            print(f"No se pudo obtener información para el dominio: {dominio}")
            return

        # Imprimir la información WHOIS obtenida
        print(f"\nInformación WHOIS para el dominio: {dominio}")
        print(f"Nombre del Dominio: {info.name}")
        print(f"Registro (Registrar): {info.registrar}")
        print(f"Fechas de Registro:")
        print(f"  Creado: {info.creation_date}")
        print(f"  Actualizado: {info.last_updated}")
        print(f"  Expiración: {info.expiration_date}")
        print(f"Servidores DNS: {info.name_servers}")

    except Exception as e:
        print(f"Error al obtener información de WHOIS para '{dominio}': {e}")

# Función para obtener información WHOIS mediante la API de WhoisXML
def obtener_info_whois_api(dominio, api_key):
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?domainName={dominio}&apiKey={api_key}&outputFormat=JSON"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        whois_record = data.get('WhoisRecord', {})

        # Imprimir la información WHOIS obtenida de manera estructurada
        print(f"\nInformación WHOIS para el dominio '{dominio}':")
        print(f"Nombre del Dominio: {whois_record.get('domainName', 'N/A')}")
        print(f"Organización Registrante: {whois_record.get('registrant', {}).get('organization', 'N/A')}")
        print(f"Correo de Contacto: {whois_record.get('registrant', {}).get('email', 'N/A')}")
        print(f"Teléfono de Contacto: {whois_record.get('registrant', {}).get('telephone', 'N/A')}")
        print(f"Dirección Registrante: {whois_record.get('registrant', {}).get('street1', 'N/A')}, {whois_record.get('registrant', {}).get('city', 'N/A')}, {whois_record.get('registrant', {}).get('country', 'N/A')}")
        print(f"Servidores DNS: {', '.join(whois_record.get('nameServers', {}).get('hostNames', []))}")
        print(f"Fecha de Creación: {whois_record.get('createdDate', 'N/A')}")
        print(f"Fecha de Actualización: {whois_record.get('updatedDate', 'N/A')}")
        print(f"Fecha de Expiración: {whois_record.get('expiresDate', 'N/A')}")
        print(f"Estado del Dominio: {whois_record.get('status', 'N/A')}")
    else:
        print(f"Error en la consulta WHOIS: {response.status_code}, {response.text}")

if __name__ == "__main__":
    api_key = "AQUI API"  # Clave de API proporcionada
    while True:
        entrada = input("\nIntroduce el dominio para obtener información WHOIS (o 'salir' para finalizar): ")
        if entrada.lower() == 'salir':
            break
        # Primero intentamos obtener la información con la librería whois
        if entrada.endswith(".com") or entrada.endswith(".net") or entrada.endswith(".org"):
            obtener_info_whois(entrada)
        else:
            obtener_info_whois_api(entrada, api_key)
