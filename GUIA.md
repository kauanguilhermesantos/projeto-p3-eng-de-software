# Guia de Comandos Git

## Clonar Repositósio

```
    git clone <URLDoRepositorio>
```

## Controle de versão

Verificando alterações do repositório remoto:
```
    git pull
```

Adicionando um arquivo específico ao stage:
```
    git add <nomeDoArquivo>
```

Adicionando todos os arquivos modificados ao stage:
```
    git add .
```

Resgistrando um commit com mensagem:
```
    git commit -m "mensagem do commit"
```

Enviando commit para o repositório remoto:
```
    git push
```

## Branches

Listando branches criadas:
```
    git branch
```

Criando uma nova branch:
```
    git branch <nomeDaBranch>
```

Mudando para uma outra branch:
```
    git checkout <nomeDaBranch>
```

Criando e mudando para a branch criada:
```
    git checkout -b <nomeDaBranch>
```

Deletando uma branch local:
```
    git branch -d <nome-da-branch>
```

Forçando a deleção de uma branch:
```
    git branch -D <nome-da-branch>
```

## Merge
Fazendo merge de uma branch na branch atual.
```
    git merge <nome-da-branch>
```

## Repositório remoto

Enviando a branch para o repositório remoto:
```
    git push -u origin <nomeDaBranch>
```

Atualizando o repositório local:
```
    git pull origin <nomeDaBranch>
```