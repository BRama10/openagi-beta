from pydantic import BaseModel


class AgentBody:
    payload: str | dict | float