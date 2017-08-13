import json, os

head = """<!DOCTYPE html>
<html>
 <head>
    <meta charset="UTF-8" />
    <title>Members - Oakton Computer Science Club</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.7/css/materialize.min.css" />
  </head>

  <body>
    <h2 style="text-align:center">Club Members</h2>
    <div class="container">
      <div class="row">
    """

template = """
        <div class="col s6 m4">
          <div class="card z-depth-3">
            <div class="card-content activator">
              <span class="card-title activator grey-text text-darken-4"><a href="https://github.com/{0}" target="_new">{1}</a></span>
              <p>{2}</p>
            </div>
          </div>
        </div>
    """

tail = """
      </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.7/js/materialize.min.js"></script>
  </body>
</html>
"""

output = ""

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"members"))
for file in os.listdir():
    try:
        with open(file) as jsonFile:
            info = json.load(jsonFile)
            output += template.format(info["github"],info["name"],info["description"])
    except:
        pass

os.chdir("..")
with open("members.html",'w') as html:
    html.write(head+output+tail)
