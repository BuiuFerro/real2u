from flask import Flask, request, render_template

from script import gerar_img

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
     errors = ""
     if request.method == "POST":
        url = None
        try:
            url = str(request.form["url"])
        except:
            errors += "<p>{!r} não é uma URL.</p>\n".format(request.form["url"])
       
        if url is not None:
            result = gerar_img(url)

     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)