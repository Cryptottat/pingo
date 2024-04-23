from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pingo</title>
        <style>
            body, html {
                margin: 0;
                padding: 0;
                height: auto; /* Allow vertical scrolling */
                width: 100%; /* Full width */
                overflow-x: hidden; /* Hide horizontal scrollbar */
            }
            .background {
                width: 100%; /* Each background takes full width */
                height: auto; /* Height is auto to maintain aspect ratio */
                background-size: 100% auto; /* Adjust width and maintain aspect ratio */
                background-repeat: no-repeat; /* Do not repeat the image */
            }
            #background1 {
                background-image: url('/static/background.png');
            }
            #background2 {
                background-image: url('/static/background2.png');
            }
            .button {
                width: 100px;
                height: 100px;
                background-size: contain;
                background-repeat: no-repeat;
                position: absolute;
                top: 10px;
            }
            #button1 {
                left: 10px;
                background-image: url('/static/tele.png');
            }
            #button2 {
                left: 120px;
                background-image: url('/static/twt.png');
            }
            #button3 {
                left: 230px;
                background-image: url('/static/pump.png');
            }
        </style>
    </head>
    <body>
        <div id="background1" class="background"></div>
        <div id="background2" class="background"></div>
        <a href="https://t.me/pingo_portal" target="_blank" class="button" id="button1"></a>
        <a href="https://twitter.com/pingoonsol/media" target="_blank" class="button" id="button2"></a>
        <a href="" target="_blank" class="button" id="button3"></a>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)