import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Quiz Bíblico Interativo", page_icon="📝", layout="centered")

# =========================================================================
# BANCO DE DADOS DE PERGUNTAS (Tudo junto no mesmo arquivo agora!)
# =========================================================================
lista_perguntas = [
    {"pergunta": "Quem foi o homem mais velho mencionado na Bíblia?", "opcoes": ["Matusalém", "Noé", "Adão", "Abraão"], "correta": "Matusalém", "curiosidade": "Matusalém viveu por 969 anos (Gênesis 5:27)."},
    {"pergunta": "Qual foi o primeiro milagre público realizado por Jesus?", "opcoes": ["Multiplicação dos pães", "Caminhar sobre as águas", "Transformação de água em vinho", "Ressurreição de Lázaro"], "correta": "Transformação de água em vinho", "curiosidade": "Ocorreu em Caná da Galileia (João 2:1-11)."},
    {"pergunta": "Quantos livros tem a Bíblia Protestante / Evangélica completa?", "opcoes": ["73 livros", "66 livros", "50 livros", "12 livros"], "correta": "66 livros", "curiosidade": "São 39 no Velho Testamento e 27 no Novo Testamento."},
    {"pergunta": "Quem liderou o povo de Israel na travessia do Mar Vermelho?", "opcoes": ["Josué", "Davi", "Moisés", "Arão"], "correta": "Moisés", "curiosidade": "Esse evento está registrado em Êxodo 14."},
    {"pergunta": "Qual animal conversou com Balaão no caminho?", "opcoes": ["Um leão", "Uma jumenta", "Uma ovelha", "Uma pomba"], "correta": "Uma jumenta", "curiosidade": "Deus abriu a boca da jumenta (Números 22:28)."},
    {"pergunta": "O que caiu do céu para alimentar o povo no deserto?", "opcoes": ["Maná", "Trigo", "Pão sírio", "Frutos"], "correta": "Maná", "curiosidade": "Tinha gosto de bolo de mel (Êxodo 16:31)."},
    {"pergunta": "Quem foi jogado na cova dos leões por não deixar de orar?", "opcoes": ["Sansão", "Daniel", "Ezequiel", "Elias"], "correta": "Daniel", "curiosidade": "Deus enviou um anjo e fechou a boca dos leões (Daniel 6:22)."},
    {"pergunta": "O que Noé soltou para saber se as águas do dilúvio tinham secado?", "opcoes": ["Uma águia", "Um gavião", "Uma pomba", "Um pardal"], "correta": "Uma pomba", "curiosidade": "A pomba voltou com uma folha de oliveira (Gênesis 8:11)."},
    {"pergunta": "Quem foi vendido por seus irmãos como escravo para o Egito?", "opcoes": ["Benjamim", "José", "Rúben", "Levi"], "correta": "José", "curiosidade": "Gênesis 37:28."},
    {"pergunta": "Qual o menor livro do Velho Testamento?", "opcoes": ["Obadias", "Ageu", "Malaquias", "Naum"], "correta": "Obadias", "curiosidade": "Possui apenas um capítulo com 21 versículos."},
    {"pergunta": "Quantos discípulos Jesus escolheu inicialmente?", "opcoes": ["7", "10", "12", "70"], "correta": "12", "curiosidade": "Mateus 10:1-4."},
    {"pergunta": "Quem derrotou o gigante Golias com uma funda e uma pedra?", "opcoes": ["Saul", "Salomão", "Davi", "Sansão"], "correta": "Davi", "curiosidade": "1 Samuel 17:49."},
    {"pergunta": "De onde veio a força extraordinária de Sansão?", "opcoes": ["Do seu cabelo longo", "Do Espírito do Senhor", "De uma poção", "Da sua espada"], "correta": "Do Espírito do Senhor", "curiosidade": "O voto de nazireado proibia cortar o cabelo, mas a força vinha de Deus (Juízes 14:6)."},
    {"pergunta": "Qual apóstolo negou Jesus três vezes antes do galo cantar?", "opcoes": ["João", "Tiago", "Pedro", "Judas"], "correta": "Pedro", "curiosidade": "Mateus 26:75."},
    {"pergunta": "Qual é o primeiro livro do Novo Testamento?", "opcoes": ["Gênesis", "Mateus", "Marcos", "Apocalipse"], "correta": "Mateus", "curiosidade": "O Evangelho segundo Mateus abre o Novo Testamento."},
    {"pergunta": "Quem escreveu a maioria das cartas (epístolas) do Novo Testamento?", "opcoes": ["Pedro", "João", "Paulo", "Lucas"], "correta": "Paulo", "curiosidade": "Paulo escreveu 13 cartas confirmadas."},
    {"pergunta": "Como se chama o último livro da Bíblia?", "opcoes": ["Malaquias", "Apocalipse", "Judas", "Hebreus"], "correta": "Apocalipse", "curiosidade": "Significa 'Revelação'."},
    {"pergunta": "Em qual cidade Jesus nasceu?", "opcoes": ["Nazaré", "Jerusalém", "Belém", "Cafarnaum"], "correta": "Belém", "curiosidade": "Conforme profetizado em Miqueias 5:2 e cumprido em Mateus 2:1."},
    {"pergunta": "Qual discípulo traiu Jesus por 30 moedas de prata?", "opcoes": ["Tomé", "Judas Iscariotes", "Simão", "Filipe"], "correta": "Judas Iscariotes", "curiosidade": "Mateus 26:15."},
    {"pergunta": "Quem foi a esposa de Abraão e mãe de Isaque?", "opcoes": ["Sara", "Rebeca", "Raquel", "Lia"], "correta": "Sara", "curiosidade": "Ela deu à luz na velhice (Gênesis 21:2)."},
    {"pergunta": "Por quantos dias e noites choveu durante o Dilúvio de Noé?", "opcoes": ["7 dias", "40 dias", "100 dias", "1 ano"], "correta": "40 dias", "curiosidade": "Gênesis 7:12."},
    {"pergunta": "Quem pediu a cabeça de João Batista num prato?", "opcoes": ["Filha de Herodias", "Rainha Ester", "Dalila", "Jezabel"], "correta": "Filha de Herodias", "curiosidade": "Mateus 14:8."},
    {"pergunta": "Qual homem foi ressuscitado por Jesus após estar morto por 4 dias?", "opcoes": ["Lázaro", "Jairo", "Estêvão", "Eutíco"], "correta": "Lázaro", "curiosidade": "Ocorreu em Betânia (João 11:43-44)."},
    {"pergunta": "Quem foi o primeiro rei de Israel?", "opcoes": ["Davi", "Saul", "Salomão", "Ezequias"], "correta": "Saul", "curiosidade": "1 Samuel 10:1."},
    {"pergunta": "Qual o livro mais longo da Bíblia?", "opcoes": ["Gênesis", "Salmos", "Isaías", "Jeremias"], "correta": "Salmos", "curiosidade": "Contém 150 capítulos (cânticos/poemas)."}
]

# Inicia as variáveis do jogo se elas não existirem
if "perguntas_sorteadas" not in st.session_state:
    # Sorteia 15 perguntas aleatórias da lista para cada partida
    st.session_state.perguntas_sorteadas = random.sample(lista_perguntas, k=min(15, len(lista_perguntas)))
    st.session_state.pergunta_atual = 0
    st.session_state.pontuacao = 0

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
# MOTOR DO JOGO
# =========================================================================
if st.session_state.pergunta_atual < len(perguntas_partida):
    dados_pergunta = perguntas_partida[st.session_state.pergunta_atual]
    
    st.caption(f"Pergunta {st.session_state.pergunta_atual + 1} de {len(perguntas_partida)}")
    st.subheader(dados_pergunta["pergunta"])
    
    with st.form(key=f"form_pergunta_{st.session_state.pergunta_atual}"):
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
        del st.session_state.perguntas_sorteadas
        st.session_state.pergunta_atual = 0
        st.session_state.pontuacao = 0
        st.rerun()

st.divider()
st.caption("ANÚNCIO: Fortaleça seu ministério conhecendo as ferramentas dos nossos parceiros abaixo.")
