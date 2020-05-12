
app=Flask(__name__)
@app.route('/')
def Hola():
    return 'Hola Mundo Flask es facil'
@app.route ('/prueba')
def prueba():
    return "Estoy en prueba"

@app.route('/insertar/<string:nombre>')
def insertar(nombre):
    return 'Tu quieres insertar a %s en la BD'%nombre


if __name__  == "__main__" :
    app.run(host='0.0.0.0',debug=True,port=5000)
   
   