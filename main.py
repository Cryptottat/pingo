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
            html, body {
                margin: 0;
                padding: 0;
                height: 200%; 
                width: 100%;
                overflow-x: hidden; 
            }
            #background1 {
                background: url('/static/background.png') no-repeat center center;
                background-size: cover;
                position: fixed;
                width: 100%;
                height: 50%;
                top: 0;
            }
            #background2 {
                background: url('/static/background2.png') no-repeat center center;
                background-size: cover;
                position: fixed;
                width: 100%;
                height: 50%; 
                top: 50%; 
            }
            .button {
                width: 100px;
                height: 100px;
                background-size: contain;
                background-repeat: no-repeat;
                display: block; /* Make sure anchor tags behave like block elements */
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
        <div id="background1"></div>
        <div id="background2"></div>
        <a href="https://t.me/pingo_portal" target="_blank" class="button" id="button1"></a>
        <a href="https://twitter.com/pingoonsol/media" target="_blank" class="button" id="button2"></a>
        <a href="" target="_blank" class="button" id="button3"></a>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
