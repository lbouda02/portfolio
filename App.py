import streamlit as st
import os
from typing import List, Optional
from upstash_vector import Index
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv

# --- INITIALISATION ---
load_dotenv()

# Configuration de la page
st.set_page_config(page_title="Portfolio IA - BoudaudLucas", page_icon="⚡")

# Connexion à l'index Upstash Vector
try:
    index: Index = Index.from_env()
except Exception as e:
    st.error(f"Erreur de configuration Upstash : {e}")
    st.stop()

# --- TÂCHE 5 : CONNEXION AGENT ↔ VECTEURS (RAG TOOL) ---

@function_tool
def consulter_portfolio(query: str) -> str:
    """
    Interroge la base de données vectorielle Upstash pour obtenir le contexte du portfolio.

    Args:
        query (str): La question de l'utilisateur transformée en requête de recherche.

    Returns:
        str: Le contenu textuel récupéré pour alimenter la réponse de l'agent.
    """
    # Recherche sémantique (Top 3 pour la précision)
    results = index.query(
        data=query,
        top_k=3,
        include_metadata=True
    )
    
    # Transformation des résultats en un bloc de contexte unique
    extracted_text: List[str] = [
        res.metadata.get("text", "") for res in results if res.metadata
    ]
    
    return "\n\n".join(extracted_text) if extracted_text else "Aucune donnée trouvée."

# --- TÂCHE 4 : CRÉATION DE L'AGENT IA ---

# qui est le modèle 'nano' officiel d'OpenAI.
NANO_MODEL_ID: str = "gpt-4.1-nano" 

AGENT_INSTRUCTIONS: str = (
    "Tu es un assistant concis. Utilise le contexte fourni pour répondre. "
    "Si l'info manque, dis-le. 3 phrases maximum. Réponds en français."
)

mon_agent: Agent = Agent(
    name="Nano-Portfolio-Agent",
    model=NANO_MODEL_ID,  # Application du modèle spécifié
    instructions=AGENT_INSTRUCTIONS,
    tools=[consulter_portfolio]
)

# --- TÂCHE 6 : INTERFACE UTILISATEUR (STREAMLIT) ---

def main() -> None:
    """
    Lance l'interface de chat Streamlit et gère l'interaction avec l'agent Nano.
    """
    st.title("⚡ Assistant Portfolio (Boudaud Lucas)")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Posez votre question ici..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # Exécution du cycle RAG via le Runner d'OpenAI-Agents
                result = Runner.run_sync(mon_agent, prompt)
                response_text: str = result.final_output
                
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"Erreur d'accès au modèle '{NANO_MODEL_ID}' : {e}")

if __name__ == "__main__":
    main()