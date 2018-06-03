import click
import pygments
import pygments.formatters

from suricata_prettifier.beautify import beautify_file
from suricata_prettifier.lexer import SuricataLexer


@click.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.option('-f', '--formatter', default='terminal')
@click.argument('input', type=click.File('r'), default='-')
@click.argument('output', type=click.File('w'), default='-')
@click.argument('formatter_options', nargs=-1, type=click.UNPROCESSED)
def prettify(input, output, formatter, formatter_options=()):
    lexer = SuricataLexer()
    default_options = dict(
        full=True,
        style='vim',
        prestyles='white-space: pre-wrap;',
    )
    options = {
        **default_options,
        **dict(option.split('=', 1) for option in formatter_options),
    }
    formatter = pygments.formatters.get_formatter_by_name(formatter, **dict(options))
    source = beautify_file(input)
    pygments.highlight(source, lexer, formatter, output)


if __name__ == '__main__':
    prettify()
