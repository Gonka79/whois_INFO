# WHOIS Query Tool with Python and WhoisXML API

This project allows you to obtain detailed geographical information about a domain using the **WhoisXML** API or the `whois` library. The script provides a simple and detailed query for domains like `.com`, `.net`, `.org`, and others through an API.

## Features

- Detailed WHOIS information query for domains.
- Uses the `whois` library for common domains (`.com`, `.net`, `.org`).
- Uses the **WhoisXML** API for other domains (e.g., `.es`).

## Requirements

- Python 3.x
- `requests` and `socket` for performing queries.
- **WhoisXML** API key for restricted domain queries.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script to enter a domain and get detailed WHOIS information:

```bash
python3 whois_info.py
```

Enter the domain you want to query when prompted. The script will retrieve and display detailed WHOIS information for the domain.

## Get the WhoisXML API Key

To perform WHOIS queries using the API, you need to register at [WhoisXML API](https://www.whoisxmlapi.com/) and obtain an **API key**. Once registered, paste your key into the script to perform queries.

## Example Output

The information obtained may include:

- Domain Name
- Registrant Organization
- Contact Email and Phone Number
- DNS Servers
- Domain creation, update, and expiration dates

## Contributions

Contributions are welcome. You can fork the repository and submit a Pull Request with improvements or fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

# Herramienta de Consulta WHOIS con Python y WhoisXML API

Este proyecto permite obtener información geográfica detallada sobre un dominio usando la API de **WhoisXML** o la librería `whois`. El script ofrece una consulta simple y detallada sobre dominios `.com`, `.net`, `.org` y otros dominios a través de una API.

## Características

- Consulta información WHOIS detallada para dominios.
- Usa la librería `whois` para dominios comunes (`.com`, `.net`, `.org`).
- Usa la **API de WhoisXML** para otros dominios (ej., `.es`).

## Requisitos

- Python 3.x
- `requests` y `socket` para realizar las consultas.
- Clave de API de **WhoisXML** para las consultas de dominios restringidos.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repositorio.git
   cd nombre-del-repositorio
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta el script para ingresar un dominio y obtener la información WHOIS detallada:

```bash
python3 whois_info.py
```

Introduce el dominio que deseas consultar cuando se te solicite. El script obtendrá y mostrará la información detallada de WHOIS del dominio.

## Obtener la Clave de API de WhoisXML

Para realizar consultas WHOIS con la API, debes registrarte en [WhoisXML API](https://www.whoisxmlapi.com/) y obtener una **clave de API**. Una vez registrada, puedes pegar tu clave en el script para realizar consultas.

## Ejemplo de Salida

La información obtenida puede incluir:

- Nombre del Dominio
- Organización Registrante
- Correo y Teléfono de Contacto
- Servidores DNS
- Fechas de creación, actualización y expiración del dominio

## Contribuciones

Las contribuciones son bienvenidas. Puedes hacer un fork del repositorio y enviar un Pull Request con mejoras o correcciones.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.


