from io import StringIO

import hug
import pygments
import pygments.formatters

from . import beautify_file
from .lexer import SuricataLexer


@hug.get('/', output=hug.output_format.html)
def form():
    return '''
        <!doctype html>
        <html>
            <head>
                <title>Suricata Prettifier</title>
                <style type="text/css">
                    .fullwidth {
                        width: 100%;
                    }
                </style>
            </head>
            <body>
                <form method="post" action="/prettify">
                    <input type="submit" value="Prettify" class="fullwidth" />
                    <br>
                    <br>
                    <textarea name="source" placeholder="Paste Suricata rules here..." class="fullwidth" style="height: 500px"></textarea>
                    <br>
                    <br>
                    <input type="submit" value="Prettify" class="fullwidth" />
                </form>
            </body>
        </html>
    '''


@hug.post(output=hug.output_format.html)
def prettify(source):
    lexer = SuricataLexer()
    default_options = dict(
        full=True,
        style='vim',
        prestyles='white-space: pre-wrap;',
    )
    options = {
        **default_options,
    }
    formatter = pygments.formatters.get_formatter_by_name('html', **options)
    source = beautify_file(StringIO(source))
    html = pygments.highlight(source, lexer, formatter)
    return html
