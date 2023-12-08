from flask import Flask, request, jsonify
from cedol.cedol import getCedol
from cer.cer import getCER

app = Flask(__name__)

# Aquí puedes configurar tu conexión a la base de datos


@app.route('/')
def index():
    return "Servidor funcionando"

# Aquí puedes agregar más rutas para manejar diferentes peticiones


@app.route('/cedol/<month>/<year>', methods=['GET'])
def get_cedol(month, year):
    mes = str(month)
    año = str(year)
    valor = getCedol(mes, año)
    print("valor: ", valor)

    # Aquí puedes obtener datos de la base de datos o realizar alguna operación
    return str(valor)


@app.route('/cer/<year>/<month>/<day>', methods=['GET'])
def get_cer(month, year, day):
    mes = str(month)
    año = str(year)
    day = str(day)
    date = f'${mes}-${año}-${day}'
    valor = getCER(date)
    print("valor: ", valor)

    # Aquí puedes obtener datos de la base de datos o realizar alguna operación
    return str(valor)


if __name__ == '__main__':
    app.run(debug=True)
