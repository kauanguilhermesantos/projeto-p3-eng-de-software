# **Título:** Fazer Reserva  

**Descrição:** O Usuário faz uma reserva de um livro.  

**Atores:**  
- Usuário  
- Sistema  

# **Fluxo:**  

### **Principal:**  
**1.** O Usuário seleciona a opção de Fazer Reserva.  
**2.** O Sistema pede pelo nome de usuário que irá fazer a reserva.  
**3.** O usuário insere o nome dele.  
**4.** O Sistema pede pelo nome do livro a ser reservado.  
**5.** O usuário insere o título do livro.  
**6.** O Sistema faz a reserva do livro.  

### **Fluxo de Exceções:**  
- **3.1.** Se o usuário não tiver cadastro, a operação é cancelada.  
- **5.1.** Se o Sistema não encontrar o livro pelo título, a operação é cancelada.  
- **6.1.** Se o Sistema não conseguir realizar a reserva, a operação é cancelada.  

---
**Pós-Condições:** O Sistema realiza a reserva do livro para o usuário.  
