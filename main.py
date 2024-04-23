from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# static 폴더를 'static' 경로로 마운트
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image and Button Page</title>
        <style>
            body, html {
                margin: 0;
                padding: 0;
                height: 100%;
                background: url('/static/background.png') no-repeat center center fixed;
                background-size: cover;
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
    <a href="https://t.me/pingo_portal" target="_blank" class="button" id="button1"></a>
    <a href="https://twitter.com/pingoonsol/media" target="_blank" class="button" id="button2"></a>
    <a href="https://example.com/link3" target="_blank" class="button" id="button3"></a>
</body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)