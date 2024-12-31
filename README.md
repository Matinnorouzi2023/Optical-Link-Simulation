# Optical Link Simulation

## Overview
This project provides a comprehensive simulation of optical communication links, specifically focusing on ground-to-space transmissions. The simulation considers the impact of atmospheric turbulence, distance, and wavelength on communication quality, offering insights into the Bit Error Rate (BER) under varying conditions.

The simulation uses advanced models such as:
- **Kolmogorov Model**: For atmospheric turbulence.
- **Geometric Loss and Atmospheric Attenuation**: To assess power loss.

The results are visualized using a 3D surface plot, showing the relationship between BER, distance, and wavelength.

---

## Features
- **Modeling atmospheric turbulence** using the Kolmogorov spectrum.
- **Simulating power loss** due to geometric spreading and atmospheric attenuation.
- **Calculating Bit Error Rate (BER)** under various conditions.
- **Visualizing results** in a detailed 3D surface plot for better understanding.

---

## Applications
This project can help address challenges in:
1. **Designing robust optical communication systems**.
2. **Evaluating the impact of turbulence and distance** on communication reliability.
3. **Optimizing wavelength selection** for minimizing BER.

Potential use cases include satellite communication, free-space optical (FSO) systems, and ground-to-space data transmission networks.

---

## Requirements
To run the simulation, you need:
1. Python 3.8 or higher
2. The following Python libraries:
   - `numpy`
   - `matplotlib`
   - `scipy`

Install dependencies using:
```bash
pip install numpy matplotlib scipy
```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/optical-link-simulation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd optical-link-simulation
   ```
3. Run the simulation:
   ```bash
   python optical_link_simulation.py
   ```
4. A 3D surface plot will be displayed, showing BER versus distance and wavelength.

---

## Explanation of Results
The simulation generates a 3D surface plot where:
- The **x-axis** represents the distance (in kilometers).
- The **y-axis** represents the wavelength (in nanometers).
- The **z-axis** shows the Bit Error Rate (BER).

The plot provides insights into how different wavelengths and distances affect the quality of optical communication, enabling the optimization of system parameters.

---

## Key Models Used
1. **Kolmogorov Spectrum**:
   - Models atmospheric turbulence based on refractive index variations.
   - Accounts for fading effects in signal transmission.
2. **Geometric Loss**:
   - Considers aperture sizes and distance to estimate signal power reduction.
3. **BER Calculation**:
   - Uses an idealized BPSK model to determine error rates based on the Signal-to-Noise Ratio (SNR).

---

## Example Output
A sample 3D plot showing the BER changes across distances and wavelengths. The results indicate how communication quality degrades with increasing distance and certain wavelengths due to turbulence and noise.

---

## Future Improvements
- Integration of machine learning models to predict BER under complex conditions.
- Inclusion of weather-based turbulence models.
- Support for real-world experimental data.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contact
For questions or collaboration, please contact:
- **Name**: Matin
- **Email**: hajnorouzimatin@gmail.com

