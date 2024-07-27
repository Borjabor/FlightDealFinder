# Flight Deal Finder

## Description
This project was an exploration into Object Oriented Programming (OOP), and API usage by doing something relatively useful. 
It uses Sheety API to edit and fetch data from spreadsheets with city information and desired lowest ticket price.
![image](https://github.com/user-attachments/assets/bdaaa830-26e3-4ef4-979b-2c87b9953d5c)

Then, it uses that data to connect to the Amadeus API and search for tickets witht the desired parameters.
Finally, it sends whatever deals it finds through SMS or WhatsApp using the Twilio API, or by email  with smtplib to all the users in another spreadsheet, populated with a Google form.
The script searched within a 7-day period, 1 month ahead, for the cheapest flights.

## Installation
1. Clone the repository.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Set up environment variables for Twilio SID, Auth token and virtual number, your personal phone number (to receive the message), the email and password for the email that will send out the deals (I used Gmail, and created an App password), for the endpoints and Bearer token for the Sheety API and spreadsheets, and finally for the Amadeus Key and Secret

## Usage
Run the `main()` function in the script to get ticket data according to the cities chosen inside the spreadsheet.
You should receive notifications with all the deals found, or an "N/A" if nothing was found

## NOTE!
The data found through Amadeus wasn't the best, and the purchase of the tickets would need more functionality. This was simply an exploration and learning experience for myself
