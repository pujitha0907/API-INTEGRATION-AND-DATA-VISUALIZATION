import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Step 1: Set your API key and city name
API_KEY = 'YOUR_API_KEY'  # 🔑 Replace with your actual API key from OpenWeatherMap
CITY = 'Hyderabad'

# Step 2: Prepare the API URL
url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Step 3: Fetch the weather data
response = requests.get(url)
data = response.json()

# Step 4: Extract date and temperature at 12 PM for each day
dates = []
temperatures = []

for forecast in data['list']:
    if "12:00:00" in forecast['dt_txt']:
        date = datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S").date()
        temp = forecast['main']['temp']
        dates.append(date)
        temperatures.append(temp)

# Step 5: Create a line chart using matplotlib
plt.figure(figsize=(10, 5))
plt.plot(dates, temperatures, marker='o', color='teal', linestyle='-')
plt.title(f"5-Day Temperature Forecast in {CITY}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("weather_output.png")  # Save the graph as an image
plt.show()
