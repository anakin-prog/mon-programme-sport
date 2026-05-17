import streamlit as st

# Configuration de la page pour un affichage optimal sur smartphone (Pixel 6)
st.set_page_config(page_title="Mon Coach Sport", page_icon="💪", layout="centered")

st.title("💪 Mon Programme Renforcement")
st.write("Suivez vos séances et cochez vos exercices au fil de l'entraînement.")

# Sélection de la séance parmi les 4 options disponibles
seance = st.selectbox(
    "Quelle séance faites-vous aujourd'hui ?",
    (
        "Séance A : Force & Endurance Musculaire (Poids du corps)", 
        "Séance B : Gainage & Cardio-Trunk (Poids du corps)",
        "Séance C : Renforcement Full Body (Haltères)",
        "Séance D : Focus Abdominaux"
    )
)

st.divider()

# ==========================================
# --- SÉANCE A : FORCE POIDS DE CORPS ------
# ==========================================
if "Séance A" in seance:
    st.subheader("🏋️‍♂️ Séance A — Objectif : Force & Endurance")
    st.info("Structure : 3 à 4 tours. Prenez 15s de repos entre les exercices, et 1 min à la fin de chaque tour.")
    
    st.checkbox("1. Squats au poids du corps (20 réps) — *Cuisses & Fessiers*")
    st.checkbox("2. Pompes / Push-ups (10 à 15 réps) — *Pectoraux & Triceps*")
    st.checkbox("3. Fentes alternées (20 réps au total) — *Équilibre & Quadriceps*")
    st.checkbox("4. Dips entre deux chaises (10 à 12 réps) — *Triceps*")
    st.checkbox("5. Superman alterné (12 réps - bloquer 2s en haut) — *Bas du dos*")

# ==========================================
# --- SÉANCE B : GAINAGE & CARDIO ----------
# ==========================================
elif "Séance B" in seance:
    st.subheader("⏱ Séance B — Objectif : Gainage & Cardio")
    st.info("Structure : 3 à 4 tours. Travaillez au temps (chrono Garmin). 15s de repos entre les exercices, 1 min en fin de tour.")
    
    st.checkbox("1. Mountain Climbers (45 secondes) — *Cardio & Tronc*")
    st.checkbox("2. La Planche / Plank (45 secondes) — *Stabilité abdominale*")
    st.checkbox("3. Le Pont / Bridge (20 réps) — *Ischios & Fessiers*")
    st.checkbox("4. Russian Twist (40 secondes) — *Obliques & Taille*")
    st.checkbox("5. Abdominaux / Sit-ups (15 réps) — *Grand droit*")

# ==========================================
# --- SÉANCE C : FULL BODY (HALTÈRES) ------
# ==========================================
elif "Séance C" in seance:
    st.subheader("💪 Séance C — Full Body avec Haltères")
    st.info("Structure Classique : Faites les 4 séries d'un exercice avant de passer au suivant. Prenez 1 minute de repos entre chaque série.")
    
    exos_c = {
        "1. Squats (4 séries x 12 réps)": "Cuisses et Fessiers",
        "2. Lunges / Fentes (4 séries x 15 réps)": "Cuisses et Équilibre",
        "3. Deadlift / Soulevé de terre (4 séries x 8 réps)": "Ischios-jambiers et Bas du dos",
        "4. Row / Tirage buste penché (4 séries x 10 réps)": "Muscle grand dorsal et milieu du dos",
        "5. Shoulder Press / Développé épaules (4 séries x 10 réps)": "Épaules (Deltoïdes)",
        "6. Lateral Raises / Élévations latérales (4 séries x 12 réps)": "Côtés des épaules (Largeur)",
        "7. Skull Crusher / Barre au front haltères (4 séries x 10 réps)": "Arrière des bras (Triceps)",
        "8. Biceps Curl (4 séries x 12 réps)": "Avant des bras (Biceps)"
    }
    
    for nom, desc in exos_c.items():
        with st.expander(nom, expanded=True):
            st.write(f"*{desc}*")
            for i in range(1, 5): 
                st.checkbox(f"Série {i} fait", key=f"c_{nom}_{i}")

# ==========================================
# --- SÉANCE D : FOCUS ABDOMINAUX ---------
# ==========================================
else:
    st.subheader("🎯 Séance D — Focus Abdominaux")
    st.info("Objectif : 3 tours complets. 20-60s de repos entre les séries.")
    
    # 1. Exercice avec l'image hébergée sur GitHub
    with st.expander("1. Crunches (15-20 réps)", expanded=True):
        st.write("*Cible : Grand droit (haut)*")
        
        # Insertion de l'image présente sur votre espace GitHub
        st.image(
            "crunches_fr.jpg", 
            caption="Posture : Relevez le buste et contractez vos abdominaux.",
            use_container_width=True
        )
        
        for i in range(1, 4): 
            st.checkbox(f"Série {i} fait", key=f"d_crunch_{i}")

    # 2. Reste des exercices de la sangle abdominale
    autres_exos_d = {
        "2. Leg Raises (12-15 réps)": "Cible : Bas des abdos",
        "3. Bicycle Crunches (20 réps)": "Cible : Obliques (vélo)",
        "4. Reverse Crunches (12-15 réps)": "Cible : Bas des abdos",
        "5. Plank (30-60 secondes)": "Cible : Gainage profond",
        "6. Russian Twists (20 réps)": "Cible : Obliques & Taille",
        "7. Mountain Climbers (30-45s)": "Cible : Cardio & Core"
    }
    
    for nom, desc in autres_exos_d.items():
        with st.expander(nom):
            st.write(f"*{desc}*")
            for i in range(1, 4): 
                st.checkbox(f"Série {i} fait", key=f"d_{nom}_{i}")

st.divider()

# Section Conseils de progression commune
with st.expander("💡 Conseils de progression et posture"):
    st.markdown("""
    - **La forme avant tout :** Une répétition lente et parfaitement exécutée est 100x plus efficace qu'un mouvement bâclé.
    - **Dos droit :** Gardez une attention particulière sur l'alignement de la colonne lors du *Deadlift* et du *Row*.
    - **Régularité :** Utilisez les rappels de votre agenda pour maintenir vos créneaux d'entraînement !
    """)
