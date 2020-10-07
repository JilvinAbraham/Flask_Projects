import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    city = "delhi"

    if request.method == 'POST':

        new_city = request.form.get('city')

        if new_city == "" or new_city is None:
            city = "delhi"
        else:
            city = str(new_city)

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=645183e67fb897eb16867da750323622'
    r = requests.get(url.format(city)).json()

    temp = r.get('main', {}).get('temp')
    weather = {
        'city': city,
        'description': r["weather"][0]["description"],
        'temperature': int(round(temp - 273.15, 2)),
        'humidity': r.get('main', {}).get('humidity'),
        'wind': r.get('wind', {}).get('speed'),
        'pressure': r.get('main', {}).get('pressure')

    }
    return render_template('home.html', weather=weather)


if __name__ == "__main__":
    app.run(debug=True)
