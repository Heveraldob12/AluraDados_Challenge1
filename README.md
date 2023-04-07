# Alura Cash | Challenge Dados

Projeto do Desafio de dados da [Alura](https://www.alura.com.br) #alura

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **Challenge Dados Alura**
| :label: Tecnologias | MySQL,Pyhton,Jupyter Notebook, Power Bi (tecnologias utilizadas)
| :fire: Desafio     | https://www.alura.com.br/challenges/dados?host=https://cursos.alura.com.br

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](file:///D:/Arquivos-antigos/Progamação/challenge/Fotos/Alura_Cash_logo-removebg-preview.png#vitrinedev)

## Detalhes do projeto

### Dicionário de dados por tabela

### dados_mutuarios

Tabela contendo os dados pessoais de cada solicitante

| Feature | Característica |
| --- | --- |
|`person_id`|ID da pessoa solicitante|
| `person_age` | Idade da pessoa - em anos - que solicita empréstimo |
| `person_income` | Salário anual da pessoa solicitante |
| `person_home_ownership` | Situação da propriedade que a pessoa possui: *Alugada* (`Rent`), *Própria* (`Own`), *Hipotecada* (`Mortgage`) e *Outros casos* (`Other`) |
| `person_emp_length` | Tempo - em anos - que a pessoa trabalhou |

### emprestimos

Tabela contendo as informações do empréstimo solicitado

| Feature | Característica |
| --- | --- |
|`loan_id`|ID da solicitação de empréstico de cada solicitante|
| `loan_intent` | Motivo do empréstimo: *Pessoal* (`Personal`), *Educativo* (`Education`), *Médico* (`Medical`), *Empreendimento* (`Venture`), *Melhora do lar* (`Homeimprovement`), *Pagamento de débitos* (`Debtconsolidation`) |
| `loan_grade` | Pontuação de empréstimos, por nível variando de `A` a `G` |
| `loan_amnt` | Valor total do empréstimo solicitado |
| `loan_int_rate` | Taxa de juros |
| `loan_status` | Possibilidade de inadimplência |
| `loan_percent_income` | Renda percentual entre o *valor total do empréstimo* e o *salário anual* |


### historicos_banco

Histório de emprétimos de cada cliente

| Feature | Característica |
| --- | --- |
|`cb_id`|ID do histórico de cada solicitante|
| `cb_person_default_on_file` | Indica se a pessoa já foi inadimplente: sim (`Y`,`YES`) e não (`N`,`NO`) |
| `cb_person_cred_hist_length` | Tempo - em anos - desde a primeira solicitação de crédito ou aquisição de um cartão de crédito |

### id

Tabela que relaciona os IDs de cada informação da pessoa solicitante

| Feature | Característica |
| --- | --- |
|`person_id`|ID da pessoa solicitante|
|`loan_id`|ID da solicitação de empréstico de cada solicitante|
|`cb_id`|ID do histórico de cada solicitante|


✅Primeiro Alura Challenge Concluido #alura #alurachallengedatascience2

# Resumos:
## Semana 1 💾
Nessa semana meu foco foi em entender e analisar o banco de dados da Alura Cash e fazer alguns tratamentos de dados nulos e em brancos(Resolvi fazer esse tratamento pelo Jupyter, pois tenho maior familiaridade). Antes disso, juntei as tabelas e exportei elas em forma de [csv](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/DADOS/DADOSJUNTOS.csv) para a utilização no Jupyer Notebook

---

This week my focus was on understanding and analyzing the Alura Cash's database and doing some treatments of null and blank data (I decided to do this treatment using Jupyter, as I am more familiar with it). Before that, I joined the tables and exported them in the form of [csv](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/DADOS/DADOSJUNTOS.csv) for use in Jupyer Notebook

## Semana 2 🐍

Como já havia adiantado parte do tratamento, nessa etapa eu removi alguns Outliers e vi a Correlação entre as variáveis para ter melhor entendimento quando for realizar os modelos de Machine learning. Logo após, realizei o balanceamento para que pudesse fazer os modelos de o [endcoding](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/one_hot_enc.pkl), [normalização](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/norm.pkl), vale ressaltar que, tive certos problemas na realização do endcoding e balanceamentos, que foram sanados no Discord do challenge.
Então, já tendo os modelos de endcoding e normalização exportados pelo pickle, passei a fazer e analisar o modelo de classificação em si, utilizei diversos métodos, contudo o [GradientBoostingClassifier](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/model.pkl) foi o que se saiu melhor ao meu critério.

---
As I had already advanced part of the treatment, at this stage I removed some Outliers and saw the Correlation between the variables to have a better understanding when performing the Machine learning models. Soon after, I performed the balancing so that I could make the models of the [endcoding](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/one_hot_enc.pkl), [normalization](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/norm.pkl), it is worth noting that I had certain problems with endcoding and balancing, which were resolved in the challenge's Discord.
So, already having the endcoding and normalization models exported by pickle, I started to make and analyze the classification model itself, I used several methods, however [GradientBoostingClassifier](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/model.pkl) did the best job in my opinion.

# Semana 3 e 4 🎨
Essa foi a semana mais desafiadora, não tinha muita experiência com APIs até aquele momentos então passei muita dificuldade em criar uma, até que com prática e aulas na Plataforma Alura eu consegui fazer tanto a [API](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/main.py) quanto por minhas visões e dados da API. 

---

This was the most challenging week, I didn't have much experience with APIs until that moment so I had a lot of difficulty creating one, until with practice and classes on the Alura Platform I managed to do both the [API](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/main.py) and my API views and data.

Dashboard abaixo:
![https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/DashBoard/Alura.pbix](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/DashBoard/Captura%20de%20tela%202023-02-02%20202007.png)




## 
☢️☢️☢️ Qualquer erro de código ou gramatical, por favor entrar em contato

☢️☢️☢️ Any code or grammatical errors, please contact me
