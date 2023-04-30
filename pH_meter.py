import streamlit as st
import math

def calculate_ph(hydrogen_ion_concentration):
    pH = -1 * (math.log10(hydrogen_ion_concentration))
    return pH

def main():
    st.title("Simple pH Meter")

    st.write("Masukkan konsentrasi ion hidrogen (dalam mol/L):")
    hydrogen_ion_concentration = st.number_input("", min_value=0.0, format="%.4f")

    if st.button("Hitung pH"):
        pH = calculate_ph(hydrogen_ion_concentration)
        st.write(f"pH dari larutan dengan konsentrasi ion hidrogen {hydrogen_ion_concentration} mol/L adalah {pH:.2f}")

        if pH < 7:
            st.write("Larutan termasuk dalam asam")
        elif pH > 7:
            st.write("Larutan termasuk dalam basa")
        else:
            st.write("Larutan bersifat netral")

if __name__ == "__main__":
    main()
