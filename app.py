from flask import Flask, render_template, request
from few_shot import FewShotPost
from post_gen import generate_post

app = Flask(__name__)

# Initialize your FewShotPost instance
fs = FewShotPost('data/processed_posts.json')
fs.load_posts()  # load the data

length_options = ['Short', 'Medium', 'Long']
language_options = ['English', 'Hinglish']

@app.route('/', methods=['GET', 'POST'])
def index():
    post = None
    if request.method == 'POST':
        selected_tag = request.form.get('title')
        selected_length = request.form.get('length')
        selected_language = request.form.get('language')
        post = generate_post(selected_tag, selected_length, selected_language)

    return render_template(
        'index.html',
        tags=fs.get_tags(),
        lengths=length_options,
        languages=language_options,
        post=post
    )

if __name__ == '__main__':
    app.run(debug=True)
