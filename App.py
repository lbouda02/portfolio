import streamlit as st #framework pour créer des applications web interactives en Python
import os
from typing import List, Optional #Importation de types pour l'annotation de fonctions : List pour les listes, Optional pour indiquer qu'une valeur peut être None
from upstash_vector import Index #gérer l'index de vecteurs pour la recherche sémantique
# Agent : un agent intelligent
# Runner : pour exécuter des agents
# function_tool :utilitaire pour créer des outils/fonctions que l'agent peut utiliser
from agents import Agent, Runner, function_tool
#charger les variables d'environnement depuis un fichier .env
from dotenv import load_dotenv

# --- INITIALISATION ---
load_dotenv()

# Configuration de la page titre et icône
st.set_page_config(page_title="Portfolio IA - BoudaudLucas", page_icon="🄻🅄🄲🄰🅂") #icone récupérée sur https://fr.piliapp.com/symbol/

# Connexion à l'index Upstash Vector à partir des variables d'environnement
try:
    index: Index = Index.from_env()  # Crée l'instance de l'index pour la recherche vectorielle
except Exception as e:
    st.error(f"Erreur de configuration Upstash : {e}")  # Affiche une erreur si la connexion échoue
    st.stop()  # Arrête l'application Streamlit si l'index n'est pas accessible



# --- TÂCHE 5 : CONNEXION AGENT ↔ VECTEURS (RAG TOOL) --- "Retrieval/Augmented Generation"

# Définition d'une fonction outil que l'agent peut utiliser pour consulter le portfolio
@function_tool
def consulter_portfolio(query: str) -> str:
    """
    Interroge la base de données vectorielle Upstash pour obtenir le contexte du portfolio.

    Args:
        query (str): La question de l'utilisateur transformée en requête de recherche.

    Returns:
        str: Le contenu textuel récupéré pour alimenter la réponse de l'agent.
    """
    # Recherche des 3 résultats les plus pertinents dans l'index vectoriel
    results = index.query(
        data=query, # La requête de recherche
        top_k=3, # on limite à 3 résultats pour éviter de surcharger la réponse
        include_metadata=True  # Inclut les métadonnées associées aux vecteurs
    )
    
    # Création d'une liste de textes extraits depuis les métadonnées des résultats de la recherche
    extracted_text: List[str] = [
        # Pour chaque résultat dans la liste 'results'
        res.metadata.get("text", "")  # récupère la valeur associée à la clé "text" dans les métadonnées
                                   # si la clé n'existe pas, renvoie une chaîne vide ""
        for res in results                 # itération sur tous les résultats renvoyés par l'index
        if res.metadata                     # ne garde que les résultats qui ont des métadonnées définies
    ]
    
    # Retourne le texte combiné ou un message si aucun résultat n'est trouvé
    return "\n\n".join(extracted_text) if extracted_text else "Aucune donnée trouvée."


# --- TÂCHE 4 : CRÉATION DE L'AGENT IA ---

# qui est le modèle 'nano' officiel d'OpenAI.
NANO_MODEL_ID: str = "gpt-4.1-nano" 

AGENT_INSTRUCTIONS: str = (
    "You are an assistant for question-answering tasks. Use the following pieces of "
    "retrieved context to answer the question. If you don't know the answer, "
    "just say that you don't know. be verbose and detailed in your answers. "
    "Réponds en français si la question est en français."
)

# Création de l'agent IA qui répondra aux questions sur le portfolio
mon_agent: Agent = Agent(
    name="Nano-Portfolio-Agent",           # Nom de l'agent, utilisé pour l'identifier dans les logs ou l'interface
    model=NANO_MODEL_ID,                   # Modèle de génération utilisé (GPT-4.1 Nano)
    instructions=AGENT_INSTRUCTIONS,      # Instructions guidant le comportement et le style de réponse de l'agent
    tools=[consulter_portfolio]            # Liste d'outils/fonctions que l'agent peut utiliser pour récupérer des informations
)


# --- TÂCHE 6 : INTERFACE UTILISATEUR (STREAMLIT) ---

def main() -> None:
    """
    Lance l'interface de chat Streamlit et gère l'interaction avec l'agent Nano.
    """
    st.title("⚡ Assistant Portfolio (Boudaud Lucas)")  # Titre de l'application

    # Initialisation de l'historique des messages dans la session si inexistant
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage de tous les messages précédemment échangés dans le chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):  # rôle 'user' ou 'assistant' pour le style du message
            st.markdown(message["content"])     # affichage du contenu du message

    # Champ de saisie utilisateur
    if prompt := st.chat_input("Ex: Parle-moi du projet OAT..."):
        # Sauvegarde du message utilisateur dans l'historique
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)  # Affichage immédiat du message de l'utilisateur

        # Bloc pour la réponse de l'agent
        with st.chat_message("assistant"):
            try:
                # Exécution du RAG : récupère le contexte et génère la réponse
                result = Runner.run_sync(mon_agent, prompt)
                response_text: str = result.final_output  # Récupération du texte final de l'agent

                st.markdown(response_text)  # Affiche la réponse dans le chat
                # Sauvegarde de la réponse de l'agent dans l'historique
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                # Gestion des erreurs si le modèle n'est pas accessible
                st.error(f"Erreur d'accès au modèle '{NANO_MODEL_ID}' : {e}")

if __name__ == "__main__":
    main()