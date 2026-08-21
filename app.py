import streamlit as st
import random
# Importa a lista de perguntas do outro arquivo
from perguntas import lista_perguntas

# Configuração da página
st.set_page_config(page_title="Quiz Bíblico Interativo", page_icon="📝", layout="centered")

# Inicia as variáveis do jogo se elas não existirem
if "perguntas_sorteadas" not in st.session_state:
    # Sorteia 15 perguntas aleatórias da lista de 100+ para cada partida
    st.session_state.perguntas_sorteadas = random.sample(lista_perguntas, k=min(15, len(lista_perguntas)))
    st.session_state.pergunta_atual = 0
    st.session_state.pontuacao = 0

# Atalho para facilitar a leitura do código
perguntas_partida = st.session_state.perguntas_sorteadas

# =========================================================================
# DESIGN VISUAL E BARRA DE PROGRESSO
# =========================================================================
st.title("⛪ Gincana & Quiz Bíblico")
st.markdown("##### *'Lâmpada para os meus pés é tua palavra e luz para o meu caminho.' — Salmo 119:105*")
st.divider()

if st.session_state.pergunta_atual < len(perguntas_partida):
    progresso_porcentagem = (st.session_state.pergunta_atual) / len(perguntas_partida)
    st.progress(progresso_porcentagem, text=f"Progresso da Gincana: {int(progresso_porcentagem * 100)}%")
else:
    st.progress(1.0, text="Gincana Concluída! 🎉")

# =========================================================================
# SISTEMA DO JOGO ALEATÓRIO
# =========================================================================
if st.session_state.pergunta_atual < len(perguntas_partida):
    dados_pergunta = perguntas_partida[st.session_state.pergunta_atual]
    
    st.caption(f"Pergunta {st.session_state.pergunta_atual + 1} de {len(perguntas_partida)}")
    st.subheader(dados_pergunta["pergunta"])
    
    with st.form(key=f"form_pergunta_{st.session_state.pergunta_atual}"):
        # Mistura as alternativas para não ficarem sempre na mesma ordem
        opcoes_misturadas = dados_pergunta["opcoes"].copy()
        resposta_usuario = st.radio("Escolha a alternativa correta:", opcoes_misturadas)
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
    st.metric(label="Sua Pontuação Final", value=f"{st.session_state.pontuacao} de {len(perguntas_partida)} acertos")
    
    if st.button("🔄 JOGAR NOVAMENTE", use_container_width=True):
        # Limpa o estado para sortear novas perguntas na próxima rodada
        del st.session_state.perguntas_sorteadas
        st.session_state.pergunta_atual = 0
        st.session_state.pontuacao = 0
        st.rerun()

st.divider()
st.caption("ANÚNCIO: Fortaleça seu ministério conhecendo as ferramentas dos nossos parceiros abaixo.")
