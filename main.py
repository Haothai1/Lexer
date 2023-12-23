import re  # Regular Expressions library

# list of tokens
TOKENS = [
    ('keyword', r'float|double|int|while|if|else|for|return'),  # keywords
    ('Separator', r'[();]'),
    ('Operator', r'[<>=+-/*%]'),
    ('Identifer', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('Real', r'\d+\.\d+')
]

# Create a regular expression pattern to match any token
TOKENS = '|'.join(f'(?P<{token}>{pattern})' for token, pattern in TOKENS)


def lexer(input_string):
  tokens = []  # empty list to hold tokens

  for match in re.finditer(TOKENS,
                           input_string):  # finds all instances of tokens
    token_type = match.lastgroup
    if token_type is not None:
      token_value = match.group(
          token_type)  # extracts the lexeme and appends to the list
      tokens.append((token_type, token_value))
  return tokens


# read the file
def readFile(filePath):
  with open(filePath, 'r') as file:
    test = file.read()
  return test


def main():
  inputFile = 'input_scode.txt'
  outputFile = 'output.txt'
  input_code = readFile(inputFile)
  tokens = lexer(input_code)

  with open(outputFile, 'w') as outFile:  # saves output file
    outFile.write("token\tLexeme\n")
    for token in tokens:
      token_type, token_value = token
      outFile.write(f'{token_type}\t{token_value}\n')


# Run main function
if __name__ == '__main__':
  main()
