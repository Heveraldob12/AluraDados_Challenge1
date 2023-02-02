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
Nessa semana meu foco foi em entender e analizar o banco de dados da Alura Cash e fazer alguns tratamentos de dados nulos e em brancos(Resolvi fazer esse tratamento pelo Jupyter,pois tenho maior familharidade).Antes disso, juntei as tabelas e exportei elas em forma de [csv](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/DADOS/DADOSJUNTOS.csv) para o utilização no Jupyer Notebook


## Semana 2 🐍

Como já havia andiantado parte do tratamento, nessa etapa eu removi alguns Outliers e vi a Correlação entre as variavéis para ter melhor entendimento quando for realizar os modelos de Machine learing.Logo após, realizei o balenceamento para que pudesse fazer os modelos de o [endcoding](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/one_hot_enc.pkl), [normalização](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/norm.pkl),vale ressaltar que,  tive certos problemas na realização do endcoding e balanceamentos, que foram sanados no Discord do challenge.
Então já tendo os modelos de endcoding e normalização exportados pelo pickle, passei a fazer e analizar o modelo de classificação em si utilizei diversos métodos, contudo o [GradientBoostingClassifier](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/pikle%20and%20model/model.pkl) foi o que se saiu melhor ao meu critério.

# Semana 3 e 4 🎨
Essa foi a semana mais desafiadora, não tinha muita experiência com APIs até aquele momentos então passei muita dificuldade em criar uma, até que com prática e aulas na Plataforma Alura eu consegui fazer tanto a [API](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/main.py) quanto por meus insights e dados da API no Dashboard abaixo:
![https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/DashBoard/Alura.pbix](https://github.com/Heveraldob12/AluraDados_Challenge1/blob/main/DashBoard/Captura%20de%20tela%202023-02-02%20202007.png)




--
Caso tenha algum erro gramatical ou de progamação peço para que entrem em contato comigo. ☢️☢️☢️
