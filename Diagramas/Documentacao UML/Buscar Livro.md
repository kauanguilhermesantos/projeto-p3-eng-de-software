# **Título:** Buscar Livro  

**Descrição:** O Usuário busca por um livro na livraria.  

**Atores:**  
- Usuário  
- Sistema  


# **Fluxo:**  

### **Principal:**  
1. O Usuário seleciona a opção de buscar livro.  
2. O Sistema dá opções de buscar por título, autor ou categoria.  

### **Alternativo:**  
- **1.1.** O Usuário seleciona a opção de Buscar por Título  
  - **2.1.** O Sistema pede pelo título do livro.  
  - **3.1.** O Usuário preenche o campo com o título do livro.  
  - **4.1.** O Sistema busca o livro pelo título dele.  

- **1.2.** O Usuário seleciona a opção de Buscar por Autor.  
  - **2.2.** O Sistema pede pelo autor do livro.  
  - **3.2.** O Usuário preenche o campo com o autor do livro.  
  - **4.2.** O Sistema busca os livros pelo autor.  

- **1.3.** O Usuário seleciona a opção de Buscar por Categoria.  
  - **2.3.** O Sistema fornece opções de categoria para escolher.  
  - **3.3.** O Usuário seleciona qual categoria deseja pesquisar.  
  - **4.3.** O Sistema busca os livros com a categoria desejada.  

### **Fluxo de Exceções:**  
- **4.** O Sistema não consegue encontrar o livro por título, autor ou categoria.  

---
**Pós-Condições:** O Sistema busca os livros desejados.
