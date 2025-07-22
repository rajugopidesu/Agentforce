import os
from agent_sdk import Agentforce, AgentUtils
from agent_sdk.models.agent import Agent
from agent_sdk.models.topic import Topic
from agent_sdk.models.action import Action
from agent_sdk.models.input import Input
from agent_sdk.models.output import Output
from agent_sdk.models.system_message import SystemMessage
from agent_sdk.models.variable import Variable
from agent_sdk.core.auth import BasicAuth

# Replace with your Salesforce credentials
username = "rajugopidesu343@agentforce.com"
password = "Ganga@73969405918rfUvYKF3DkBlvT3MphTofv07"

auth = BasicAuth(username=username, password=password)

# Initialize the AgentForce client
agentforce = Agentforce(auth=auth)

# Define the action
action = Action(
    name="findOrder action agentforce",
    description="Find order details using an order ID",
    inputs=[
        Input(
            name="orderID",
            description="Order identification number",
            data_type="Text",
        )
    ],
    outputs=[
        Output(
            name="orderDetails", description="Details of the order", data_type="Object"
        )
    ],
)

# Define the topic
topic = Topic(
    name="Order Management Topic Agentforce",
    description="Handles all user requests related to finding and managing orders",
    scope="public",
    instructions=[
        "If a user cannot find their order, attempt to locate it using the order ID",
        "If a user wants to check the status of their order, retrieve the order details",
    ],
    actions=[action],
)

# Define the agent
agent = Agent(
    name="SDK Agentforce Agent",
    description="An agent created programmatically for order management",
    agent_type="External",
    agent_template_type="EinsteinServiceAgent",
    company_name="Example Corp",
    sample_utterances=["What's the status of my order?", "I need to find my order"],
    system_messages=[
        SystemMessage(message="Welcome to Order Management!", msg_type="welcome"),
        SystemMessage(message="I'm sorry, I encountered an error.", msg_type="error"),
    ],
    variables=[
        Variable(
            name="apiKey",
            data_type="Text",
            var_type="conversation",
            visibility="Internal",
            developer_name="apiKey",
            label="API Key"
        )
    ],
    topics=[topic],
)

# View the agent configuration
print(f"Agent Name: {agent.name}")
print(f"Description: {agent.description}")
print(f"Topics: {len(agent.topics)}")

# Deploy the agent
result = agentforce.create(agent)
print(f"Agent created successfully")
