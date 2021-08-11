import os
from datetime import date

from google.cloud.dialogflowcx_v3.services.agents.client import AgentsClient
from google.cloud.dialogflowcx_v3.types.agent import DeleteAgentRequest

import pytest

from create_agent import create_agent

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
pytest.AGENT_PATH = ""


def delete_agent(name):
    agents_client = AgentsClient()
    request = DeleteAgentRequest(name=name)
    agents_client.delete_agent(request=request)


def test_create_agent():
    today = date.today()
    agentName = "tempAgent." + today.strftime("%d.%m.%Y")
    response = create_agent(PROJECT_ID, agentName)
    pytest.AGENT_PATH = response.name

    assert response.display_name == agentName

    delete_agent(pytest.AGENT_PATH)
