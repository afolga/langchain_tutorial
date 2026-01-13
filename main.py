from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import os
load_dotenv()
def main():
    print("Hello from langchain-course!")
    information="""     
Francis Scott Key Fitzgerald (September 24, 1896 – December 21, 1940), widely known as F. Scott Fitzgerald or simply Scott Fitzgerald,[1] was an American novelist, essayist, and short story writer. He is best known for his novels depicting the flamboyance and excess of the Jazz Age, a term that he popularized in his short story collection Tales of the Jazz Age. He published four novels, four story collections, and 164 short stories. He achieved transient success and fortune in the 1920s, but did not receive critical acclaim until after his death.
 He is now widely regarded as one of the greatest American writers of the 20th century."""
    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-5") #temp controls randomness
    chain = summary_prompt_template | llm ##prompt template and LLM

    response = chain.invoke(input={"information": information}) 
    print(response.content) ## AI Message Object
if __name__ == "__main__":
    main()
