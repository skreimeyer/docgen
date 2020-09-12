import sys
from datetime import datetime
from jinja2.loaders import FileSystemLoader
from jinja2.utils import select_autoescape
from typing import Dict, Any, List
from pdb import set_trace

import toml
from jinja2 import Environment

def usage():
    print("""python render.py FILENAME""")
    quit()

def content_or_blank(local_config:Dict[str,Any],keys:List[str]) -> str:
    """Keys must be passed in list format"""
    search_key = keys.pop()
    result = local_config.get(search_key)
    if result and keys:
        set_trace()
        return content_or_blank(result,keys)
    if result:
        return f"<div class='underlined'>{result}</div>"
    else:
        set_trace()
        return "<div class='blank-line'></div>"       

if __name__ == "__main__":
    if len(sys.argv) < 1:
        usage()
    with open(sys.argv[1],'r') as config_file:
        config = toml.load(config_file)
        config['today'] = datetime.now().strftime("%B %d, %Y")
    env = Environment(loader=FileSystemLoader('templates'))
    env.filters['content_or_blank'] = content_or_blank
    template = env.get_template('SWPPP_template.html')
    with open('check.html','w') as out_file:
        out_file.write(template.render(config))