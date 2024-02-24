from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

##Defining the config list
##So basically config list consists of the API KEY and the Large Langauge model you are using, typially in a 'json' format.

##Importing the Config lis file from json

config_list = config_list_from_json(env_or_file = "OAI_CONFIG_LIST")

##Now we will create or define our Agents.
## USerProxyAgent = Proxy for the User and does the User's work.
## AssistentAgent = Agent that does the work that we ask it to do.


user_proxy_agent = UserProxyAgent(
    name = "user_proxy_agent",
    code_execution_config = {"work_dir": "coding"}
)

assistant_agent = AssistantAgent(
    name = "assistant_agent",
    llm_config = {"config_list": config_list}
)


##Initiate the workflow or the char between the Agents
user_proxy_agent.initiate_chat(assistant_agent, message = "Plot a chart of comparing the amount of males and females on Earth.")