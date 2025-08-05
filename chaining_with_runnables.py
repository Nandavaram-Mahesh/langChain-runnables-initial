import random
from abc import ABC, abstractmethod
class Runnable(ABC):

    @abstractmethod
    def invoke(self, input_data):
        pass

class DummyLLM(Runnable):

  def __init__(self):
    print('LLM created')
# New Method - Standardized Version
  def invoke(self, prompt):
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}

# Old Method - Not Standardized
  def predict(self, prompt):

    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}

class DummyPromptTemplate(Runnable):

  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables
# New Method - Standardized Version
  def invoke(self, input_dict):
    return self.template.format(**input_dict)
# Old Method - Not Standardized
  def format(self, input_dict):
    return self.template.format(**input_dict)

class DummyStrOutputParser(Runnable):

  def __init__(self):
    pass

  def invoke(self, input_data):
    return input_data['response']

class RunnableConnector(Runnable):

  def __init__(self, runnable_list):
    self.runnable_list = runnable_list

  def invoke(self, input_data):
    # Here we are looping thorugh each of the runnables and invoking them 
    # and passing the input data of previous runnable to the next runnable
    for runnable in self.runnable_list:
      input_data = runnable.invoke(input_data)

    return input_data

template = DummyPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

llm = DummyLLM()

parser = DummyStrOutputParser()

chain = RunnableConnector([template, llm, parser])

chain.invoke({'length':'long', 'topic':'india'})



template1 = DummyPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2 = DummyPromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)


llm = DummyLLM()

parser = DummyStrOutputParser()

chain1 = RunnableConnector([template1, llm])
chain2 = RunnableConnector([template2, llm, parser])

final_chain = RunnableConnector([chain1, chain2])

response=final_chain.invoke({'topic':'india'})

print(response)