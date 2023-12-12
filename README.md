# IP-Geolocalisation

## Overview
This project retrieves information about your local machine's IP address and performs geolocation for a specified IPv6 address using the freegeoip.app API. It displays the computer name, local IP address, and geolocation information (latitude and longitude) on an interactive map.

## Features
- Fetches local machine's computer name and IP address.
- Retrieves geolocation information for a specified IPv6 address using the freegeoip.app API.
- Generates an interactive map with the target IP address's geolocation using Folium.
- Utilizes the `requests` and `folium` libraries for API calls and mapping, respectively.

## Getting Started
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-username/ip-geolocation.git
   ```
2. **Navigate to the project**
   ```sh
   cd ip-geolocalisation
   ``` 
3. **Run the script**
  ```sh
  python geolocation.py
  ```
Note: Make sure you have the required dependencies installed.

## Usage
1. The script will display your computer name and local IP address.
2. Enter the IPv6 address you want to geolocate when prompted.
3. The script will generate an interactive map (map.html) showcasing the geolocation of the specified IP address.

## Dependencies
- Requests: A Python library for making HTTP requests.
- Folium: A Python wrapper for Leaflet.js for mapping.

## API Key
Ensure you have an API key for freegeoip.app and replace the placeholder fd2233f0-3456-11ec-9eeb-c1b33a419b4f with your actual API key in the geolocation.py script.

## Contributing
Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.

