import os
import django
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

settings.configure(TEMPLATES=[
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["."]
    }
])
django.setup()

template = get_template("template.html")
names = [file[:-4] for file in os.listdir(".") if file.endswith(".wav")]
rendered = template.render({"names": names})

with open("index.html", "w") as f:
    f.write(rendered)
