from fastapi import APIRouter
import os
import importlib

current_directory = os.path.dirname(os.path.abspath(__file__))
agents_directory = os.path.join(current_directory, "hub")

functions = []

agent_router = APIRouter(
    prefix="/agent",
)

for file_name in os.listdir(agents_directory):
    if file_name.endswith(".py") and file_name != "__init__.py":
        module_name = file_name[:-3]
        module = importlib.import_module(f"agents.hub.{module_name}")
        
        for attribute_name in dir(module):
            if attribute_name.endswith("_run"):
                func = getattr(module, attribute_name)
                route_name = attribute_name.replace("_run", "")
                functions.append((func, route_name))

for func, route_name in functions:
    agent_router.get(f"/{route_name}")(func)