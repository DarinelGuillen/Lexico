import re

def check_for_structure(code):
    pattern = re.compile(r'for\s*\(.*;.*;.*\)\s*\{.*\}', re.DOTALL)
    return bool(pattern.match(code))

def check_if_else_structure(code):
    pattern = re.compile(r'if\s*\(.*\)\s*\{.*\}\s*(else\s*\{.*\})?', re.DOTALL)
    return bool(pattern.match(code))

def check_while_structure(code):
    pattern = re.compile(r'while\s*\(.*\)\s*\{.*\}', re.DOTALL)
    return bool(pattern.match(code))

def check_function_structure(code):
    pattern = re.compile(r'def\s+\w+\s*\(.*\)\s*:\s*\n\s+.*', re.DOTALL)
    return bool(pattern.match(code))

def check_class_structure(code):
    pattern = re.compile(r'class\s+\w+\s*\(.*\)\s*:\s*\n\s+.*', re.DOTALL)
    return bool(pattern.match(code))
    