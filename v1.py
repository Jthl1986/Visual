import streamlit as st

st.set_page_config(page_title="Reporte Agro",page_icon="🌱",layout="wide")

st.title("Casos de mora")

left, right = st.columns(2)

# Tu código de inserción de Tableau
tableau_code = """
<div class='tableauPlaceholder' id='viz1710258658440' style='position: relative'><noscript><a href='#'><img alt='Hoja 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;Caidos_17098159316140&#47;Hoja1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Caidos_17098159316140&#47;Hoja1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;Caidos_17098159316140&#47;Hoja1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1710258658440');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""

url = "https://app.powerbi.com/reportEmbed?reportId=4fd5768a-6f9c-4e7c-84e4-4d6f0d81d708&autoAuth=true&ctid=4c818f79-ab84-4552-9b7c-2fe715b0d0d5&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXNvdXRoLWNlbnRyYWwtdXMtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D"

# Insertar el código de Tableau en la aplicación Streamlit
with left:
    st.components.v1.html(tableau_code, height=2000, scrolling=True)



with right:
    st.components.v1.iframe(url, height=600)
