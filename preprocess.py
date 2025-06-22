import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv
load_dotenv()
import os

from langchain_groq import ChatGroq

llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model="llama-3.3-70b-versatile")



def process_posts(raw_file_path,processed_file_path):

    enriched_posts=[]
    with open(raw_file_path,encoding='utf-8') as file:
        posts=json.load(file)
        
        for post in posts:
          
            metadata=extract_metadata(post['text']) 
            post_with_metadata=post | metadata
        
            enriched_posts.append(post_with_metadata)

    unified_tags=get_unified_tags(enriched_posts)
    

    for post in enriched_posts:
        current_tags=post['tags']
        print(current_tags)

        new_tags={unified_tags[tag] for tag in current_tags}
      

        post['tags']=list(new_tags)

    with open(processed_file_path,'w',encoding='utf-8') as outfile:
        json.dump(enriched_posts,outfile,indent=4)



   
            

def extract_metadata(post):
    template='''
        You are given a linkedin post. You need to extract number of lines, language of the post and tags
        1. Return a valid JSON. No preamble.
        2. JSON object should have exactly three keys : line count,language and tags.
        3. tags is an array of text tags. Except maximum two tags.
        4. Language should be English or Hinglish (Hinglish means hindi+english)

        Here is the actual on which you need to perform the task :
        {post}
     '''
    
    pt=PromptTemplate.from_template(template)
    parser=JsonOutputParser()
    chain=pt|llm|parser

    response=chain.invoke(input={'post':post})
    return response

def get_unified_tags(post_with_metadata):
    unique_tags=set()
    for post in post_with_metadata:
        unique_tags.update(post['tags'])

    unique_tag_list=','.join([tag for tag in unique_tags])

    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list. 
       Example 1: "Jobseekers", "Job Hunting" can be all merged into a single tag "Job Search". 
       Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
       Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
       Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
    2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
    3. Output should be a JSON object, No preamble
    3. Output should have mapping of original tag and the unified tag. 
       For example: {{"Jobseekers": "Job Search",  "Job Hunting": "Job Search", "Motivation": "Motivation}}
    
    Here is the list of tags: 
    {tags}
    '''
    pt=PromptTemplate.from_template(template)
    parser=JsonOutputParser()

    chain=pt|llm|parser
    response=chain.invoke({'tags':unique_tag_list})
    return response








if __name__=="__main__":
    process_posts("data/raw_posts.json","data/processed_posts.json")
