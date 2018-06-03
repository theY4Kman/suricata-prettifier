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
            (r'(\\)(\n)', bygroups(Comment.Preproc, Text)),
            (r'\s+', Text),
            (r'#.*$', Comment.Singleline),
        ],

        'host-port': [
            include('host'),
            (r'\[', Punctuation, 'host-list'),
            include('port'),
        ],
        'host-list': [
            include('host'),
            (r',', Punctuation, ('#pop', 'host-list')),
            (r'\]', Punctuation, '#pop'),
        ],
        'host': [
            (r'!', Operator),
            (words(['any']), Name.Builtin),
            (var, Name.Variable),
            (r'\d+\.\d+\.\d+\.\d+(?:/\d+)?', Literal),
        ],
        'port': [
            include('whitespace'),
            (words(['any']), Name.Builtin),
            (r'\d+', Number.Integer),
        ],

        'value': [
            include('whitespace'),
            (r'"', String.Delimiter, 'string'),
            (r'\\;', String.Escape),
            (r'[^;"]*', String.Char, '#pop'),
        ],
        'string': [
            ('\\\\"', String.Escape, ('#pop', 'string')),
            ('[^"]+', String.Char),
            ('"', String.Delimiter, '#pop:2'),
        ],

        'root': [
            include('whitespace'),
            (words(['pass', 'drop', 'reject', 'alert']), Keyword.Type, 'signature'),
        ],

        'signature': [
            include('whitespace'),
            (words(['tcp', 'udp', 'icmp', 'ip', 'http', 'ftp', 'tls', 'smb', 'dns']), Keyword.Reserved, 'source'),
            default('#pop'),
        ],
        'source': [
            include('whitespace'),
            include('host-port'),
            include('whitespace'),
            (words(['<>', '->']), Operator, ('#pop', 'dest')),
            default('#pop'),
        ],
        'dest': [
            include('whitespace'),
            include('host-port'),
            ('\(', Punctuation, ('#pop', 'opts')),
        ],
        'opts': [
            include('whitespace'),
            (r'\)', Punctuation, '#pop'),
            (prop, Name.Property),
            (':', Punctuation, 'value'),
            (';', Punctuation, ('#pop', 'opts')),
        ]
    }
