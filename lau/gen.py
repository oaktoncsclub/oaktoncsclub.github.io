import os

name = [file[:-4] for file in os.listdir(".") if file.endswith(".wav")]
template = """
        <button onclick="document.getElementById('{0}').play()">
        {0}
                <audio id="{0}">
                        <source src="{0}.wav" type="audio/wav">
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
"""
end = """
</body>
</html>
"""


with open("index.html", "w") as f:
    f.write(start)
    for n in name:
        f.write(template.format(n))
    f.write(end)
