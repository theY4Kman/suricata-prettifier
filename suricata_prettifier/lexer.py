from pygments.lexer import RegexLexer, default, include, words, bygroups
from pygments.token import *


__all__ = ['SuricataLexer']


class SuricataLexer(RegexLexer):
    name = 'Suricata'
    aliases = ['suricata']
    filenames = ['*.rules']

    prop = r'[a-zA-Z_][a-zA-Z0-9_]*'
    var = r'\$' + prop

    tokens = {
        'whitespace': [
            (r'(\s*)(\\)(\n)', bygroups(Text, Comment.Preproc, Text)),
            (r'\s+', Text),
            (r'#.*$', Comment.Singleline),
        ],

        'root': [
            include('whitespace'),
            (words(['pass', 'drop', 'reject', 'alert']), Keyword.Type, 'protocol'),
        ],

        'protocol': [
            include('whitespace'),
            (words(['tcp', 'udp', 'icmp', 'ip', 'http', 'ftp', 'tls', 'smb', 'dns', 'smtp']), Keyword.Reserved, (
                '#pop',

                'source',
                'port-expr',
                'host-expr',
            )),
        ],
        'source': [
            include('whitespace'),
            (words(['<>', '->']), Operator, (
                '#pop',

                'dest',
                'port-expr',
                'host-expr',
            )),
        ],
        'dest': [
            include('whitespace'),
            ('\(', Punctuation, (
                '#pop',
                'opts',
            )),
        ],
        'opts': [
            include('whitespace'),
            (r'\)', Punctuation, '#pop'),
            default('opt'),
        ],

        'opt': [
            include('whitespace'),
            (prop, Name.Property, 'opt'),
            (':', Punctuation, ('value', 'negatable')),
            (';', Punctuation, '#pop'),
            default('#pop'),
        ],
        'value': [
            include('whitespace'),
            (r'(")(/)((?:[^/]|\\/)+)(/)(\w*)(")',
                bygroups(String.Delimiter, Punctuation, String.Regex, Punctuation, String.Regex, String.Delimiter),
                '#pop'),
            (r'"', String.Delimiter, 'string'),
            (r'\\;', String.Escape),
            (r'[^;"]*', String.Char, '#pop'),
        ],
        'string': [
            ('\\\\"', String.Escape, ('#pop', 'string')),
            ('[^"]+', String.Char),
            ('"', String.Delimiter, '#pop:2'),
        ],

        'negatable': [
            include('whitespace'),
            (r'!', Operator),
            include('whitespace'),
            default('#pop'),
        ],

        'host-expr': [
            include('whitespace'),
            (words(['any']), Name.Builtin, '#pop'),
            (r'!', Operator),
            (r'\[', Punctuation, ('#pop', 'host-list', 'host', 'negatable')),
            default(('#pop', 'host')),
        ],
        'host': [
            (var, Name.Variable, '#pop'),
            (r'\d+\.\d+\.\d+\.\d+(?:/\d+)?', Literal, '#pop'),
        ],
        'host-list': [
            (r'\]', Punctuation, '#pop'),
            (r',', Punctuation, ('host', 'negatable')),
        ],

        'port-expr': [
            include('whitespace'),
            (words(['any']), Name.Builtin, '#pop'),
            (r'!', Operator),
            (r'\[', Punctuation, ('#pop', 'port-list', 'port', 'negatable')),
            default(('#pop', 'port')),
        ],
        'port': [
            (var, Name.Variable, '#pop'),
            (r'(\d+)([:-])(\d+)', bygroups(Number.Integer, Punctuation, Number.Integer), '#pop'),
            (r'\d+', Number.Integer, '#pop'),
        ],
        'port-list': [
            (r'\]', Punctuation, '#pop'),
            (r',', Punctuation, ('port', 'negatable')),
        ],
    }
