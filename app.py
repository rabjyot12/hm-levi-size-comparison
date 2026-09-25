import streamlit as st

from src.data_analysis import (
    hm_tops,
    levis_tops,
    recommend_size
)

st.title("H&M vs Levi's Size Comparison")

st.write(
    "Compare your body measurement with the published "
    "size ranges of H&M and Levi's."
)

st.subheader("Enter your measurement")

measurement = st.number_input(
    "Chest measurement (cm)",
    min_value=50.0,
    max_value=150.0,
    value=95.0
)

if st.button("Find Size"):

    hm_result = recommend_size(
        hm_tops,
        measurement,
        "chest_min_cm",
        "chest_max_cm"
    )

    levis_result = recommend_size(
        levis_tops,
        measurement,
        "chest_min_cm",
        "chest_max_cm"
    )

    st.subheader("H&M")

    if hm_result["status"] == "exact":

        st.success(
            f"Exact match: {hm_result['size']}"
        )

        st.write(
            f"Published range: "
            f"{hm_result['min_cm']}–{hm_result['max_cm']} cm"
        )

    else:

        st.warning(
            f"No exact match. Closest size: "
            f"{hm_result['size']}"
        )

        st.write(
            f"Published range: "
            f"{hm_result['min_cm']}–{hm_result['max_cm']} cm"
        )

        st.write(
            f"Distance: {hm_result['distance_cm']} cm"
        )


    st.subheader("Levi's")

    if levis_result["status"] == "exact":

        st.success(
            f"Exact match: {levis_result['size']}"
        )

        st.write(
            f"Published range: "
            f"{levis_result['min_cm']}–{levis_result['max_cm']} cm"
        )

    else:

        st.warning(
            f"No exact match. Closest size: "
            f"{levis_result['size']}"
        )

        st.write(
            f"Published range: "
            f"{levis_result['min_cm']}–{levis_result['max_cm']} cm"
        )

        st.write(
            f"Distance: {levis_result['distance_cm']} cm"
        )