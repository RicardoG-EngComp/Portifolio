import requests
import pandas

open_meteo = "https://api.open-meteo.com/v1/forecast?latitude=-20.7539&longitude=-42.8819&daily=temperature_2m_max,rain_sum,uv_index_max,uv_index_clear_sky_max,shortwave_radiation_sum,apparent_temperature_max,temperature_2m_min,apparent_temperature_min&hourly=temperature_2m,relative_humidity_2m,rain,shortwave_radiation,direct_radiation,direct_normal_irradiance,shortwave_radiation_instant,direct_radiation_instant,direct_normal_irradiance_instant&current=temperature_2m,rain&timezone=America%2FSao_Paulo&forecast_days=3"

resposta = requests.get(open_meteo)

print("Status da conexão:", resposta.status_code)

dados_brutos = resposta.json()

tabela_clima = pandas.DataFrame(dados_brutos["daily"])

tabela_clima['Alerta_Chuva'] = 'Sem chuva'
tabela_clima['Alerta_Calor_UV'] = 'Clima agradável'
tabela_clima.loc[ tabela_clima['rain_sum'] > 0, 'Alerta_Chuva' ] = 'Levar capa de chuva!'
tabela_clima.loc[ tabela_clima['temperature_2m_max'] > 25, 'Alerta_Calor_UV'] = 'Usar protetor solar e se hidratar'

print("\n--- Matéria_Prima Coletada ---")
print(tabela_clima)

tabela_clima.to_csv('alertas_entregadores.csv', index=False)