#!/bin/bash

# Variáveis
# Caminho do diretório de hooks do Git
HOOK_DIR=".git/hooks"
# Caminho dos hooks no repositório
REPO_HOOKS_DIR="hooks"

# Configuração de Hooks Git

# Copia todos os arquivos e diretórios de hooks para o diretório .git/hooks/
cp -r "$REPO_HOOKS_DIR/"* "$HOOK_DIR/"

# Torna todos os arquivos no .git/hooks executáveis
chmod +x "$HOOK_DIR/"*

echo "Hooks configurados com sucesso."
