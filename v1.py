import streamlit as st

st.set_page_config(page_title="Reporte Agro",page_icon="🌱",layout="wide")

# Agregar una fila para centrar el título
st.write("<h1 style='text-align: center;'>Distribución de filiales</h1>", unsafe_allow_html=True)

left, right = st.columns(2)

# Tu código de inserción de Tableau
tableau_code = """
<div class='tableauPlaceholder' id='viz1713543317038' style='position: relative'><noscript><a href='#'><img alt='Hoja 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ge&#47;Geofiliales&#47;Hoja1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Geofiliales&#47;Hoja1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ge&#47;Geofiliales&#47;Hoja1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1713543317038');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""

tableau_code2 = """
<div class='tableauPlaceholder' id='viz1713547913060' style='position: relative'><noscript><a href='#'><img alt='Hoja 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ge&#47;Geofiliales1&#47;Hoja2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Geofiliales1&#47;Hoja2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ge&#47;Geofiliales1&#47;Hoja2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1713547913060');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""

# Insertar el código de Tableau en la aplicación Streamlit
with left:
    st.components.v1.html(tableau_code, height=5000, scrolling=True)

with right:
    st.components.v1.html(tableau_code2, height=5000, scrolling=True)

