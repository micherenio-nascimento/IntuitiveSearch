# Backend - API FastAPI

Este é um servidor FastAPI que fornece uma API para buscar operadores a partir de um arquivo CSV. Abaixo estão as instruções de como rodar o backend utilizando o Uvicorn, além dos detalhes sobre os endpoints e filtros disponíveis.

---

### **Como Executar o Backend com o Uvicorn**

Para rodar o servidor de desenvolvimento do FastAPI usando o Uvicorn, siga os seguintes passos:

### **Ativar o Ambiente Virtual:**

Certifique-se de que o ambiente virtual (`venv`) está ativado. Se ainda não o fez, crie e ative o ambiente conforme as instruções abaixo:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Para Linux/Mac
   venv\Scripts\activate      # Para Windows
   ```

### **Executar o Uvicorn:**

Para iniciar o servidor de desenvolvimento, execute o seguinte comando dentro da pasta `Backend`:

   ```bash
   uvicorn main:app --reload
   ```

Esse comando iniciará o servidor na URL [**http://127.0.0.1:8000**](http://127.0.0.1:8000/) com o modo de recarga ativado. Isso significa que qualquer mudança no código fará com que o servidor reinicie automaticamente.

### **Acessar a API:**

Após o servidor iniciar, você pode acessar a API diretamente no seu navegador ou usar ferramentas como **Postman** ou **Insomnia** para interagir com ela:

   - **URL da API:** `http://127.0.0.1:8000`

---

### **Endpoints da API**

A API oferece um endpoint para realizar buscas de operadores presentes em um arquivo CSV. Abaixo estão os detalhes deste endpoint.

---

### **Endpoint: `/api/operators/search`**

- **Método:** `GET`

---

### **Parâmetros de Consulta:**

- `query` (string) [opcional]: Um termo de busca para procurar operadores com base nos seguintes campos:
    - **Razão Social (`Razao_Social`)**
    - **Nome Fantasia (`Nome_Fantasia`)**
    - **CNPJ (`CNPJ`)**
    - **Registro ANS (`Registro_ANS`)**

---

### **Exemplo de Requisição:**

1. **Busca com termo de pesquisa ("EXEMPLO"):**

    Para realizar uma busca de operadores com o nome "EXEMPLO", a requisição seria:


    ```bash
    GET http://127.0.0.1:8000/api/operators/search?query=EXEMPLO
    ```

2. **Buscar todos os operadores:**

    Se o parâmetro `query` for omitido ou deixado vazio, a requisição irá retornar **todos os operadores** disponíveis no arquivo CSV:

    ```bash
    GET http://127.0.0.1:8000/api/operators/search
    ```

---

### **Exemplo de Resposta:**

A resposta será uma lista de operadores que correspondem ao termo de busca. Exemplo de resposta:

```json
{
  "operators": [
    {
      "Registro_ANS": "419761",
      "CNPJ": "19541931000125",
      "Razao_Social": "EXEMPLO ADMINISTRADORA DE BENEFÍCIOS LTDA",
      "Nome_Fantasia": "",
      "Modalidade": "Administradora de Benefícios",
      "Logradouro": "RUA EXEMPLO DE REZENDE",
      "Numero": "274",
      "Complemento": "",
      "Bairro": "PRAÇA CENTRAL",
      "Cidade": "Exemplo City",
      "UF": "EX",
      "CEP": "36660000",
      "DDD": "32",
      "Telefone": "34624649",
      "Fax": "36526021",
      "Endereco_eletronico": "contabilidade@exemplo.com.br",
      "Representante": "JOÃO SILVA",
      "Cargo_Representante": "SÓCIO ADMINISTRADOR",
      "Regiao_de_Comercializacao": "6",
      "Data_Registro_ANS": "2020-05-19"
    }
  ]
}
```

---

### **Filtros de Pesquisa Disponíveis:**

A pesquisa pode ser realizada nos seguintes campos:

1. **Razão Social (`Razao_Social`)**
    
    Exemplo de termo pesquisável: `"EXEMPLO ADMINISTRADORA DE BENEFÍCIOS LTDA"`
    
2. **Nome Fantasia (`Nome_Fantasia`)**
    
    Exemplo de termo pesquisável: `"EXEMPLO SAÚDE"`
    
3. **CNPJ (`CNPJ`)**
    
    Exemplo de termo pesquisável: `"19541931000125"`
    
4. **Registro ANS (`Registro_ANS`)**
    
    Exemplo de termo pesquisável: `"419761"`
