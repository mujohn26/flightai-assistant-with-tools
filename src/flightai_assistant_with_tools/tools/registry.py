import json

from .ticket_price import get_ticket_price

def handle_tool_calls(message):
	responses = []

	for tool_call in message.tool_calls:
		if tool_call.function.name == "get_ticket_price":
			arguments = json.loads(tool_call.function.arguments)
			city = arguments.get("destination_city")
			price_details = get_ticket_price(city)

			responses.append({
				"role": "tool",
				"content": price_details,
				"tool_call_id": tool_call.id
			})

			return responses