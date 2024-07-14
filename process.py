"""
Script principal de limpieza y generación de mapa
"""
import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
# from folium.plugins import Search
from utils import add_missing_geocode, add_marker

print("Comienzo del proceso de limpieza y creación de mapa")
# Leemos los datos pre-procesados del formulario
df = pd.read_csv("data/europisco.csv")

# Eliminamos columnas con información confidencial
df.drop(columns=["Email Address", "Cuál es tu correo? (opcional)"], inplace=True)

# Renombre de columnas
df.rename(
    columns={
        "Timestamp": "timestamp",
        "Cúal es la dirección exacta (o más aproximada) dónde viste el pisco?": "address_raw",
        "En qué país?": "country",
        "Qué era específicamente?": "pisco_type",
        "Cúanto costaba aproximadamente (en euros)?": "price",
        "Cuál es tu nombre? (opcional)": "name",
        "Probable address": "address_clean"
    },
    inplace=True
)

# Borramos aquellos dónde no hay dirección específica
df.dropna(subset=['address_clean'], inplace=True)

df.reset_index(inplace=True, drop=True)

# Agregamos información de geolocalización
geolocator = Nominatim(user_agent="BuscandoElPisco")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

print("Obteniendo latitud y longitud...")
# Creamos las columnas con la información
df['location'] = df['address_clean'].apply(geocode)
df['latitude'] = df['location'].apply(lambda loc: loc.latitude if loc else None)
df['longitude'] = df['location'].apply(lambda loc: loc.longitude if loc else None)

df = add_missing_geocode(df)

# Generamos la tabla ya limpiada para usar con Google My Maps
df.to_csv("./processed/europisco_location.csv", index=False)
print("Tabla limpiada para subir a Google guardada en /processed...")

# Alternativamente, generamos también un mapa html
# Primero, centramos el mapa en Europa
m = folium.Map(location=[54.5260, 15.2551], zoom_start=4)

# Definimos tipos de pisco
pisco_types = ["Botella", "Piscola", "Pisco Sour"]

# Creamos un grupo por cada tipo y combinación de tipo
feature_groups = {ptype: folium.FeatureGroup(name=ptype).add_to(m) for ptype in pisco_types}

# Aplicamos función para agregar marcadores al mapa
df.apply(add_marker, args=(feature_groups,), axis=1)

# Agregamos layers al mapa para filtrar por tipo
folium.LayerControl().add_to(m)

# Guardamos el mapa como html
m.save('out/pisco_map.html')
print("Mapa guardado en out/")
input("Presionar enter para terminar...")
