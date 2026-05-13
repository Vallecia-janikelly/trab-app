import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title=&quot;Perfil&quot;, layout=&quot;wide&quot;)

# FUNÇÃO base64
def get_base64_image(path):
with open(path, &quot;rb&quot;) as img_file:
return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image(&quot;Instagram_icon.png&quot;)
zap_base64 = get_base64_image(&quot;whats.jpg&quot;)

# TOPO (imagem clicável)
col1, col2, col3 = st.columns([1,2,1])

with col2:
st.markdown(f&quot;&quot;&quot;
&lt;div style=&quot;text-align: center; margin-bottom: 50px;&quot;&gt;
&lt;a href=&quot;https://www.instagram.com//&quot; target=&quot;_blank&quot;&gt;
&lt;img src=&quot;data:Instagram_icon.png;base64,{img_base64}&quot;
width=&quot;320&quot;
style=&quot;border-radius:12px;&quot;&gt;
&lt;/a&gt;
&lt;/div&gt;
&quot;&quot;&quot;, unsafe_allow_html=True)

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3,1])

with col_left:
st.markdown(&quot;&quot;&quot;
&lt;div style=&#39;margin-bottom:30px; font-size:30px;&#39;&gt;
&lt;b&gt;Nome Dinaldo Jorge&lt;/b&gt;
&lt;/div&gt;
&quot;&quot;&quot;, unsafe_allow_html=True)

# subcolunas
subcol1, subcol2 = st.columns([1,4])

# IMAGEM (centralizada verticalmente)
with subcol1:
st.markdown(&quot;&quot;&quot;
&lt;div style=&quot;
display: flex;
align-items: center;
height: 100%;
&quot;&gt;
&quot;&quot;&quot;, unsafe_allow_html=True)

st.image(&quot;foto.jpg&quot;, width=800)

st.markdown(&quot;&lt;/div&gt;&quot;, unsafe_allow_html=True)

# TEXTO
with subcol2:
st.markdown(&quot;&quot;&quot;
&lt;div style=&quot;
text-align: justify;
font-size: 20px;
line-height: 2.0;

width: 100%;
max-width: none;
&quot;&gt;
&lt;b&gt;Sobre Mim:&lt;br&gt;
Vallécia Janikelly, 17 anos, sou uma estudante 
de informática que está cursando o curso técnico
integrado em informática no IFPB - Campus itabaiana

&lt;/div&gt;
&quot;&quot;&quot;, unsafe_allow_html=True)

st.markdown(&quot;&lt;div style=&#39;margin-top:30px;&#39;&gt;&quot;, unsafe_allow_html=True)
st.link_button(&quot;Acessar&quot;, &quot;http://lattes.cnpq.br/4494611683890258&quot;)
st.markdown(&quot;&lt;/div&gt;&quot;, unsafe_allow_html=True)

with col_right:
st.empty()

# �� NOVO BLOCO (WhatsApp clicável no final)
st.markdown(f&quot;&quot;&quot;
&lt;div style=&quot;text-align: center; margin-top: 10px;&quot;&gt;
&lt;a href=&quot;https://web.whatsapp.com/&quot; target=&quot;_blank&quot;&gt;
&lt;img src=&quot;whats.jpg;base64,{zap_base64}&quot; width=&quot;100&quot;&gt;
&lt;/a&gt;
&lt;/div&gt;
&quot;&quot;&quot;, unsafe_allow_html=True)
