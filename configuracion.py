import os
from pathlib import Path


DIRECTORIO_BASE = Path(__file__).resolve().parent


class Configuracion:
    CLAVE_API_GOOGLE = ("AIzaSyBI7-JK1Ll0OQGwG7n0tTdkQAYRDN4f094")

    TIPO_VEHICULO_PREDETERMINADO = "GASOLINE"
    PRECIO_GASOLINA_MXN = 23.99
    RENDIMIENTO_PREDETERMINADO_KM_L = 14.0

    ARCHIVO_ZONAS = DIRECTORIO_BASE / "data" / "zonas_rojas.json"
    TIEMPO_ESPERA_GOOGLE_SEGUNDOS = 35

    SERVIDOR = "0.0.0.0"
    PUERTO = int(os.environ.get("PORT", 5000))
    DEPURACION = False  # ← False en producción

    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False