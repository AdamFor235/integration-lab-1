import requests
from django.shortcuts import render

weather_codes = {
    (0,): "czyste niebo",
    (1,): "głównie bezchmurnie",
    (2,): "częściowo pochmurno",
    (3,): "pochmurno",
    (45,): "mgła",
    (48,): "opadająca mgła szronowa",
    (51,): "mżawka lekka",
    (53,): "mżawka umiarkowana",
    (55,): "mżawka gęsta",
    (56,): "zamrażająca mżawka: lekka",
    (57,): "zamrażająca mżawka: gęsta intensywność",
    (61,): "deszcz słaby",
    (63,): "deszcz umiarkowany",
    (65,): "deszcz intensywny",
    (66,): "marznący deszcz: intensywność lekka",
    (67,): "marznący deszcz: intensywność ciężka",
    (71,): "opady śniegu: intensywność niewielka",
    (73,): "opady śniegu: intensywność umiarkowana",
    (75,): "opady śniegu: intensywność duża",
    (77,): "ziarna śniegu",
    (80,): "przelotne opady deszczu: słabe",
    (81,): "przelotne opady deszczu: umiarkowane",
    (82,): "przelotne opady deszczu: gwałtowne",
    (85,): "opady śniegu lekkie",
    (86,): "opady śniegu intensywne",
    (95,): "burza: Słaba lub umiarkowana",
    (96,): "burza z lekkim gradem",
    (99,): "burza z silnym gradem",
}

coordinates = {
    "Gowino": ("54.57", "18.20"),
    "Gdynia": ("54.52", "18.53"),
    "Warszawa": ("52.237", "21.017"),
    "Tokyo": ("35.65", "139.84")
}

def weather_view(request):
    place = "Gdynia"

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={coordinates[place][0]}"
        f"&longitude={coordinates[place][1]}"
        f"&hourly=temperature_2m,rain,weather_code,wind_speed_10m"
    )
    
    gdynia_weather= requests.get(weather_url).json()
    data = {}
    hourly = {}
    for key, value in gdynia_weather.items():
        if key != 'hourly':
            data[key] = value
        else:
            for key1, value1 in value.items():
                hourly[key1] = value1  

    num_hours = len(hourly['time'])
    rows = []
    for i in range(num_hours):
        row = {
            "time": hourly['time'][i],
            "temperature_2m": hourly['temperature_2m'][i],
            "rain": hourly['rain'][i],
            "weather_code": hourly['weather_code'][i],
            "wind_speed_10m": hourly['wind_speed_10m'][i],
        }
        rows.append(row)
    Dane = {
        "place": place,
        "weather_url": weather_url,
        "general_data": data,
        "hourly_data": rows
    }
    return render(request, "external_data/weather.html", Dane)