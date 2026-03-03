from PyPDF2 import PdfWriter
from flask import Flask, request, render_template,send_file

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/merge", methods=["POST"])
def merge():
    merger = PdfWriter()
    files = request.files.getlist("pdfs")

    for file in files:
        file.save(file.filename)
        merger.append(file.filename)

    merger.write("merged-pdf.pdf")
    merger.close()

    return send_file("merged-pdf.pdf", as_attachment=True)

app.run(debug=True)