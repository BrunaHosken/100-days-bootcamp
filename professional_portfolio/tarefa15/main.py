# Build a custom website using an API that you find interesting.

from flask import Flask, render_template
import requests
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

@app.route('/')
def index():
    # Obter uma receita aleatória da API
    recipe = get_random_recipe()
    return render_template('index.html', recipe=recipe)

def get_random_recipe():
    api_url = 'https://www.themealdb.com/api/json/v1/1/random.php'
    response = requests.get(api_url)
    data = response.json()
    
    if 'meals' in data:
        recipe = data['meals'][0]
        return {
            'name': recipe['strMeal'],
            'category': recipe['strCategory'],
            'instructions': recipe['strInstructions'],
            'image': recipe['strMealThumb'],
        }
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
