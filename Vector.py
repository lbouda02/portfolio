import os
#Base de données vectorielle, UPTASH est une plateforme cloud qui fourni des bdd serverless
from upstash_vector import Index, Vector
#pour découoper les markdowns ( gerer, reperer entetes )
from langchain_text_splitters import MarkdownHeaderTextSplitter

#pour géréer les les secrets et la config hors du code
from dotenv import load_dotenv

# 1. Chargement des clés depuis le fichier .env
load_dotenv()
index = Index.from_env()

# 2. Configuration du découpage (Chunking) par titres
# On garde la structure # pour le projet et ## pour les détails
headers_to_split_on = [
    ("#", "Titre_Projet"),
    # ("##", "Section"),
]

# Crée un splitter Markdown qui découpe le texte selon les titres (#, ##)
# et conserve ces titres comme métadonnées pour chaque section
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

def index_data_folder():
    # Liste qui va contenir tous les vecteurs à envoyer à la base vectorielle
    all_vectors = []

    # Chemin vers le dossier contenant les fichiers Markdown à indexer
    data_directory = "Data"
    
    # Vérifie si le dossier Data existe
    # Si le dossier n'existe pas, on arrête la fonction pour éviter une erreur
    if not os.path.exists(data_directory):
        print(f"Erreur : Le dossier '{data_directory}' est introuvable.")
        return

    # Parcours de tous les fichiers présents dans le dossier Data
    for filename in os.listdir(data_directory):

        # On ne traite que les fichiers Markdown (.md)
        if filename.endswith(".md"):
            # Chemin complet vers le fichier
            file_path = os.path.join(data_directory, filename)
            
            # Message pour suivre l'avancement de l'indexation
            print(f"Indexation de : {filename}...")
            
            # Ouverture du fichier Markdown en lecture (UTF-8 pour éviter les problèmes d'encodage)
            with open(file_path, 'r', encoding='utf-8') as f: #as f = donne un nom au fichier ouvert pour pouvoir l’utiliser
                # Lecture complète du contenu du fichier
                content = f.read()
            
            # Découpage du contenu Markdown en sections logiques
            # basé sur les titres (#, ##, ###, etc.)
            chunks = markdown_splitter.split_text(content)
            
            # Parcours de chaque morceau (chunk) obtenu après le découpage. chunnk --> liste de sections plus petites et cohérentes
            for i, chunk in enumerate(chunks):
                # Création d'un identifiant unique pour chaque vecteur
                # Format : nomDuFichier-indexDuChunk
                vector_id = f"{filename.replace('.md', '')}-{i}"
                
                # Préparation du vecteur à envoyer à la base vectorielle
                # - id : identifiant unique
                # - data : texte du chunk (servira à créer l'embedding = traduction du texte en nombre pour la vectorisation) 
                # - metadata : informations utiles pour le contexte et la recherche
                all_vectors.append(
                    Vector(
                        id=vector_id,
                        data=chunk.page_content,   # <- Prends le texte de ce chunk et stocke-le dans le vecteur pour qu’on puisse le transformer en embedding
                        #metadata d’où vient le texte
                        metadata={      
                            # Nom du fichier source
                            "source": filename,

                            # Texte brut du chunk (utile pour l'affichage)
                            "text": chunk.page_content,

                            # Métadonnées issues du MarkdownHeaderTextSplitter
                            # (ex : title, section, subsection)
                            **chunk.metadata
                        }
                    )
                )

    # Une fois tous les fichiers traités :
    # on envoie les vecteurs vers Upstash uniquement s'il y en a au moins un
    if all_vectors:
        # Insertion / mise à jour des vecteurs dans l'index Upstash
        index.upsert(vectors=all_vectors)

        # Message de succès avec le nombre total de chunks indexés
        print(f"\n✅ Indexation terminée ! {len(all_vectors)} morceaux ajoutés à Upstash.")
    else:
        # Aucun fichier Markdown trouvé dans le dossier Data
        print("Aucun fichier .md trouvé dans le dossier Data.")


    # 5. Envoi vers Upstash
    if all_vectors:
        index.upsert(vectors=all_vectors) #upload/insert
        print(f"\n✅ Indexation terminée ! {len(all_vectors)} morceaux ajoutés à Upstash.")
    else:
        print("Aucun fichier .md trouvé dans le dossier Data.")


#pratique pour lancer la fonction automatiquement quand le script est exécuté directement
if __name__ == "__main__":   #Cette ligne vérifie si le fichier est exécuté directement Si oui → le code à l’intérieur s’exécute
    index_data_folder() #Appelle la fonction qui lit tous les fichiers Markdown, les découpe en chunks, crée les vecteurs et les envoie à Upstash.