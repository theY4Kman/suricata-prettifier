import idstools.rule


def beautify_file(fp):
    rules = idstools.rule.parse_fileobj(fp)
    formatted = [format_parsed_rule(rule) for rule in rules]
    return '\n'.join(formatted)


def format_parsed_rule(rule):
    if rule['options']:
        options = ['  {prop} \\'.format(prop=format_parsed_option(option))
                   for option in rule['options']]
        options_str = '\n'.join(options)
        return '{header} ( \\\n{options_str}\n)'.format(**rule, options_str=options_str)
    else:
        return '{header} ()'.format(**rule)


def format_parsed_option(option):
    if option['value'] is None:
        return '{name};'.format(**option)
    else:
        return '{name}: {value};'.format(**option)
