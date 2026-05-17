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

st.divider()

# Section Conseils de progression
with st.expander("💡 Conseils de progression et posture"):
    st.markdown("""
    - **La forme avant tout :** Une répétition lente et parfaitement exécutée est 100x plus efficace qu'un mouvement bâclé.
    - **Progression :** Si cela devient trop facile, ralentissez la phase de descente (ex: 3 secondes pour descendre sur un squat).
    - **Régularité :** Vos séances sont calées chaque lundi, mercredi et vendredi à 17h30 dans votre agenda !
    """)