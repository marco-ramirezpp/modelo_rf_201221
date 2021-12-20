import streamlit as st 
import pickle
import pandas as pd 

modelo_cargado = pickle.load(open('modelo_rf.pkl', 'rb'))

add_selectbox = st.sidebar.selectbox('Paginas', ('Pagina principal', 'implementación del modelo'))

if add_selectbox == 'Pagina principal':
  
    st.title('Aplicación modelo clasificación valor clientes')
    st.text('Esta pagina web tiene implementado un modelo de clasificación de valor de clientes a partir de sus caracteristicas')

if add_selectbox == 'implementación del modelo':

    st.title('Implementación Modelo ML')
    st.text('A continuación ingrese los valores de los parametros para obtener la predicción del cliente')

    Age = st.number_input('Age', min_value=18, max_value=100)
    Recency = st.number_input('Recency', min_value=0, max_value=100)
    gasto = st.number_input('gasto', min_value=0, max_value=5000)
    compras = st.number_input('compras', min_value=0, max_value=500)
    Income = st.number_input('Income', min_value=15000, max_value=300000)

    inputs = {'Age': Age, 'Recency': Recency, 'gasto': gasto,
              'compras' : compras, 'Income': Income}
    
    input_df = pd.DataFrame([inputs])
    
    if(st.button('Predecir')):
        preds = modelo_cargado.predict(input_df)
        output = int(preds)
        if output == 0:
            st.success('Este cliente es de Muy bajo valor')    
        elif output == 1: 
            st.success('Este cliente es de bajo valor')
        elif output == 2: 
            st.success('Este cliente es de Alto valor')
        else:
            st.success('Este cliente es de Muy alto valor')