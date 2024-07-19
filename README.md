# French_Verb_API

## Bibliotecas Necessárias
```
pip install flask
pip install request
pip install pyjwt
pip install bcrypt

```

## Postman - Utilização
1. Realizar o Import da Collection
2. Escolher qual API deseja utilizar
3. Create-User(se desejar) 
    Para criar seu próprio usuário. Após a criação de um usuário, é necessária a realização de Login para capturar o Token de validação
4. Login
    Deve-se enviar o email e password no body. (Já tem um exemplo na collection)
5. GET_Verb
    alterar o verbo no body para realizar a chamada.
    obs.: Se você utilizou o create-user e login, deverá atualizar o header para atualizar o conteúdo do token obtido no login. (alterar o value do parâmetro x-access-token)
6. GET_Random_Verbs
    alterar o value em quantity no body com a quantidade que deseja retornar
    retorno: lista de verbos aleatórios origem API do Professor.
7. Add Favorite Verb
   Informar no Body qual o Verbo deseja gravar como favorito.
   Retorno: ID do Verbo gravado
8. Get One Favorite Verb
   Informar na URL o ID Favorite Verb que deseja consultar
   exemplo: http://127.0.0.1:5000/verbs/favorites/66085f1d350faefca2ba6b1c
9. Get All Favorite Verb
   Irá retornar todos os favorites Verbs conforme o Usuário Logado
10. Delete Favorite Verb
    Informar na URL o ID Favorite Verb que deseja deletar
    exemplo: http://127.0.0.1:5000/verbs/favorites/66085f1d350faefca2ba6b1c
    
## MONGODB - Account

Email: cansaditosdepython@gmail.com
Senha: cansaditos

Em Database temos 2 collections, User and Verbs
### FRENCH-VERB-API.users
Irá apresentar os resultados de cadastros de usuários no object store

### FRENCH-VERB-API.verbs
Irá apresentar os resultados de cadastros de verbos dos usuários no object store


