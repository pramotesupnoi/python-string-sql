# Python string SQL

Syntax highlighting for SQL inside Python strings.

## Installation

As the extension is in development, installation is only
possible manually.

Install [node.js](https://nodejs.org/) and then then install the
[vsce](https://www.npmjs.com/package/vsce) package:

```
npm install --global vsce
```

Clone the repository and open a terminal at the project root
and execute the following command:

```
vsce package
```

The resulting `.vsix` file can be installed via the VSCode GUI.

## Usage

SQL statements inside a single line of python code work as expected.
Multiline SQL statements require an SQL comment `-- SQL`
or `/* SQL */` as the same line as the opening triple quotes.
The comment `-- PGSQL` (or `/* PGSQL */`) will use
the postgres grammer definitions from [pgEidt](https://github.com/desoi/pgedit-textmate).


## Acknowledgements

The project was adpated from [es6-string-html](https://github.com/hanjingboo/es6-string-html).

This project reuses the textmate grammar file
from [pgEdit](https://pgedit.com/) which is distributed
under a separate license. See the license file in
`./syntaxes/pgedit/LICENSE`.
