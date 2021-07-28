from datetime import datetime

from flask import Flask, jsonify, request

from dao.confronto import ConfrontoDAO

app = Flask(__name__)


@app.route("/")
def teste():
    return "Teste"


@app.route("/cadastra-lutador/", methods=['POST'])
def cadastra_lutador(request):
    pass


@app.route("/cadastra-confronto/", methods=['POST'])
def cadastra_confronto(request):
    pass


@app.route("/cadastra-empresa/", methods=['POST'])
def cadastra_empresa(request):
    pass


@app.route("/lutas-hoje/")
def lutas_hoje():
    data_str = datetime.today().strftime("%d-%m-%Y")
    dao = ConfrontoDAO()
    luta_hoje = dao.busca_confronto_por_data(data=data_str)
    
    return jsonify({
        'local': luta_hoje.estadio
        # ...
    })


# This is no needed once you run the project via "flask run"
# see the README.md to instructions.
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True, load_dotenv=True)
