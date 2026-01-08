import os
from upstash_vector import Index, Vector
from langchain_text_splitters import MarkdownHeaderTextSplitter
from dotenv import load_dotenv

# 1. Chargement des clés depuis le fichier .env
load_dotenv()
index = Index.from_env()

# 2. Configuration du découpage (Chunking) par titres
# On garde la structure # pour le projet et ## pour les détails
headers_to_split_on = [
    ("#", "Titre_Projet"),
    ("##", "Section"),
]
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

def index_data_folder():
    all_vectors = []
    # Chemin vers ton dossier (attention à la majuscule "Data")
    data_directory = "Data"
    
    if not os.path.exists(data_directory):
        print(f"Erreur : Le dossier '{data_directory}' est introuvable.")
        return

    # 3. Parcours des fichiers uniquement dans le dossier Data
    for filename in os.listdir(data_directory):
        if filename.endswith(".md"):
            file_path = os.path.join(data_directory, filename)
            
            print(f"Indexation de : {filename}...")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Découpage du contenu
            chunks = markdown_splitter.split_text(content)
            
            for i, chunk in enumerate(chunks):
                # ID unique : nom_fichier-index
                vector_id = f"{filename.replace('.md', '')}-{i}"
                
                # 4. Préparation du vecteur avec ses métadonnées
                all_vectors.append(
                    Vector(
                        id=vector_id,
                        data=chunk.page_content,
                        metadata={
                            "source": filename,
                            "text": chunk.page_content,
                            **chunk.metadata # Ajoute Titre_Projet et Section
                        }
                    )
                )

    # 5. Envoi vers Upstash
    if all_vectors:
        index.upsert(vectors=all_vectors)
        print(f"\n✅ Indexation terminée ! {len(all_vectors)} morceaux ajoutés à Upstash.")
    else:
        print("Aucun fichier .md trouvé dans le dossier Data.")

if __name__ == "__main__":
    index_data_folder()