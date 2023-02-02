#................................................#
############IMPORTS##############
from fastapi import FastAPI
import pandas as pd
import pickle as pk
import numpy as np
#################################
#..............................................#
with open('./one_hot_enc.pkl', 'rb') as f:
    one_hot_enc = pk.load(f)
    
with open('./norm.pkl', 'rb') as f:
    norm = pk.load(f)
    
with open('./model.pkl', 'rb') as f:
    modelo = pk.load(f)
#..............................................#

app =  FastAPI()


@app.get("/")
def hello_root():
    return {"root" : "Bem vindo você está na raiz da minha API"}

@app.get("/modelo/v1={idade}&v2={salario_anual}&v3={situacao_moradia}&v4={tempo_de_trabalho}&v5={motivo_do_emprestimo}&v6={pontuacao}&v7={valor_emprestimo}&v8={taxa_de_juros}&v9={renda_percentual}&v10={possibilidade_de_inadimplencia}&v11={tempo_solicitacao}")
def previsão_modelo(idade:int,
                    salario_anual:int, 
                    situacao_moradia:str, 
                    tempo_de_trabalho:int, 
                    motivo_do_emprestimo:str,
                    pontuacao:str, 
                    valor_emprestimo:int,
                    taxa_de_juros:float, 
                    renda_percentual:int,
                    possibilidade_de_inadimplencia:int, 
                    tempo_solicitacao:int):
    
    global var,data
    var  ={
        'idade': [idade],
        'salario_anual': [salario_anual],
        'situacao_moradia': [situacao_moradia],
        'tempo_de_trabalho': [tempo_de_trabalho],
        'motivo_do_emprestimo': [motivo_do_emprestimo],
        'pontuacao': [pontuacao],
        'valor_emprestimo': [valor_emprestimo],
        'taxa_de_juros': [taxa_de_juros],
        'possibilidade_de_inadimplencia': [possibilidade_de_inadimplencia],
        'renda_percentual': [renda_percentual],
        'tempo_solicitacao': [tempo_solicitacao]}
    
    data = pd.DataFrame(var, index=[0])


    df_pred= one_hot_enc.transform(data)
    df_pred= pd.DataFrame(df_pred,columns=one_hot_enc.get_feature_names_out())
    
    x= norm.transform(df_pred)
    
    previsao = modelo.predict(x)
    
    return  {"previsao": previsao[0],
             'probability_0': modelo.predict_proba(x).tolist()[0][0],
             'probability_1': modelo.predict_proba(x).tolist()[0][1]}
