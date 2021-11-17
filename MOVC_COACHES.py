import streamlit as st
import pandas as pd
#import numpy as np
import moncli
from moncli import client

moncli.api.api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjEyNDA3MDQ4OSwidWlkIjoxNjIzOTI1MCwiaWFkIjoiMjAyMS0wOS0xMFQwNDozOToxNC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NzE1NjUwNSwicmduIjoidXNlMSJ9.7qjR_U4xyaavf5lPxAz2OjwYDcUTQoFE6kJeaLfJWq0'
moncli.api.connection_timeout = 30

# Monday
def grabar():
    thisDict = {'texto': masr, 'texto4': menosr}
    group = 'Relevancia_Septiembre_Coach'
    tboard = '1741769116'
    board = client.get_board_by_id(tboard)
    board.add_item(item_name=tap, column_values=thisDict)
    st.success('Tu encuesta ha sido guardada')


# STREAMLIT
# Menú Usuario
st.title('Master in Ownership and Value Creation - Relevancia PIE Septiembre')
st.image('MOVC.jpg')
# Menú tareas
st.subheader('Selecciona tu consejo identificando tu nombre:')
tap = st.selectbox("", ['Identificate como Coach', 'Lorena Espinoza', 'Galia Gil', 'Laura Niebla', 'Carlos Dumois L. / Jaime Salazar', 'Baltasar Madrid'])
if tap == 'Lorena Espinoza':
    g1 = 'Ricardo Clouthier'
    g2 = 'Manuel Lamadrid'
    g3 = 'Verónica Jiménez'
    g4 = 'Jaume Tort'
    st.subheader('Califica a tu Consejo')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    masr = st.radio('ALumno que considera como el Más Relevante en tu Consejo',[g1, g2, g3, g4])
    if masr == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g2, g3, g4])
    elif masr == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g3, g4])
    elif masr == g3:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g4])
    elif masr == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g3])
    
elif tap == 'Galia Gil':
    g1 = 'Sofia de Rueda'
    g2 = 'Benjamín Garza'
    g3 = 'Gerardo Elizondo'
    g4 = 'Manuel CLouthier'
    g5 = 'Roberto Dumois'
    st.subheader('Califica a tu Consejo')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    masr = st.radio('ALumno que considera como el Más Relevante en tu Consejo',[g1, g2, g3, g4, g5])
    if masr == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g2, g3, g4, g5])
    elif masr == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g3, g4, g5])
    elif masr == g3:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g4, g5])
    elif masr == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g3, g5])
    elif masr == g5:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g3, g4])

elif tap == 'Laura Niebla':
    g1 = 'César Sajché'
    g2 = 'Omar Alarcón'
    g3 = 'Luis Delfino'
    g4 = 'Aleandra Orozco'
    st.subheader('Califica a tu Consejo')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    masr = st.radio('ALumno que considera como el Más Relevante en tu Consejo',[g1, g2, g3, g4])
    if masr == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g2, g3, g4])
    elif masr == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g3, g4])
    elif masr == g3:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g4])
    elif masr == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g3])

elif tap == 'Carlos Dumois L. / Jaime Salazar':
    g1 = 'Octavio Oropeza'
    g2 = 'Adrián López'
    g3 = 'Sidney Camou'
    g4 = 'Albert Teixido'
    st.subheader('Califica a tu Consejo')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    masr = st.radio('ALumno que considera como el Más Relevante en tu Consejo',[g1, g2, g3, g4])
    if masr == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g2, g3, g4])
    elif masr == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g3, g4])
    elif masr == g3:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g4])
    elif masr == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g3])
    
elif tap == 'Baltasar Madrid':
    g1 = 'Sofia Estruga'
    g2 = 'Francisco Villegas'
    g3 = 'Luis Vizcarra'
    g4 = 'Julio Heinze'
    g5 = 'Alfonso Orozco'
    st.subheader('Califica a tu Consejo')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    masr = st.radio('ALumno que considera como el Más Relevante en tu Consejo',[g1, g2, g4, g5])
    if masr == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g2, g4, g5])
    elif masr == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g4, g5])
    elif masr == g3:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g4, g5])
    elif masr == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g5])
    elif masr == g5:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        menosr = st.radio('Alumno que considera como el Menos Relevante en tu Consejo',[g1, g2, g4])
    
else:
    st.subheader('Aún no has seleccionado a tu Coach')

if st.button('Enviar Encuesta'):
    grabar()
