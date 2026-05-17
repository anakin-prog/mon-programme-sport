import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mon Coach Poids de Corps", page_icon="💪", layout="centered")

st.title("💪 Mon Programme Renforcement")
st.write("Suivez vos séances et cochez vos exercices au fil de l'entraînement.")

# Sélection de la séance
seance = st.selectbox(
    "Quelle séance faites-vous aujourd'hui ?",
    ("Séance A : Force & Endurance Musculaire", "Séance B : Gainage & Cardio-Trunk")
)

st.divider()

if seance == "Séance A : Force & Endurance Musculaire":
    st.subheader("🏋️‍♂️ Séance A — Objectif : Force")
    st.info("Structure : 3 à 4 tours. Prenez 15s de repos entre les exercices, et 1 min à la fin de chaque tour.")
    
    # Exercices de la séance A
    st.checkbox("1. Squats au poids du corps (20 réps) — *Cuisses & Fessiers*")
    st.checkbox("2. Pompes / Push-ups (10 à 15 réps) — *Pectoraux & Triceps*")
    st.checkbox("3. Fentes alternées (20 réps au total) — *Équilibre & Quadriceps*")
    st.checkbox("4. Dips entre deux chaises (10 à 12 réps) — *Triceps*")
    st.checkbox("5. Superman alterné (12 réps - bloquer 2s en haut) — *Bas du dos*")

else:
    st.subheader("⏱ Séance B — Objectif : Gainage & Cardio")
    st.info("Structure : 3 à 4 tours. Travaillez au temps (chrono Garmin). 15s de repos entre les exercices, 1 min en fin de tour.")
    
    # Exercices de la séance B
    st.checkbox("1. Mountain Climbers (45 secondes) — *Cardio & Tronc*")
    st.checkbox("2. La Planche / Plank (45 secondes) — *Stabilité abdominale*")
    st.checkbox("3. Le Pont / Bridge (20 réps) — *Ischios & Fessiers*")
    st.checkbox("4. Russian Twist (40 secondes) — *Obliques & Taille*")
    st.checkbox("5. Abdominaux / Sit-ups (15 réps) — *Grand droit*")
# --- SÉANCE C (NOUVELLE SÉANCE) ---
else:
    st.subheader("💪 Séance C — Full Body avec Haltères")
    st.info("Structure Classique : Faites les 4 séries d'un exercice avant de passer au suivant. Prenez 1 minute de repos entre chaque série.")
    
    # Exercices de la séance C (Option 1 de l'image)
    with st.expander("1. Squats (4 séries x 12 réps)", expanded=True):
        st.write("*Cible : Cuisses et Fessiers*")
        st.checkbox("Série 1 fait", key="c_sq1")
        st.checkbox("Série 2 fait", key="c_sq2")
        st.checkbox("Série 3 fait", key="c_sq3")
        st.checkbox("Série 4 fait", key="c_sq4")
        
    with st.expander("2. Lunges / Fentes (4 séries x 15 réps)", expanded=True):
        st.write("*Cible : Cuisses et Équilibre*")
        st.checkbox("Série 1 fait", key="c_lu1")
        st.checkbox("Série 2 fait", key="c_lu2")
        st.checkbox("Série 3 fait", key="c_lu3")
        st.checkbox("Série 4 fait", key="c_lu4")

    with st.expander("3. Deadlift / Soulevé de terre (4 séries x 8 réps)", expanded=True):
        st.write("*Cible : Ischios-jambiers et Bas du dos (Charnière de hanche)*")
        st.checkbox("Série 1 fait", key="c_dl1")
        st.checkbox("Série 2 fait", key="c_dl2")
        st.checkbox("Série 3 fait", key="c_dl3")
        st.checkbox("Série 4 fait", key="c_dl4")

    with st.expander("4. Row / Tirage buste penché (4 séries x 10 réps)", expanded=True):
        st.write("*Cible : Muscle grand dorsal et milieu du dos*")
        st.checkbox("Série 1 fait", key="c_rw1")
        st.checkbox("Série 2 fait", key="c_rw2")
        st.checkbox("Série 3 fait", key="c_rw3")
        st.checkbox("Série 4 fait", key="c_rw4")

    with st.expander("5. Shoulder Press / Développé épaules (4 séries x 10 réps)", expanded=True):
        st.write("*Cible : Épaules (Deltoïdes)*")
        st.checkbox("Série 1 fait", key="c_sp1")
        st.checkbox("Série 2 fait", key="c_sp2")
        st.checkbox("Série 3 fait", key="c_sp3")
        st.checkbox("Série 4 fait", key="c_sp4")

    with st.expander("6. Lateral Raises / Élévations latérales (4 séries x 12 réps)", expanded=True):
        st.write("*Cible : Côtés des épaules (Largeur)*")
        st.checkbox("Série 1 fait", key="c_lr1")
        st.checkbox("Série 2 fait", key="c_lr2")
        st.checkbox("Série 3 fait", key="c_lr3")
        st.checkbox("Série 4 fait", key="c_lr4")

    with st.expander("7. Skull Crusher / Barre au front haltères (4 séries x 10 réps)", expanded=True):
        st.write("*Cible : Arrière des bras (Triceps)*")
        st.checkbox("Série 1 fait", key="c_sc1")
        st.checkbox("Série 2 fait", key="c_sc2")
        st.checkbox("Série 3 fait", key="c_sc3")
        st.checkbox("Série 4 fait", key="c_sc4")

    with st.expander("8. Biceps Curl (4 séries x 12 réps)", expanded=True):
        st.write("*Cible : Avant des bras (Biceps)*")
        st.checkbox("Série 1 fait", key="c_bc1")
        st.checkbox("Série 2 fait", key="c_bc2")
        st.checkbox("Série 3 fait", key="c_bc3")
        st.checkbox("Série 4 fait", key="c_bc4")
st.divider()

# Section Conseils de progression
with st.expander("💡 Conseils de progression et posture"):
    st.markdown("""
    - **La forme avant tout :** Une répétition lente et parfaitement exécutée est 100x plus efficace qu'un mouvement bâclé.
    - **Progression :** Si cela devient trop facile, ralentissez la phase de descente (ex: 3 secondes pour descendre sur un squat).
    - **Régularité :** Vos séances sont calées chaque lundi, mercredi et vendredi à 17h30 dans votre agenda !
    """)
