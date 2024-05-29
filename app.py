from flask import Flask
app = Flask(__name__)

@app.route('/')
def training():
    # Define the header and paragraph text
    header = "Training 22"
    paragraph = "Hi, my name is Jamie"

    # Construct the HTML output
    html_output = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple HTML Output</title>
    </head>
    <body>
        <h1>{header}</h1>
        <p>{paragraph}</p>
    </body>
    </html>
    """
    
    return html_output

if __name__ == '__main__':
    app.run(debug=True)
