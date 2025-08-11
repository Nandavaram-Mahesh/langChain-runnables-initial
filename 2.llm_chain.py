from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the LLM
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Create a Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# Chain
chain = LLMChain(llm=llm, prompt=prompt)

# Define the input
topic = input("Enter a topic: ")

# Run the chain
blog_title = chain.run(topic)

# Print the output
print("Generated Blog Title:", blog_title)