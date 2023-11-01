"""
Script to generate an AST from a logical expression using plyplus.
"""

import sys
from plyplus import Grammar
from ASTTraverser import ASTTraverser

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Example call: {sys.argv[0]} programa.bc")
    elif sys.argv[1].split(".")[1] != "bc":
        print("La extension del archivo no reconocida")
    else:
        sourceFile = sys.argv[1]
        with open('bool.g', 'r', encoding='utf-8') as grm:
            with open(sourceFile, 'r', encoding='utf-8') as sc:
                scode = sc.read()
                # Crear el AST para la expresión en sourceFile
                ast = Grammar(grm.read(), auto_filter_tokens=False).parse(scode)
                # Exportar el AST como imagen
                ast.to_png_with_pydot("output.png")
                # Visitar el AST para evaluarlo
                #t = ASTTraverser()
                #t.visit(ast)
