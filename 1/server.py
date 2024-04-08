from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/reg/<string:emile>")
def forReg(emile):
        if not os.path.exists(f"C:/muhammed_kurs/servers/1/datas/client/{emile}"):
                os.makedirs(f"C:/muhammed_kurs/servers/1/datas/client/{emile}")
                return "Succes"
        else:
                return f"Emile {emile} существует"

@app.route('/<string:emile>')
def forConnect(emile):
    #url = request.url

    #if 'favicon.ico' in url:
    #    return 'Иконка favicon не найдена'
    if not os.path.exists(f"C:/muhammed_kurs/servers/1/datas/client/{emile}"):
    	return(f'Эл. почта {emile} не существует')
    else:
    	print(f'Connected for {emile}')

    puth = os.listdir("C:/muhammed_kurs/servers/1/datas/client/"+emile)#url[21:])
    return f'Пользователь запросили: {str(puth)}'


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
