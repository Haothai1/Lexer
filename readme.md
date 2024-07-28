# Lexical analyzer
Lexical analyzer in Python

### Development
You will need Python 3+ to run this program.

To run the program, type the following command

```` 
python3 main.py
````

1. Put your statement in the `inputs_scode.txt` file. (Note that `inputs_scode.txt` must be in same directory as `lexer.py` in order for the program to execute.)
2. Open your terminal and make sure python is installed. Then type `python main.py` to run the program.

3. After running the program a `output.txt` will be created showing all of the tokens and lexemes provided from `inputs_scode.txt`. 

Example input and output files:
`inputs_scode.txt`:
````
x/y = a + b * c;
if (x == y) a = b - 5:
      a % b
    print ("yes")  
while (t < upper) s = 22.00;

float
````
`output.txt`:
````
token	Lexeme
Identifer	x
Operator	/
Identifer	y
Operator	=
Identifer	a
Operator	+
Identifer	b
Operator	*
Identifer	c
Separator	;
keyword	if
Separator	(
Identifer	x
Operator	=
Operator	=
Identifer	y
Separator	)
Identifer	a
Operator	=
Identifer	b
Operator	-
Identifer	a
Operator	%
Identifer	b
Identifer	print
Separator	(
Identifer	yes
Separator	)
keyword	while
Separator	(
Identifer	t
Operator	<
Identifer	upper
Separator	)
Identifer	s
Operator	=
Real	22.00
Separator	;
keyword	float

````

#### Description

This program is a lexer which converts source text from `inputs_scode.txt` and processes it into a sequence of 
tokens and lexemes in `output.txt`. 

In order to run other test cases modify `inputs_scode.txt` and rerun the program respectively. 
