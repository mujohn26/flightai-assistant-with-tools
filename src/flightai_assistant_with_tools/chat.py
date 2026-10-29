from pathlib import Path

from .config_client import client, llm_model_name
from .tools.ticket_price import tools
from .tools.registry import handle_tool_calls

BASE_DIR = Path(__file__).resolve().parents[2]
system_prompts = (BASE_DIR / "prompts" / "system.txt").read_text(encoding="utf-8")

def chat(message, history):
	history = [{"role": h['role'], "content": h['content']} for h in history]
	messages = [{"role": "system", "content": system_prompts}] + history + [{"role": "user", "content": message}]
	response = client.chat.completions.create(model=llm_model_name, messages=messages, tools=tools())

	while response.choices[0].finish_reason == "tool_calls":
		assistant_msg =  response.choices[0].message
		messages.append(assistant_msg)
		messages.extend(handle_tool_calls(assistant_msg))
		response = client.chat.completions.create(model=llm_model_name, messages=messages, tools=tools())

	return response.choices[0].message.content