import streamlit as st

# =========================================================================
# BLOCO 1: CONFIGURAÇÕES E BANCO DE DADOS (Não mexer na estrutura)
# =========================================================================
st.set_page_config(page_title="Quiz Bíblico Interativo", page_icon="📝", layout="centered")

perguntas_biblicas = [
    {
        "pergunta": "Quem foi o homem mais velho mencionado na Bíblia?",
        "opcoes": ["Matusalém", "Noé", "Adão", "Abraão"],
        "correta": "Matusalém",
        "curiosidade": "Matusalém viveu por 969 anos (Gênesis 5:27)."
    },
    {
        "pergunta": "Qual foi o primeiro milagre público realizado por Jesus?",
        "opcoes": ["Multiplicação dos pães", "Caminhar sobre as águas", "Transformação de água em vinho", "Ressurreição de Lázaro"],
        "correta": "Transformação de água em vinho",
        "curiosidade": "Este milagre aconteceu durante uma festa de casamento em Caná da Galileia (João 2:1-11)."
    },
    {
        "pergunta": "Quantos livros tem a Bíblia Protestante / Evangélica completa?",
        "opcoes": ["73 livros", "66 livros", "50 livros", "12 livros"],
        "correta": "66 livros",
        "curiosidade": "A Bíblia é dividida em 39 livros no Velho Testamento e 27 no Novo Testamento."
    },
    {
        "pergunta": "Quem liderou o povo de Israel na travessia do Mar Vermelho?",
        "opcoes": ["Josué", "Davi", "Moisés", "Arão"],
        "correta": "Moisés",
        "curiosidade": "Esse evento histórico e milagroso está registrado no livro de Êxodo, capítulo 14."
    }
]

if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = 0
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0


# =========================================================================
# BLOCO 2: NOVO DESIGN VISUAL E BARRA DE PROGRESSO
# =========================================================================
st.title("⛪ Gincana & Quiz Bíblico")
st.markdown("##### *'Lâmpada para os meus pés é tua palavra e luz para o meu caminho.' — Salmo 119:105*")
st.divider()

# Cria a barra carregando no topo do quiz de forma automática
if st.session_state.pergunta_atual < len(perguntas_biblicas):
    progresso_porcentagem = (st.session_state.pergunta_atual) / len(perguntas_biblicas)
    st.progress(progresso_porcentagem, text=f"Progresso da Gincana: {int(progresso_porcentagem * 100)}%")
else:
    st.progress(1.0, text="Gincana Concluída! 🎉")


# =========================================================================
# BLOCO 3: FUNCIONAMENTO DO JOGO (Sistema de perguntas)
# =========================================================================
if st.session_state.pergunta_atual < len(perguntas_biblicas):
    dados_pergunta = perguntas_biblicas[st.session_state.pergunta_atual]
    
    st.caption(f"Pergunta {st.session_state.pergunta_atual + 1} de {len(perguntas_biblicas)}")
    st.subheader(dados_pergunta["pergunta"])
    
    with st.form(key=f"form_pergunta_{st.session_state.pergunta_atual}"):
        resposta_usuario = st.radio("Escolha a alternativa correta:", dados_pergunta["opcoes"])
        enviar = st.form_submit_button("CONFERIR RESPOSTA", type="primary")
        
        if enviar:
            if resposta_usuario == dados_pergunta["correta"]:
                st.success("🎯 Resposta Correta! Glória a Deus!")
                st.session_state.pontuacao += 1
            else:
                st.error(f"❌ Resposta Incorreta. A alternativa certa era: **{dados_pergunta['correta']}**")
            
            st.info(f"📖 **Curiosidade Bíblica:** {dados_pergunta['curiosidade']}")
            
    if st.button("PRÓXIMA PERGUNTA ➡️", use_container_width=True):
        st.session_state.pergunta_atual += 1
        st.rerun()

else:
    st.balloons()
    st.success("🎉 Parabéns! Você concluiu o Quiz Bíblico.")
    st.metric(label="Sua Pontuação Final", value=f"{st.session_state.pontuacao} de {len(perguntas_biblicas)} acertos")
    
    if st.button("🔄 JOGAR NOVAMENTE", use_container_width=True):
        st.session_state.pergunta_atual = 0
        st.session_state.pontuacao = 0
        st.rerun()

st.divider()
st.caption("ANÚNCIO: Fortaleça seu ministério conhecendo as ferramentas dos nossos parceiros abaixo.")
