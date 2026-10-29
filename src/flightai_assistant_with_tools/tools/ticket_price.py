import sqlite3

from ..database.db import get_connection

TICKET_PRICES = {"london": "$345", "paris": "$573", "tokyo": "1400", "berlin": "342"}

DB = "data/prices.db"


def get_ticket_price(destination_city):
	print(f"DATABASE TOOL CALLED: Getting price for {destination_city} ", flush=True)
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT price FROM prices WHERE city = ?", (destination_city.lower(),))
	result = cursor.fetchone()
	return f"Ticket price to {destination_city} is ${result[0]}" if result else "No Price data available for this city"



def tools():
	tools_array = [{"type": "function", "function": schema}]

	return tools_array


schema = {
	"name": "get_ticket_price",
	"description": "Get a price of a return ticket to the destination city",
	"parameters":{
		"type": "object",
		"properties":{
			"destination_city":{
				"type": "string",
				"description":"The city that you want to travel to"
			}
		},
		"required": ["destination_city"],
		"additionalProperties": False
	}
}