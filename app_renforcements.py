import streamlit as st

# Configuration pour le Pixel 6 (on garde le layout centered)
st.set_page_config(page_title="Coach Pixel 6 - Sport", page_icon="🔥", layout="centered")

# --- STYLES CSS PERSONNALISÉS ---
st.markdown("""
<style>
    /* Force les images à s'adapter et centre-les */
    .stImage > img {
        width: 100% !important;
        height: auto !important;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* Centre les titres de séances */
    .stSubheader {
        text-align: center;
        color: #e03131; /* Rouge énergique */
    }

    /* Centre les infos de repos */
    .stAlert {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("💪 Mon Programme Renforcement")
st.write("Suivez votre séance et validez vos séries.")

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

# ==========================================
# --- SÉANCE A : FORCE POIDS DE CORPS ------
# ==========================================
if "Séance A" in seance:
    st.subheader("🏋️‍♂️ Séance A — Force & Endurance")
    st.info("Structure : 3 à 4 tours. Prenez 15s de repos entre exercices et 1 min à la fin de chaque tour.")

    st.markdown("---")

    exercices_a = [
        ("1. Squats (20 réps)", "Cible : Cuisses & Fessiers — Descendez les fesses vers l'arrière, buste droit.", "Squat.jpg"),
        ("2. Pompes / Push-ups (10-15 réps)", "Cible : Pectoraux & Triceps — Corps aligné, descendez la poitrine près du sol.", "pompes.jpg"),
        ("3. Fentes alternées (20 réps au total)", "Cible : Quadriceps & Équilibre — Un grand pas avant, genou arrière frôle le sol.", "fentes.jpg"),
        ("4. Dips (10-12 réps)", "Cible : Triceps — En appui sur le bord d'une chaise, fléchissez les coudes.", "Dips.jpg"),
        ("5. Superman (12 réps)", "Cible : Bas du dos — Allongé sur le ventre, décollez poitrine et jambes simultanément.", "superman.jpg")
    ]

    for titre, desc, img_nom in exercices_a:
        est_ouvert = True if "1." in titre else False
        with st.expander(titre, expanded=est_ouvert):
            st.write(f"👉 *{desc}*")
            try:
                st.image(img_nom, use_container_width=True)
            except FileNotFoundError:
                st.error(f"⚠️ Fichier image non trouvé : {img_nom}")

            st.write("---")
            col1, col2, col3 = st.columns(3)
            with col1: st.checkbox("S1", key=f"a_{img_nom}_1")
            with col2: st.checkbox("S2", key=f"a_{img_nom}_2")
            with col3: st.checkbox("S3", key=f"a_{img_nom}_3")

# ==========================================
# --- SÉANCE B : GAINAGE & CARDIO ---------
# ==========================================
elif "Séance B" in seance:
    st.subheader("⏱ Séance B — Gainage & Cardio")
    st.info("Travail au temps (Garmin). 15s de repos entre exercices.")
    for ex in ["1. Mountain Climbers (45s)", "2. Planche (45s)", "3. Le Pont (20r)", "4. Russian Twist (40s)", "5. Sit-ups (15r)"]:
        st.checkbox(ex, key=f"b_{ex}")

# ==========================================
# --- SÉANCE C : Haut du corps ------
# ==========================================
elif "Séance C" in seance:
    st.subheader("💪 Séance C — Haut du corps")
    st.info("4 séries par exercice. 1 min de repos entre les séries.")

    st.markdown("---")

    # Liste structurée : (Titre, Description, Nom de fichier)
    exercices_c = [
        ("1. Squats (12 réps)", "Cible : Cuisses & Fessiers — Haltères sur les épaules ou le long du corps.", "Squat.jpg"),
        ("2. Pompes / Push-ups (10-15 réps)", "Cible : Pectoraux & Triceps — Corps aligné, descendez la poitrine près du sol.", "pompes.jpg"),
        ("3. Deadlift (8 réps)", "Cible : Chaîne postérieure — Gardez le dos parfaitement droit, basculez les hanches.", "Deadlift.gif"),
        ("4. Row (10 réps)", "Cible : Dos — Buste penché en avant, ramenez les coudes vers le haut.", "Row.jpg"),
        ("5. Shoulder Press (10 réps)", "Cible : Épaules — Développé vertical au-dessus de la tête, assis ou debout.", "Shoulder Press.jpg"),
        ("6. Lateral Raises (12 réps)", "Cible : Épaules (faisceau moyen) — Élevez les bras sur les côtés jusqu'à l'horizontale.", "Lateral Raises.jpg"),
        ("7. Skull Crusher (10 réps)", "Cible : Triceps — Allongé, fléchissez les coudes pour amener les haltères vers les tempes.", "Skullcrusher.jpg"),
        ("8. Biceps Curl (12 réps)", "Cible : Biceps — Flexion des bras sans élan, coudes verrouillés au corps.", "Biceps curl.jpg")
    ]

    # Affichage avec expandeurs et cases à cocher pour 4 séries
    for titre, desc, img_nom in exercices_c:
        est_ouvert = True if "1." in titre else False

        with st.expander(titre, expanded=est_ouvert):
            st.write(f"👉 *{desc}*")
            try:
                st.image(img_nom, use_container_width=True)
            except FileNotFoundError:
                st.error(f"⚠️ Image non trouvée : {img_nom}")

            st.write("---")
            col1, col2, col3, col4 = st.columns(4)
            with col1: st.checkbox("S1", key=f"c_{img_nom}_1")
            with col2: st.checkbox("S2", key=f"c_{img_nom}_2")
            with col3: st.checkbox("S3", key=f"c_{img_nom}_3")
            with col4: st.checkbox("S4", key=f"c_{img_nom}_4")

# ==========================================
# --- SÉANCE D : FOCUS ABDOMINAUX ----------
# ==========================================
else:
    st.subheader("🎯 Séance D — Focus Abdominaux")
    st.info("Objectif : 3 tours. 20-60s de repos entre les séries.")

    exercices_abs = [
        ("1. Crunches (15-20 réps)", "Cible : Haut des abdos", "1_crunches_fr.jpg"),
        ("2. Leg Raises (12-15 réps)", "Cible : Bas des abdos : Allongez-vous, levez les jambes et descendez-les avec contrôle.", "2_leg-raises.jpg"),
        ("3. Bicycle Crunches (20 réps)", "Cible : Obliques & Coordination : Touchez le genou opposé avec le coude", "3_bicycle_crunches.jpg"),
        ("4. Reverse Crunches (12-15 réps)", "Cible : Bas des abdos : Décollez les hanches et ramenez les genoux vers la poitrine.", "4_reverse_crunches.jpg"),
        ("5. Plank (30-60 secondes)", "Cible : Gainage profond : Corps droit, abdos contractés, immobile.", "5_panches.jpg"),
        ("6. Russian Twists (20 réps)", "Cible : Obliques & Taille : Rotation buste gauche/droite, abdos serrés.", "6_russian_twists.jpg"),
        ("7. Mountain Climbers (30-45 sec)", "Cible : Cardio & Core : Ramenez les genoux rapidement vers la poitrine.", "7_mountain_climbers.jpg")
    ]

    for titre, desc, img_nom in exercices_abs:
        est_ouvert = True if "1." in titre else False
        with st.expander(titre, expanded=est_ouvert):
            st.write(f"👉 *{desc}*")
            try:
                st.image(img_nom, use_container_width=True)
            except FileNotFoundError:
                st.error(f"⚠️ Image non trouvée : {img_nom}")

            st.write("---")
            col1, col2, col3 = st.columns(3)
            with col1: st.checkbox("S1", key=f"d_{img_nom}_1")
            with col2: st.checkbox("S2", key=f"d_{img_nom}_2")
            with col3: st.checkbox("S3", key=f"d_{img_nom}_3")

# --- ZONE DE FINALISATION DU TOUR ---
st.divider()
st.markdown("### 🏁 Tour Terminé ?")
if st.button("Valider la fin du tour", key="fin_tour"):
    st.balloons()
    st.success("Super boulot ! Prenez 1 min de repos complet avant de relancer le tour suivant !")
    st.write("---")

# --- PIED DE PAGE (FOOTER) ---
st.write("---")
st.markdown("<p style='text-align: center; color: grey;'>v1.3 | Gardez la posture avant la répétition !</p>", unsafe_allow_html=True)
