import os
import dash
from dash import html, Input, Output, State
from layout import get_layout
from funciones import cargar_excel, cargar_nombres_pdf, procesar_pdfs
app = dash.Dash(__name__)
server = app.server
app.layout = get_layout()
@app.callback([Output('output-mensaje', 'children'), Output('output-mensaje', 'style')], Input('btn-generar', 'n_clicks'), State('input-carpeta-pdfs', 'value'), prevent_initial_call=True)
def generar_pdfs(n_clicks, carpeta_pdfs):
    estilo_visible = {'display': 'block', 'margin-top': '30px', 'padding': '20px', 'border-radius': '6px', 'background': '#ecf0f1'}
    estilo_oculto = {'display': 'none'}
    if not carpeta_pdfs:
        return html.Div("❌ Por favor, ingresa la ruta de la carpeta", style={'color': 'red'}), estilo_visible
    if not os.path.exists(carpeta_pdfs):
        return html.Div(f"❌ No se encuentra la carpeta: {carpeta_pdfs}", style={'color': 'red'}), estilo_visible
    ruta_sello = os.path.join(carpeta_pdfs, "SELLO.png")
    ruta_excel = os.path.join(carpeta_pdfs, "nombre-folio.xlsx")
    if not os.path.exists(ruta_excel):
        return html.Div(f"❌ No se encuentra el archivo Excel 'nombre-folio.xlsx' en: {carpeta_pdfs}", style={'color': 'red'}), estilo_visible
    if not os.path.exists(ruta_sello):
        return html.Div(f"❌ No se encuentra el archivo 'SELLO.png' en: {carpeta_pdfs}", style={'color': 'red'}), estilo_visible
    carpeta_salida = os.path.join(carpeta_pdfs, "PDF_generados")
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    try:
        df = cargar_excel(ruta_excel)
        df["nombre"] = cargar_nombres_pdf(carpeta_pdfs)
        archivos = procesar_pdfs(df, carpeta_pdfs, ruta_sello, carpeta_salida)
        return html.Div([html.H3("✅ PROCESO COMPLETADO", style={'color': 'green', 'margin-bottom': '10px'}),html.P(f"Total de archivos procesados: {len(archivos)}", style={'margin': '5px 0', 'color': '#555'}),html.P(f"Guardados en: {carpeta_salida}", style={'margin': '5px 0', 'color': '#555'})]), estilo_visible
    except Exception as e:
        return html.Div(f"❌ Error: {str(e)}", style={'color': 'red'}), estilo_visible
@app.callback([Output('output-mensaje', 'children', allow_duplicate=True), Output('output-mensaje', 'style', allow_duplicate=True), Output('input-carpeta-pdfs', 'value')], Input('btn-limpiar', 'n_clicks'), prevent_initial_call=True)
def limpiar(n_clicks):
    return "", {'display': 'none'}, ""
if __name__ == '__main__':
    app.run_server(debug=False)