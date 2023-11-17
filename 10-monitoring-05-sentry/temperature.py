import sentry_sdk
from pygismeteo import Gismeteo

def temperature_air(town):
    try:
        gismeteo = Gismeteo()
        search_results = gismeteo.search.by_query(town)
        city_id = search_results[0].id
        current = gismeteo.current.by_id(city_id)
        print(f'Температура в городе {town} составляет {current.temperature.air.c} градусов цельсия')
    except AttributeError:
        pass      

sentry_sdk.init(
    dsn="https://d463da0b5af9be72ed2cb06066bd6d21@o4506223878537216.ingest.sentry.io/4506234346340352",
    environment="development",
    release='1.0'
)

if __name__ == "__main__":
    temperature_air(town=input("Введите название города в котором вы хотите узнать температуру воздуха: "))