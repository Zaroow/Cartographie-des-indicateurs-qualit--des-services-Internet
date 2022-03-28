import folium
import pandas as pd
import numpy as np

print("Programme lecture de base de données")
import pandas as pd
import io


##### 01) Importation de la base de données
df_dataVO = pd.read_csv('SelectedData.csv', sep=";", header=0)

### Create loaclisation Paris
c = folium.Map(location=[48.856614, 2.3522219], zoom_start=12)
### Création des points d'interêts
for i in range(len(df_dataVO)):
    print("i = ", i)
    html = f"""
                        <h2>Service: {df_dataVO.protocol[i]}</h2>
                        <ul>
                            <li>Location: {df_dataVO.name[i]}</li>
                            <li>OPERATOR : {df_dataVO.sim_provider[i]}</li>
                            <li>Environnement: {df_dataVO.user_location_type[i]}</li>
                        </ul>
                        <h3>Quality: {df_dataVO.quality[i]}</h3>
                        <ul>
                            <li>RSRP level: {df_dataVO.trace_cellular_lte_rsrp[i]} dBm</li>
                            <li>Bandwidth : {df_dataVO.trace_cellular_bandwidth[i]} kBps</li>
                            <li>Jitter: {df_dataVO.launch_duration[i]} ms</li>
                        </ul>
                        """
    iframe = folium.IFrame(html, width=300, height=300)
    popup = folium.Popup(iframe, max_width=300)
    if df_dataVO.quality[i] == "Excellent":
        folium.Marker(location=[df_dataVO.location_latitude[i], df_dataVO.location_longitude[i]], popup=popup, icon=folium.Icon(color="blue", icon="info-sign")).add_to(c)
    elif df_dataVO.quality[i] == "Good":
        folium.Marker(location=[df_dataVO.location_latitude[i], df_dataVO.location_longitude[i]], popup=popup,icon=folium.Icon(color="green", icon="info-sign")).add_to(c)
    elif df_dataVO.quality[i] == "Middle Cell":
        folium.Marker(location=[df_dataVO.location_latitude[i], df_dataVO.location_longitude[i]], popup=popup,icon=folium.Icon(color="orange", icon="info-sign")).add_to(c)
    elif df_dataVO.quality[i] == "Cell Edge":
        folium.Marker(location=[df_dataVO.location_latitude[i], df_dataVO.location_longitude[i]], popup=popup,icon=folium.Icon(color="red", icon="info-sign")).add_to(c)
c.save('maCarte3.html')
print("Map done")