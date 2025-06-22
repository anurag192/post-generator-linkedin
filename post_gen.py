from llm_helper import llm
from few_shot import FewShotPost

few_shot=FewShotPost('data/processed_posts.json')


def get_line_count(length):

    if length=='Short':
        return "1 to 5 lines"
    
    elif length=='Medium':
        return "5 to 10 lines"
    
    else:
        return "10 to 15 lines"
    

def get_prompt(tag,length,language):

    length_str=get_line_count(length)
    prompt=f''' 
    Generate a linkedin post using the following information. No preamble.

    1) Topic:{tag}
    2) Length:{length_str}

    3) Language:{language}

    If the Language is Hinglish, means it is a mix of Hindi and English.
    The script for the genearted post should always be in English.

    '''

    examples=few_shot.get_filtered_posts(language,length,tag)

    if len (examples) >0:

        prompt+="4) Use the writing style as per the following example"
        for i,post in enumerate(examples):
            post_text=post['text']
            prompt+=f"\n\n Example{i+1}: \n\n {post_text}"

            if i==1:
                break


    return prompt

    

def generate_post(tag,length,language):
    prompt=get_prompt(tag,length,language)
    response=llm.invoke(prompt)

    return response.content





if __name__=="__main__":
    post=generate_post('LinkedIn','Short','English')
    print(post)