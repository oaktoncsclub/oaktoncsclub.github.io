import os
from urllib.parse import quote

name = [file[:-4] for file in os.listdir(".") if file.endswith(".wav")]
template = """
    <button onclick="document.getElementById('{1}').play()">
        {0}
        <audio id="{1}">
            <source src="{2}.wav" type="audio/wav">
        </audio>
    </button>
"""

start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Lau Board</title>
</head>
<body>
<h1>Welcome to Lau Board!</h1>
"""
end = """
</body>
</html>
"""


with open("index.html", "w") as f:
    f.write(start)
    for (i, n) in enumerate(name):
        f.write(template.format(n, i, quote(n)))
    f.write(end)
