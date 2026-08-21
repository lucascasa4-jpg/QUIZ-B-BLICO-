import streamlit as st

# Configuração inicial da página do site
st.set_page_config(page_title="Quiz Bíblico Interativo", page_icon="📝", layout="centered")

# Banco de dados de perguntas e respostas
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

# Título visual do portal
st.title("📝 Gincana & Quiz Bíblico")
st.write("Teste seus conhecimentos ou use as perguntas na sua célula e classe da EBD!")

st.divider()

# Usar o estado do Streamlit (session_state) para controlar em qual pergunta o usuário está
if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = 0
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0

# Verifica se o jogo ainda está acontecendo ou se chegou ao fim
if st.session_state.pergunta_atual < len(perguntas_biblicas):
    dados_pergunta = perguntas_biblicas[st.session_state.pergunta_atual]
    
    # Exibe o progresso
    st.caption(f"Pergunta {st.session_state.pergunta_atual + 1} de {len(perguntas_biblicas)}")
    st.subheader(dados_pergunta["pergunta"])
    
    # Cria os botões de opção usando um formulário para processar o clique
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
            
    # Botão para avançar para a próxima etapa do jogo
    if st.button("PRÓXIMA PERGUNTA ➡️", use_container_width=True):
        st.session_state.pergunta_atual += 1
        st.rerun() # Atualiza a tela para carregar a nova pergunta

else:
    # Tela final do Quiz mostrando o resultado
    st.balloons()
    st.success("🎉 Parabéns! Você concluiu o Quiz Bíblico.")
    st.metric(label="Sua Pontuação Final", value=f"{st.session_state.pontuacao} de {len(perguntas_biblicas)} acertos")
    
    # Botão para reiniciar o jogo do zero
    if st.button("🔄 JOGAR NOVAMENTE", use_container_width=True):
        st.session_state.pergunta_atual = 0
        st.session_state.pontuacao = 0
        st.rerun()

st.divider()
# Local estratégico para faturamento
st.caption("ANÚNCIO: Fortaleça seu ministério conhecendo as ferramentas dos nossos parceiros abaixo.")
