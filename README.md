# Python string SQL

Enable syntax highlighting for SQL inside Python multiline strings using VS Code.

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

Multiline SQL statements require an SQL comment `-- SQL`
or `/* SQL */` as the same line as the opening triple quotes.

Note that this extension does not highlight SQL itself, it merely
uses whatever highlighter is associated with the `.sql` extension.

## Acknowledgements

The project was adpated from [es6-string-html](https://github.com/hanjingboo/es6-string-html).
Considerable insight into writing 
the [TextMate grammars](https://macromates.com/manual/en/language_grammars)
used by VS Code,
can be found in an [old blog post](https://www.apeth.com/nonblog/stories/textmatebundle.html)
by Matt Neuburg. 

