import streamlit as st

# =========================================================================
# BLOCO 1: CONFIGURAÇÕES E BANCO DE DADOS (Com novas perguntas e imagens)
# =========================================================================
st.set_page_config(page_title="Quiz Bíblico Interativo", page_icon="📝", layout="centered")

perguntas_biblicas = [
    {
        "pergunta": "Quem foi o homem mais velho mencionado na Bíblia?",
        "opcoes": ["Matusalém", "Noé", "Adão", "Abraão"],
        "correta": "Matusalém",
        "curiosidade": "Matusalém viveu por 969 anos (Gênesis 5:27).",
        "imagem": "https://unsplash.com" # Foto representativa de ancião
    },
    {
        "pergunta": "Qual foi o primeiro milagre público realizado por Jesus?",
        "opcoes": ["Multiplicação dos pães", "Caminhar sobre as águas", "Transformação de água em vinho", "Ressurreição de Lázaro"],
        "correta": "Transformação de água em vinho",
        "curiosidade": "Este milagre aconteceu durante uma festa de casamento em Caná da Galileia (João 2:1-11).",
        "imagem": "https://unsplash.com" # Foto de taças de vinho
    },
    {
        "pergunta": "Quantos livros tem a Bíblia Protestante / Evangélica completa?",
        "opcoes": ["73 livros", "66 livros", "50 livros", "12 livros"],
        "correta": "66 livros",
        "curiosidade": "A Bíblia é dividida em 39 livros no Velho Testamento e 27 no Novo Testamento.",
        "imagem": "https://unsplash.com" # Foto de livro aberto
    },
    {
        "pergunta": "Quem liderou o povo de Israel na travessia do Mar Vermelho?",
        "opcoes": ["Josué", "Davi", "Moisés", "Arão"],
        "correta": "Moisés",
        "curiosidade": "Esse evento histórico e milagroso está registrado no livro de Êxodo, capítulo 14.",
        "imagem": "https://unsplash.com" # Foto de mar
    },
    # --- NOVAS PERGUNTAS ADICIONADAS ---
    {
        "pergunta": "Qual animal conversou com Balaão no caminho?",
        "opcoes": ["Um leão", "Uma jumenta", "Uma ovelha", "Uma pomba"],
        "correta": "Uma jumenta",
        "curiosidade": "Deus abriu a boca da jumenta para repreender a loucura do profeta (Números 22:28).",
        "imagem": "https://unsplash.com" # Foto de animal no campo
    },
    {
        "pergunta": "O que caiu do céu para alimentar o povo de Israel no deserto?",
        "opcoes": ["Maná", "Trigo", "Pão sírio", "Frutos dourados"],
        "correta": "Maná",
        "curiosidade": "O maná parecia semente de coentro e tinha gosto de bolo de mel (Êxodo 16:31).",
        "imagem": "https://unsplash.com" # Foto de alimento/pão
    },
    {
        "pergunta": "Quem foi jogado na cova dos leões por não deixar de orar a Deus?",
        "opcoes": ["Sansão", "Daniel", "Ezequiel", "Elias"],
        "correta": "Daniel",
        "curiosidade": "Deus enviou o seu anjo e fechou a boca dos leões para que não fizessem mal a Daniel (Daniel 6:22).",
        "imagem": "https://unsplash.com" # Foto de um leão
    },
    {
        "pergunta": "O que Noé soltou para saber se as águas do dilúvio tinham secado?",
        "opcoes": ["Uma águia", "Um gavião", "Uma pomba", "Um pardal"],
        "correta": "Uma pomba",
        "curiosidade": "A pomba retornou na segunda vez trazendo uma folha de oliveira no bico (Gênesis 8:11).",
        "imagem": "https://unsplash.com" # Foto de pomba branca voando
    }
]

if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = 0
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0

# =========================================================================
# BLOCO 2: DESIGN VISUAL E BARRA DE PROGRESSO
# =========================================================================
st.title("⛪ Gincana & Quiz Bíblico")
st.markdown("##### *'Lâmpada para os meus pés é tua palavra e luz para o meu caminho.' — Salmo 119:105*")
st.divider()

if st.session_state.pergunta_atual < len(perguntas_biblicas):
    progresso_porcentagem = (st.session_state.pergunta_atual) / len(perguntas_biblicas)
    st.progress(progresso_porcentagem, text=f"Progresso da Gincana: {int(progresso_porcentagem * 100)}%")
else:
    st.progress(1.0, text="Gincana Concluída! 🎉")

# =========================================================================
# BLOCO 3: FUNCIONAMENTO DO JOGO (Sistema de perguntas com exibição de imagem)
# =========================================================================
if st.session_state.pergunta_atual < len(perguntas_biblicas):
    dados_pergunta = perguntas_biblicas[st.session_state.pergunta_atual]
    
    st.caption(f"Pergunta {st.session_state.pergunta_atual + 1} de {len(perguntas_biblicas)}")
    st.subheader(dados_pergunta["pergunta"])
    
    # MOSTRA A IMAGEM ILUSTRATIVA DA PERGUNTA ATUAL [1]
    if "imagem" in dados_pergunta:
        st.image(dados_pergunta["imagem"], use_container_width=True) [1]
    
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
