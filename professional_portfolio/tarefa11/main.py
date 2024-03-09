from flask import Flask, render_template, request
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_top_colors(image_path, num_colors=10):
    img = Image.open(image_path)
    img_array = np.array(img)
    img_array = img_array.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(img_array)
    
    dominant_colors = kmeans.cluster_centers_.astype(int)

    return [tuple(color) for color in dominant_colors]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' in request.files:
            image_file = request.files['image']

            # Verificar se é um arquivo de imagem válido
            if image_file.filename and allowed_file(image_file.filename):
                try:
                    # Salvar o arquivo temporariamente com um nome seguro
                    filename = secure_filename(image_file.filename)
                    temp_image_path = os.path.join(os.path.dirname(__file__), 'uploads', filename)
                    image_file.save(temp_image_path)

                    # Obter as 10 principais cores
                    dominant_colors = get_top_colors(temp_image_path)
                    print(dominant_colors)

                    # Renderizar a página com as cores usando safe para evitar o erro
                    return render_template('index.html', dominant_colors=dominant_colors, safe=app.jinja_env.filters['safe'])
                finally:
                    # Remover o arquivo temporário
                    if os.path.exists(temp_image_path):
                        os.remove(temp_image_path)
    
    # Renderizar a página inicial
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
