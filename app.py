import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="OptoSim Lab", layout="centered")
st.title("🔬 OptoSim Lab — Advanced Optoelectronics Virtual Lab")

st.write("""
Interactive simulations based on **Opto Electronic Theory (FI9071)**  
No datasets • No AI models • Pure physics + math.
""")

section = st.sidebar.selectbox(
    "Choose Experiment",
    [
        "Young's Double Slit — Interference",
        "Single Slit — Diffraction",
        "Polarization (Malus Law)",
        "LED: Bandgap → Wavelength",
        "Laser Threshold Gain",
        "Photodiode I–V Characteristics",
        "Electro-Optic Modulator"
    ]
)

# ---------------------------
# Young's Double Slit
# ---------------------------
if section == "Young's Double Slit — Interference":
    st.header("🌈 Young's Double Slit — Interference Pattern")

    wavelength = st.slider("Wavelength (nm)", 400, 700, 550)
    slit_distance = st.slider("Slit Separation (mm)", 0.1, 2.0, 0.5)
    screen_distance = st.slider("Screen Distance (m)", 0.1, 2.0, 1.0)

    wl = wavelength * 1e-9
    d = slit_distance * 1e-3
    L = screen_distance

    x = np.linspace(-0.01, 0.01, 2000)
    beta = (np.pi * d * x) / (wl * L)
    intensity = (np.cos(beta)) ** 2

    fig, ax = plt.subplots()
    ax.plot(x * 1000, intensity)
    ax.set_xlabel("Position (mm)")
    ax.set_ylabel("Normalized Intensity")
    ax.set_title("Interference Pattern")
    st.pyplot(fig)

    st.info("Bright & dark fringes appear due to constructive and destructive interference.")

# ---------------------------
# Single Slit Diffraction
# ---------------------------
elif section == "Single Slit — Diffraction":
    st.header("🔦 Single Slit Diffraction")

    wavelength = st.slider("Wavelength (nm)", 450, 700, 600)
    slit_width = st.slider("Slit Width (mm)", 0.05, 1.0, 0.2)
    screen_distance = st.slider("Screen Distance (m)", 0.5, 3.0, 1.0)

    wl = wavelength * 1e-9
    a = slit_width * 1e-3
    L = screen_distance

    x = np.linspace(-0.01, 0.01, 2000)
    alpha = (np.pi * a * x) / (wl * L)
    intensity = (np.sin(alpha) / (alpha + 1e-12)) ** 2

    fig, ax = plt.subplots()
    ax.plot(x * 1000, intensity)
    ax.set_xlabel("Position (mm)")
    ax.set_ylabel("Normalized Intensity")
    ax.set_title("Diffraction Pattern")
    st.pyplot(fig)

    st.info("Central maximum is widest — diffraction causes wave spreading.")

# ---------------------------
# Polarization
# ---------------------------
elif section == "Polarization (Malus Law)":
    st.header("🕶 Polarization — Malus' Law")

    angle = st.slider("Angle (degrees)", 0, 180, 45)
    I0 = 1
    theta = np.deg2rad(angle)
    I = I0 * (np.cos(theta)) ** 2

    st.metric("Transmitted Intensity", f"{I:.2f}")
    st.info("I = I0 cos²θ — transmission decreases as angle increases.")

# ---------------------------
# LED Bandgap
# ---------------------------
elif section == "LED: Bandgap → Wavelength":
    st.header("💡 LED Bandgap to Emission Wavelength")

    Eg = st.slider("Bandgap Energy (eV)", 1.2, 3.5, 2.0)

    h = 4.135e-15
    c = 3e8
    wavelength = (h * c) / (Eg * 1.6e-19)
    nm = wavelength * 1e9

    st.metric("Emission Wavelength", f"{nm:.1f} nm")
    st.info("Smaller bandgap → longer wavelength (red). Larger bandgap → blue/violet.")

# ---------------------------
# Laser Threshold Gain
# ---------------------------
elif section == "Laser Threshold Gain":
    st.header("🔺 Laser Threshold Gain Estimator")

    mirror_r1 = st.slider("Mirror 1 Reflectivity", 0.3, 0.99, 0.9)
    mirror_r2 = st.slider("Mirror 2 Reflectivity", 0.3, 0.99, 0.8)
    length = st.slider("Cavity Length (cm)", 0.1, 5.0, 1.0)

    L = length * 1e-2
    g_th = (1 / (2 * L)) * np.log(1 / (mirror_r1 * mirror_r2))

    st.metric("Threshold Gain (1/m)", f"{g_th:.2f}")
    st.info("Laser oscillation starts when gain exceeds optical losses.")

# ---------------------------
# Photodiode IV Curve
# ---------------------------
elif section == "Photodiode I–V Characteristics":
    st.header("📡 Photodiode I–V Characteristics")

    Is = st.slider("Saturation Current (µA)", 0.1, 10.0, 1.0)
    illumination = st.slider("Illumination Current (µA)", 0.0, 50.0, 10.0)
    temperature = st.slider("Temperature (°C)", 0, 80, 27)

    Is = Is * 1e-6
    IL = illumination * 1e-6
    T = temperature + 273
    q = 1.6e-19
    k = 1.38e-23

    V = np.linspace(-0.6, 0.6, 400)
    I = Is * (np.exp((q * V) / (k * T)) - 1) - IL

    fig, ax = plt.subplots()
    ax.plot(V, I * 1e6)
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Current (µA)")
    ax.set_title("Photodiode I–V Curve")
    st.pyplot(fig)

    st.info("Reverse bias + illumination shifts current downward (photocurrent).")

# ---------------------------
# Electro-Optic Modulator
# ---------------------------
elif section == "Electro-Optic Modulator":
    st.header("⚡ Electro-Optic Modulator (Pockels Effect)")

    V = st.slider("Applied Voltage (V)", 0, 500, 100)
    Vpi = st.slider("Half-Wave Voltage Vπ (V)", 50, 400, 200)

    intensity = (np.sin((np.pi * V) / (2 * Vpi))) ** 2

    st.metric("Output Intensity (Normalized)", f"{intensity:.3f}")
    st.info("Voltage controls phase → controls light intensity (digital/analog modulation).")
