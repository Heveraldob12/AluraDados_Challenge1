##FUNCTION
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import make_column_transformer
import pandas as pd
def OneHotEncoding(X):
    one = make_column_transformer(
        (OneHotEncoder(), ['situacao_moradia','motivo_do_emprestimo','pontuacao']), 
        remainder="passthrough")

    dados_transformados= one.fit_transform(X)
    return  pd.DataFrame(dados_transformados, columns=one.get_feature_names_out())

def normalização(dados):
    norm = MinMaxScaler()
    dados_novo=norm.fit_transform(dados)
    return dados_novo

