# agents.py
from swarm import Agent
from prompts import main_agent_system_prompt, calendar_agent_system_prompt
from calendar_tools import list_calendar_lists, list_calendar_events, insert_calendar_event, create_calendar_list

MODEL = 'gpt-4o-mini'

def transfer_to_main_agent():
    return main_agent

def transfer_to_calendar_agent():
    return calendar_agent

main_agent = Agent(
    name="Main Agent",
    model=MODEL,
    instructions=main_agent_system_prompt,
    functions=[transfer_to_calendar_agent]
)

calendar_agent = Agent(
    name="Google Calendar Agent",
    model=MODEL,
    instructions=calendar_agent_system_prompt,
    functions=[transfer_to_main_agent]
)

calendar_agent.functions.extend([
    list_calendar_lists,
    list_calendar_events,
    insert_calendar_event,
    create_calendar_list
])