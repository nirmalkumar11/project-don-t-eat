import asyncio
from google.adk.runners import InMemoryRunner
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.agents.sequential_agent import SequentialAgent
from dotenv import load_dotenv


load_dotenv()
refiner_agent=Agent(
    
    model='gemini-2.5-flash',
    
    name="refiner",
    
    description="""
                
                you are a food engineer, working at pepcico. 
                you can know about all ingredients.
                you want to help to users to find the exact chemical name.
                
                """,

    instruction="""
                user can give some text. 
                it contains some chemical names and some another names seperated by commas and spaces. 
                you want to find and merge the food ingredients name and give output to users"
                
                output formate: 
                give the ingredient names in a dictionary.
                "food_ingredients_name"= { 
                   "name":<string-finded names>
                }

                you can use google_search tool to verify it is ingredient name or not

                FINAL NOTE: 
                give all ingredient names which exist in the given text.
                do not skip ingredient like water,salt,sugar and many more.
                do not add a foods name like chips, sauce, why because it is final proguct. we want ingredients name which used in the final product.

                """,

    tools=[google_search],
    
    output_key="food_ingredients_name"
)

checker_agent=Agent(
    model='gemini-2.5-flash',

    name='checker',
    
    description="""
                you are a food engineer, working at pepcico . 
                you can know about all ingredients which used in foods for some resons.
                you want to check the ingredients name which is given by refiner agent.
                
                """,

    instruction="""
                you want to check the ingredients name {food_ingredients_name.name}, which is given by refiner agent.
                you can check which is food ingredient or not, if you not sure about it is food ingredient or not you can find food ingredient which possible to stay here.
                you can use the google_search tool to find the possible food ingredient.
                
                output formate:
                give the output in dictionary.
                "final_ingredient_names"= { 
                   "name":<string-verified chemical names>"' 
                }

                """ ,

    tools=[google_search],

    output_key="final_ingredient_names"

)

search_agent = Agent(
    model='gemini-2.5-flash',
    name='search_agent',
    description=(
        "You are a chemical research specialist, working at the LyondellBasell for 10 years. "
        "As a researcher, you can search the web for the side effects of ingredients. "
        "You know about the side effects of all ingredients. "
        "Now you are working at the food inspection department."
    ),
    instruction=(
        "The user can give ingredients of a food product {final_ingredient_names.name}, and you want to find its side effects from the web. "
        "If you find any side effects, you must list them out with proper explanation. "
        "You can add some cases or case studies about its side effects. "
        "You must give the output in the below format:\n"
        '"output_format_for_side_effect":\n'
        '    name of the ingredient:\n'
        '        {\n'
        '            "side_effects":\n'
        '            [\n'
        '                {\n'
        '                    "name": "name of side effect",\n'
        '                    "explanation": "detailed explanation about side effect with timeline of the usage. give website link for more details.'
        '                    (e.g., if used for 1 month you have this side effect, if used for 3 months you have this side effect)",\n'
        '                    "case_study": "case study about side effect, give link of the case study with it"\n'
        '                }\n'
        '            ]\n'
        '        }\n'
        "You can give this output for all ingredients provided by the user. "
        "You can make this output based on the timeline of usage of the product (e.g., daily, weekly, monthly, yearly usage side effects). "
        "If you don't find any side effects, you must say there are no side effects found."
    ),
    tools=[google_search]
)


root_agent = SequentialAgent(

    name='chemical_researcher',
    sub_agents=[refiner_agent,checker_agent,search_agent],
     description='A helpful assistant for user full dill the user request.'  
)

async def researcher(input_text: str):
    runner = InMemoryRunner(root_agent)
    response = await runner.run_debug(input_text)
    print("yes")

def start(query: str):
    asyncio.run(researcher(query))
