# will use api.tl and saved.json and template.md to generate a folder called tl that contains all the generated docs
# run this file after you run scrape_data.py
import json
import os
from io import StringIO
from pathlib import Path

from markdownify import markdownify

from gen_exmp import generate_example
from tlarg import TLArg
from tlobject import TLObject
from tlparser import parse_tl, find_layer
import shutil

api_file = Path("api.tl")
scrapped_file = json.loads(Path("saved.json").open().read())
with open("saved.json", "r", encoding="utf-8") as out:
    methods = json.loads(out.read())
with open("template.md", "r", encoding="utf-8") as out:
    template = out.read()

if os.path.exists("tl"):
    shutil.rmtree("tl")
os.makedirs("tl", exist_ok=True)


def to_camel_case(snake_str):
    if snake_str[0].isupper():
        return snake_str
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def to_table(row):
    a = ""
    for x in row:
        x = list(x.values())
        first = markdownify(to_camel_case(x[0])).replace('|', '').replace("\n", '<br>')
        second = markdownify(x[1]).replace('|', '').replace("\n", '<br>')
        third = markdownify(x[2]).replace('|', '').replace("\n", '<br>')
        a += f"|{first}|{second}|{third}\n"
    return a


def to_related(related):
    a = ""
    for x in related:

        temp = f"<p><a href='https://core.telegram.org{x['page_link']}'>{x['page_name']}</a></p>"
        if x["description"]:
            temp += f"<p>{x['description']}</p>"
        temp = markdownify(temp)
        a += f"#### {temp}"
    return a


parsed = parse_tl(api_file, find_layer(api_file))
for method in parsed:
    method: TLObject
    path = "tl/"
    if method.namespace:
        path = path + method.namespace + "/"
        os.makedirs(path, exist_ok=True)

    # we only want to write functions for now
    description = "No description found"
    params = []
    errors = []
    related_pages = []
    can_bots_use = "No"
    main_result = ""
    if method.is_function:
        # try to find description
        for function in scrapped_file:
            if method.name.lower() in function["title"].lower():
                description = function["description"]
                params = function["params"]
                main_result = function["result"]
                errors = function["errors"]
                can_bots_use = function["can_bot_use"].title()
                related_pages = function["related_pages"]
                break
        # we now populate the template.md
        if not params:
            for x in method.args:
                x: TLArg
                if not x.type:
                    continue
                params.append({"name": x.name, "type": x.type, "description": "No description found"})
        b = StringIO()
        method.as_example(b)
        result = method.result
        if result == "X":
            result = "AnyRequest"
        title: str = method.class_name
        if method.namespace:
            title = f"{method.namespace}.{title}"

        data = template.format(title=title,
                               description=markdownify(description),
                               params=to_table(params),
                               result=markdownify(main_result or result),
                               errors=to_table(errors),
                               bots=can_bots_use,
                               related=markdownify(to_related(related_pages)),
                               examples=generate_example(b.getvalue(), result)
                               )
        with open(os.path.join(path, f"{method.class_name}.md"), "w", encoding="utf-8") as out:
            out.write(data)
