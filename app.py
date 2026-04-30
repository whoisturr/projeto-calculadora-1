import streamlit as st
import calculadora as calc


st.title("calculadora ╰(*°▽°*)╯")

numero1 = st.number_input("digite o primeiro número: ", step=0.1,value=None)
numero2 = st.number_input("digite o segundo número: ", step=0.1,value=None)
operacao = st.selectbox("selecione a operação",["+","-","*","/"])

if st.button("Calcular"):
    resultado = calc.calcular(numero1 , numero2 , operacao)
    st.success(f"sua continha: {numero1} {operacao} {numero2} resulta em: {resultado}")

    

