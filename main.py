from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/weather")
def get_weather():
    city = request.args.get("City")

    # check for empty strings or strings with spaces
    if not bool(city.strip()):
        city = "Bangalore"

    # get weather data from API
    weather_data = get_current_weather(city)

    # city not found by the API
    if not weather_data["cod"] == 200:
        return render_template("city-not-found.html")

    # return weather data once city is found
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}°C",
        feels=f"{weather_data['main']['feels_like']:.1f}°C",
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
