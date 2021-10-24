from base64 import b64decode

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pyflowchart import Flowchart
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def generate_flowchart_data(filename: str):
    with open(filename) as f:
        code = f.read()

    fc = Flowchart.from_code(code)

    return fc.flowchart()


app = FastAPI()

app.mount("/www", StaticFiles(directory="public", html=True))

@app.get("/program")
def index():
    data = generate_flowchart_data('main.py')

    return {"data": data}


class Body(BaseModel):
    svg: str


@app.post("/svg")
def index(body: Body):
    svg = str(b64decode(body.svg))[2:-1]

    with open('output.svg', 'w') as f:
        f.write(svg)

    drawing = svg2rlg("output.svg")
    renderPM.drawToFile(drawing, "output.png", fmt="PNG")

    return {"ok": True}
