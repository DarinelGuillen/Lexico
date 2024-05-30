import re

def check_for_structure(code):
    pattern = re.compile(r'for\s*\(.*;.*;.*\)\s*\{.*\}', re.DOTALL)
    return bool(pattern.match(code))

def check_if_else_structure(code):
    pattern = re.compile(r'if\s*\(.*\)\s*\{.*\}\s*(else\s*\{.*\})?', re.DOTALL)
    return bool(pattern.match(code))
