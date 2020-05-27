import flask

from flask import Flask, request, render_template

from script import gerar_img

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("index.html", token='token')
    
    # errors = ""
    # if request.method == "POST":
    #     url = None
    #     try:
    #         url = str(request.form["url"])
    #     except:
    #         errors += "<p>{!r} não é uma URL.</p>\n".format(request.form["url"])
       
    #     if url is not None:
    #         result = gerar_img(url)
    #         return '''
    #             <html>
    #                 <body>
    #                     <p>The result is {result}</p>
    #                     <p><a href="/">Click aqui para gerar outra imagem</a>
    #                 </body>
    #             </html>
    #         '''.format(result=result)

    # return '''
    #     <html>
    #         <body>
    #             {errors}
    #             <p>Inserir a URL da imagem:</p>
    #             <form method="post" action=".">
    #                 <p><input name="url" /></p>
    #                 <p><input type="submit" value="Gerar filtro!" /></p>
    #             </form>
    #         </body>
    #     </html>
    # '''.format(errors=errors)


if __name__ == "__main__":
    app.run(debug=True)