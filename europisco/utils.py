"""
Script con funciones utiles para el proceso
"""
import folium
import pandas as pd

def add_missing_geocode(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rellenamos manualmente información de localizaciones
    que el package geopy no encontró
    """
    df.loc[6, "latitude"] = 40.972546300325746
    df.loc[6, "longitude"] = -5.658419387328101
    df.loc[18, "latitude"] = 41.38006562275075
    df.loc[18, "longitude"] = 2.163010839291413
    df.loc[21, "latitude"] = 41.40293279969603
    df.loc[21, "longitude"] = 2.159256096961093
    df.loc[23, "latitude"] = 43.26163372566617
    df.loc[23, "longitude"] = -2.929120933831521
    df.loc[30, "latitude"] = 39.47078392527955
    df.loc[30, "longitude"] = -0.37138733009770314
    df.loc[32, "latitude"] = 41.40191119891952
    df.loc[32, "longitude"] = 2.154507805637604
    df.loc[45, "latitude"] = 38.7127794867824
    df.loc[45, "longitude"] = -9.137327763919329
    df.loc[47, "latitude"] = 53.34083826660188
    df.loc[47, "longitude"] = -6.24482527367974
    df.loc[48, "latitude"] = 53.342904383050765
    df.loc[48, "longitude"] = -6.236903285325631
    df.loc[49, "latitude"] = 41.40290997130236
    df.loc[49, "longitude"] = 2.1592672681276954
    df.loc[51, "latitude"] = 51.90172595208701
    df.loc[51, "longitude"] = -8.470310360254798
    df.loc[52, "latitude"] = 38.709764127838696
    df.loc[52, "longitude"] = -9.151407431973473
    df.loc[59, "latitude"] = 46.22150670601297
    df.loc[59, "longitude"] = 6.0956530670457125
    df.loc[69, "latitude"] = 40.4292948540896
    df.loc[69, "longitude"] = -3.673644174454475
    df.loc[73, "latitude"] = 38.964916663935924
    df.loc[73, "longitude"] = -9.417234623696746
    df.loc[86, "latitude"] = 39.61589090757615
    df.loc[86, "longitude"] = 2.705252368571537
    df.loc[88, "latitude"] = 38.909667696473214
    df.loc[88, "longitude"] = 1.4355332133343959
    df.loc[113, "latitude"] = 40.41763629833717
    df.loc[113, "longitude"] = -3.704811116568445
    df.loc[120, "latitude"] = 51.51430664403254
    df.loc[120, "longitude"] = -0.17540551511112104
    df.loc[121, "latitude"] = 41.554654136702574
    df.loc[121, "longitude"] = 2.0986853875424276
    df.loc[122, "latitude"] = 53.347946518816215
    df.loc[122, "longitude"] = -6.261642988640728
    df.loc[144, "latitude"] = 41.886411780046295
    df.loc[144, "longitude"] = 12.472420643711015
    df.loc[156, "latitude"] = 39.962617683800325
    df.loc[156, "longitude"] = -4.817903422418324
    df.loc[164, "latitude"] = 36.722722720729806
    df.loc[164, "longitude"] = -4.421907362981686
    df.loc[168, "latitude"] = 52.335601064944704
    df.loc[168, "longitude"] = -6.459070773663258
    df.loc[174, "latitude"] = 51.51430664403254
    df.loc[174, "longitude"] = -0.17540551511112104
    df.loc[183, "latitude"] = 47.56107982868368
    df.loc[183, "longitude"] = 7.592640489055312
    df.loc[187, "latitude"] = 52.41953431610891
    df.loc[187, "longitude"] = 9.792439901292278
    df.loc[193, "latitude"] = 52.62872890971545
    df.loc[193, "longitude"] = 1.292831732093453
    df.loc[195, "latitude"] = 53.347946518816215
    df.loc[195, "longitude"] = -6.261642988640728
    df.loc[203, "latitude"] = 40.40772969233442
    df.loc[203, "longitude"] = -3.703651318600535
    df.loc[204, "latitude"] = 51.51430664403254
    df.loc[204, "longitude"] = -0.17540551511112104
    df.loc[213, "latitude"] = 53.34086289380278
    df.loc[213, "longitude"] = -6.244776361603958
    df.loc[214, "latitude"] = 50.81501521279863
    df.loc[214, "longitude"] = 4.367106972592874

    return df

def add_marker(row:pd.Series, feature_groups: dict):
    """
    Agrega marcadores para el mapa html

    Args:
        row (pd.Series): Fila con la información de cada registro.
        feature_groups(dict): Diccionario con tipos de pisco y combinaciones.
    """
    popup_text = f"Tipo: {row['category']}<br>Precio: {row['price']}<br>Subido por: {row['name']}<br>Dirección: {row['address_clean']}"
    categories_in_row = row['category'].split(", ")
    for category in categories_in_row:
        if category in feature_groups:
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=popup_text,
                tooltip=row['category']
            ).add_to(feature_groups[category])
