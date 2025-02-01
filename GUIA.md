# Guia de Comandos Git

## Clonar Repositósio

```
    git clone <URLDoRepositorio>
```

## Controle de versão

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

## Repositório remoto

Enviando a branch para o repositório remoto:
```
    git push -u origin <nomeDaBranch>
```

Atualizando o repositório local:
```
    git pull origin <nomeDaBranch>
```