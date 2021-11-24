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
    group = 'Relevancia_Septiembre'
    tboard = '1741254208'
    board = client.get_board_by_id(tboard)
    board.add_item(item_name=alumno, column_values=thisDict)
    st.success('Tu encuesta ha sido guardada')


# STREAMLIT
# Menú Usuario
st.title('Master in Ownership and Value Creation - Relevancia PIE Septiembre')
st.image('MOVC.jpg')
# Menú tareas
st.subheader('Selecciona tu Coach del Posgrado en Innovación y emprendimiento')
tap = st.selectbox("", ['Selecciona a tu Coach', 'Lorena Espinoza', 'Galia Gil', 'Laura Niebla', 'Carlos Dumois L. / Jaime Salazar', 'Baltasar Madrid'])
if tap == 'Lorena Espinoza':
    st.subheader('Alumno que califica')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    alumno = st.radio('Selecciona tu nombre de la lista: ',['Ricardo Clouthier','Manuel Lamadrid', 'Verónica Jiménez', 'Jaume Tort'])
    st.subheader('Califica a tu Consejo')
    if alumno == 'Ricardo Clouthier':
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',['Manuel Lamadrid', 'Verónica Jiménez', 'Jaume Tort'])
        if masr == 'Manuel Lamadrid':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Verónica Jiménez', 'Jaume Tort'])
        elif masr == 'Verónica Jiménez':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Manuel Lamadrid', 'Jaume Tort'])
        elif masr == 'Jaume Tort':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Manuel Lamadrid', 'Verónica Jiménez'])
    elif alumno == 'Manuel Lamadrid':
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',['Ricardo Clouthier', 'Verónica Jiménez', 'Jaume Tort'])
        if masr == 'Ricardo Clouthier':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Verónica Jiménez', 'Jaume Tort'])
        elif masr == 'Verónica Jiménez':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Ricardo Clouthier', 'Jaume Tort'])
        elif masr == 'Jaume Tort':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Ricardo Clouthier', 'Verónica Jiménez'])
    elif alumno == 'Verónica Jiménez':
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',['Ricardo Clouthier', 'Manuel Lamadrid', 'Jaume Tort'])
        if masr == 'Ricardo Clouthier':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Manuel Lamadrid', 'Jaume Tort'])
        elif masr == 'Manuel Lamadrid':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Ricardo Clouthier', 'Jaume Tort'])
        elif masr == 'Jaume Tort':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Ricardo Clouthier', 'Manuel Lamadrid'])
    elif alumno == 'Jaume Tort':
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',['Ricardo Clouthier', 'Manuel Lamadrid', 'Verónica Jiménez'])
        st.write(masr)
        if masr == 'Ricardo Clouthier':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Manuel Lamadrid', 'Verónica Jiménez'])
        elif masr == 'Manuel Lamadrid':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Ricardo Clouthier', 'Verónica Jiménez'])
        elif masr == 'Verónica Jiménez':  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',['Ricardo Clouthier', 'Manuel Lamadrid'])
    if st.button('Envíar Encuesta'):
        grabar()
elif tap == 'Galia Gil':
    g1 = 'Sofía de Rueda'
    g2 = 'Benjamín Garza'
    g3 = 'Gerardo Elizondo'
    g4 = 'Manuel Clouthier'
    g5 = 'Roberto Dumois'
    st.subheader('Alumno que califica')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    alumno = st.radio('Persona que caifica',[g1, g2, g3, g4, g5])
    st.subheader('Califica a tu Consejo')
    if alumno == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g2, g3, g4, g5])
        if masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g3, g4, g5])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g4, g5])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g3, g5])
        elif masr == g5:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g3, g4])
    elif alumno == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g3, g4, g5])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g3, g4, g5])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g4, g5])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g3, g5])
        elif masr == g5:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g3, g4])
    elif alumno == g3:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g4, g5])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g4, g5])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g4, g5])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2, g5])
        elif masr == g5:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2, g4])
    elif alumno == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g3, g5])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g3, g5])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g3, g5])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2, g5])
        elif masr == g5:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2, g3])
    elif alumno == g5:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g3, g4])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g3, g4])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g3, g4])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2, g4])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2, g3])
    if st.button('Envíar Encuesta'):
        grabar()
elif tap == 'Laura Niebla':
    g1 = 'César Sajché'
    g2 = 'Omar Alarcón'
    g3 = 'Luis Delfino'
    g4 = 'Alejandra Orozco'
    st.subheader('Alumno que califica')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    alumno = st.radio('Persona que caifica',[g1, g2, g3, g4])
    st.subheader('Califica a tu Consejo')
    if alumno == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g2, g3, g4])
        if masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g3, g4])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g4])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g3])
    elif alumno == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g3, g4])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g3, g4])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g4])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g3])
    elif alumno == g3:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g4])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g4])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g4])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2])
    elif alumno == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g3])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g3])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g3])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2])
    if st.button('Envíar Encuesta'):
        grabar()
elif tap == 'Carlos Dumois L. / Jaime Salazar':
    g1 = 'Octavio Oropeza'
    g2 = 'Adrián López'
    g3 = 'Sidney Camou'
    g4 = 'Albert Teixido'
    st.subheader('Alumno que califica')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    alumno = st.radio('Persona que caifica',[g1, g2, g3, g4])
    st.subheader('Califica a tu Consejo')
    if alumno == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g2, g3, g4])
        if masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g3, g4])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g4])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g3])
    elif alumno == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g3, g4])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g3, g4])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g4])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g3])
    elif alumno == g3:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g4])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g4])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g4])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2])
    elif alumno == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g3])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g3])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g3])
        elif masr == g3:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2])
    if st.button('Envíar Encuesta'):
        grabar()
elif tap == 'Baltasar Madrid':
    g1 = 'Sofia Estruga'
    g2 = 'Francisco Villegas'
    g4 = 'Julio Heinze'
    g5 = 'Alfonso Orozco'
    st.subheader('Alumno que califica')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    alumno = st.radio('Persona que caifica',[g1, g2, g4, g5])
    st.subheader('Califica a tu Consejo')
    if alumno == g1:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g2, g4, g5])
        if masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g4, g5])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g5])
        elif masr == g5:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g4])
    elif alumno == g2:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g4, g5])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g4, g5])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g5])
        elif masr == g5:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g4])
    elif alumno == g4:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g5])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g5])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g5])
        elif masr == g5:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2])
    elif alumno == g5:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        masr = st.radio('Persona que consideras la Más Relevante en tu Consejo',[g1, g2, g4])
        if masr == g1:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g2, g4])
        elif masr == g2:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g4])
        elif masr == g4:  
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            menosr = st.radio('Persona que consideras la Menos Relevante en tu Consejo',[g1, g2])
    if st.button('Envíar Encuesta'):
        grabar()
else:
    st.subheader('Aún no has seleccionado a tu Coach')
