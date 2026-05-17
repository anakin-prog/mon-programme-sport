import streamlit as st

# Configuration pour le Pixel 6
st.set_page_config(page_title="Coach Pixel 6 - Sport", page_icon="🔥", layout="centered")

st.title("💪 Mon Programme Renforcement")
st.write("Cochez vos exercices au fil de l'entraînement.")

# Sélection de la séance
seance = st.selectbox(
    "Quelle séance faites-vous aujourd'hui ?",
    (
        "Séance A : Force (Poids du corps)",
        "Séance B : Gainage & Cardio (Poids du corps)",
        "Séance C : Full Body (Haltères)",
        "Séance D : Focus Abdominaux"
    )
)

st.divider()

# --- SÉANCES A, B, C (Logique conservée) ---
if "Séance A" in seance:
    st.subheader("🏋️‍♂️ Séance A — Force & Endurance")
    st.info("3-4 tours. 15s de repos entre exercices.")
    for ex in ["Squats (20r)", "Pompes (10-15r)", "Fentes (20r)", "Dips (10-12r)", "Superman (12r)"]:
        st.checkbox(ex)

elif "Séance B" in seance:
    st.subheader("⏱ Séance B — Gainage & Cardio")
    st.info("Travail au temps (Garmin). 15s de repos.")
    for ex in ["Mountain Climbers (45s)", "Planche (45s)", "Le Pont (20r)", "Russian Twist (40s)", "Sit-ups (15r)"]:
        st.checkbox(ex)

elif "Séance C" in seance:
    st.subheader("💪 Séance C — Haltères Full Body")
    st.info("4 séries par exercice. 1 min de repos.")
    exos_c = ["Squats (12r)", "Fentes (15r)", "Deadlift (8r)", "Row (10r)", "Shoulder Press (10r)", "Lateral Raises (12r)", "Skull Crusher (10r)", "Biceps Curl (12r)"]
    for exo in exos_c:
        with st.expander(exo):
            for i in range(1, 5): st.checkbox(f"Série {i}", key=f"c_{exo}_{i}")

# --- SÉANCE D : ABDOMINAUX AVEC IMAGES CORRESPONDANTES ---
else:
    st.subheader("🎯 Séance D — Focus Abdominaux")
    st.info("Objectif : 3 tours. 20-60s de repos entre les séries.")

    # Liste structurée : (Titre, Description, Nom de l'image sur GitHub)
    exercices_abs = [
        ("1. Crunches (15-20 réps)", "Cible : Haut des abdos", "1_crunches_fr.jpg"),
        ("2. Leg Raises (12-15 réps)", "Cible : Bas des abdos :Allongez-vous, levez les jambes et descendez-les avec contrôle.", "2_leg-raises.jpg"),
        ("3. Bicycle Crunches (20 réps)", "Cible : Obliques & Coordination : Touchez le genou opposé avec le coude (mouvement de vélo)", "3_bicycle_crunches.jpg"),
        ("4. Reverse Crunches (12-15 réps)", "Cible : Bas des abdos : Décollez les hanches et ramenez les genoux vers la poitrine.", "4_reverse_crunches.jpg"),
        ("5. Plank (30-60 secondes)", "Cible : Gainage profond : Corps droit, contractez les abdos et restez immobile.", "5_panches.jpg"),
        ("6. Russian Twists (20 réps)", "Cible : Obliques & Taille : Rotation du buste de gauche à droite, abdos serrés.", "6_russian_twists.jpg"),
        ("7. Mountain Climbers (30-45 sec)", "Cible : Cardio & Core : Ramenez les genoux rapidement vers la poitrine.", "7_mountain_climbers.jpg")
    ]

    for titre, desc, img_nom in exercices_abs:
        # On ouvre l'expander par défaut pour le premier exercice
        est_ouvert = True if "1." in titre else False

        with st.expander(titre, expanded=est_ouvert):
            st.write(f"*{desc}*")

            # Affichage de l'image correspondante
            try:
                st.image(img_nom, use_container_width=True)
            except:
                st.warning(f"Image {img_nom} non trouvée sur GitHub.")

            # Cases à cocher pour les 3 séries
            col1, col2, col3 = st.columns(3)
            with col1: st.checkbox("S1", key=f"d_{img_nom}_1")
            with col2: st.checkbox("S2", key=f"d_{img_nom}_2")
            with col3: st.checkbox("S3", key=f"d_{img_nom}_3")

st.divider()
st.write("💡 *Astuce : Gardez le dos bien plaqué au sol sur les exercices de battements.*")
