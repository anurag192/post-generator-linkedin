import json
import pandas as pd


class FewShotPost:
    def __init__(self,processed_file_path):
        self.df=None
        self.tags=None
        self.file_path=processed_file_path
        self.unique_tags=None
        self.load_posts()


    def load_posts(self):
        with open(self.file_path,encoding='utf-8') as f:
            posts=json.load(f)
            self.df=pd.json_normalize(posts)

            self.df['line count']=self.df['line count'].apply(self.categorize_line_count)
            all_tags=self.df['tags'].apply(lambda x:x).sum()
            self.unique_tags=list(set(all_tags))
            
           


    def categorize_line_count(self,line_count):
        if line_count<5:
            return "Short"
        
        elif 5<=line_count<=10:
            return "Medium"
        
        else:
            return "Long"
        
    def get_tags(self):
        return self.unique_tags
        
    
    
    def get_filtered_posts(self,language,line_count,tag):

        response=self.df[(self.df['language']==language) & 
                         (self.df['line count']==line_count) 
                         & (self.df['tags'].apply(lambda tags:tag in tags))]
        
        return response.to_dict(orient='records')
    




           


if __name__=="__main__":
    fewshot=FewShotPost('data/processed_posts.json')
    fewshot.load_posts()
    unique_tags=fewshot.get_tags()
    print(unique_tags)
    post=fewshot.get_filtered_posts('English','Short','LinkedIn')
    print(post)




        