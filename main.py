import subprocess
import sanic
import os
import platform
import aiofiles
import json

app = sanic.Sanic(name="clip2http")

print("Clip2Http")

SETTING = json.load(open("setting.json", "r"))

@app.post("/post")
async def post(request: sanic.Request):
    content = request.json["content"]
    async with aiofiles.open("tmp", "w") as f:
        await f.write(content)
    if platform.system() == "Windows":
        proc = subprocess.Popen(f'clip < tmp', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = proc.communicate()
        os.remove("tmp")
        return sanic.response.json({"stdout": result[0], "stderr": result[1]})
    elif platform.system() == "Linux":
        proc = subprocess.Popen(f'xclip -selection clipboard < tmp', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = proc.communicate()
        os.remove("tmp")
        return sanic.response.json({"stdout": result[0], "stderr": result[1]})
    else:
        return sanic.response.json({"stdout": "", "stderr": "Unsupported platform"})

@app.get("/get")
async def post(request: sanic.Request):
    if platform.system() == "Windows":
        proc = subprocess.Popen(f'powershell -command "get-clipboard"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = proc.communicate()
        return sanic.response.text(result[0])
    elif platform.system() == "Linux":
        proc = subprocess.Popen(f'xclip -selection clipboard -o', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = proc.communicate()
        return sanic.response.text(result[0])

app.run(host=SETTING["host"], port=SETTING["port"])
