# -*- coding: utf-8 -*-
from dash import dcc, html
def get_layout():
    return html.Div([
        html.Div([
            html.H1("Sistema de Validación y Sellado de PDFs"),
            html.Div([
                html.Label("Carpeta con PDFs, Excel y SELLO.png:"),
                html.P("La carpeta debe contener:", style={'margin': '5px 0 5px 20px', 'font-size': '0.9em', 'color': '#666'}),
                html.Ul([
                    html.Li("Los archivos PDF a procesar"), html.Li("El archivo 'nombre-folio.xlsx'"),html.Li("El archivo 'SELLO.png'")
                ], style={'margin': '0 0 10px 40px', 'font-size': '0.9em', 'color': '#666'}),
                dcc.Input(
                    id='input-carpeta-pdfs', 
                    type='text', 
                    placeholder='C:\\Users\\Héctor\\Documents\\Programacion\\Python\\Validación\\Archivos_PDF', 
                    className='input-field'
                ),
            ], className='input-group'),
            html.Div([
                html.Button('Generar PDFs', id='btn-generar', className='btn-primary', n_clicks=0),
                html.Button('Limpiar', id='btn-limpiar', className='btn-secondary', n_clicks=0),
            ], className='button-group'),      
            html.Div(id='output-mensaje', style={'display': 'none'})
        ], className='container')
    ])