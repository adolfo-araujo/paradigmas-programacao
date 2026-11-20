#!/usr/bin/env python3
"""Checagens de sintaxe/compilação sem modificar os arquivos do repositório."""
from __future__ import annotations
import ast
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
EXERCICIOS = ROOT / "aulas"

def main() -> int:
    arquivos_py = sorted(EXERCICIOS.rglob("*.py"))
    arquivos_c = sorted(EXERCICIOS.rglob("*.c"))
    codigos_java = sorted(EXERCICIOS.rglob("*.java"))
    erros = []
    print(f"Arquivos: {len(arquivos_py)} Python, {len(arquivos_c)} C, {len(codigos_java)} Java")
    for path in arquivos_py:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except Exception as exc:
            erros.append(f"Python {path.relative_to(ROOT)}: {exc}")
    print(f"Python: {len(arquivos_py)} verificados")

    with tempfile.TemporaryDirectory(prefix="plp-validar-") as tmp:
        temp = Path(tmp)
        if not shutil.which("gcc"):
            erros.append("GCC não encontrado: a compilação C não foi verificada")
        else:
            for i, path in enumerate(arquivos_c):
                result = subprocess.run(["gcc", "-std=c11", "-Wall", "-Wextra", "-pedantic", str(path), "-o", str(temp / f"programa{i}")], text=True, capture_output=True)
                if result.returncode:
                    erros.append(f"C {path.relative_to(ROOT)}:\n{result.stderr}")
            print(f"C: {len(arquivos_c)} compilações executadas")

        if not shutil.which("javac"):
            erros.append("javac não encontrado: a compilação Java não foi verificada")
        else:
            # Cada programa Java possui uma classe principal própria e deve ser compilado isoladamente.
            grupos = {}
            for file in codigos_java:
                if 'src' in file.parts:
                    group = file.parent.parent if file.parent.name == 'classe' else file.parent
                    # .../java/src  -> agrupar pelo diretório src
                    group = next((p for p in file.parents if p.name == 'src'), file.parent)
                else:
                    group = file.parent
                grupos.setdefault(group, []).append(file)
            for idx, (group, arquivos) in enumerate(sorted(grupos.items())):
                destino = temp / f"java{idx}"
                destino.mkdir()
                result = subprocess.run(["javac", "-encoding", "UTF-8", "-d", str(destino), *map(str, arquivos)], capture_output=True, text=True)
                if result.returncode:
                    erros.append(f"Java {group.relative_to(ROOT)}:\n{result.stderr}")
            print(f"Java: {len(grupos)} projetos compilados ({len(codigos_java)} arquivos)")

    if erros:
        print("\nFALHAS:")
        for erro in erros:
            print("-", erro)
        return 1
    print("\nOK: sintaxe Python e compilação C/Java concluídas.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
