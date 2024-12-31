# Optical Link Simulation: Step-by-Step Development
# Project Goal: Simulate optical communication links from ground to space considering atmospheric turbulence
# Author: <Your Name>
# Usage: Part of MSCA PhD application showcase
import matplotlib
matplotlib.use('TkAgg')  # تنظیم backend برای استفاده از tkinter

## Advanced Optical Link Simulation with Professional Enhancements
# Project Goal: Simulate advanced optical communication links considering atmospheric turbulence, noise, and advanced error correction.
# Author: <Your Name>
# Usage: Showcase for MSCA PhD application

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc


# گام 1: مقداردهی اولیه پارامترها
def initialize_parameters():
    params = {
        "c": 3e8,  # سرعت نور (m/s)
        "wavelengths": np.linspace(800e-9, 1600e-9, 50),  # طول موج‌ها (m)
        "aperture_diameter": 0.1,  # قطر دیافراگم فرستنده (m)
        "receiver_diameter": 0.1,  # قطر دیافراگم گیرنده (m)
        "distances": np.linspace(1e3, 1000e3, 100),  # فاصله‌ها (m)
        "power_transmitted": 1,  # توان ارسالی (W)
        "refractive_index_structure": 1e-14,  # مقدار Cn^2
        "receiver_noise": 1e-12,  # توان نویز گیرنده (W)
    }
    return params


# گام 2: محاسبه تضعیف اتمسفری با مدل Kolmogorov
def atmospheric_loss(params, distance, wavelength):
    """محاسبه تضعیف اتمسفری بر اساس فاصله و طول موج"""
    r0 = (0.423 * (2 * np.pi / wavelength) ** 2 * params["refractive_index_structure"] * distance) ** (-3 / 5)
    loss_factor = np.exp(-distance / r0)  # تخمینی
    return loss_factor


# گام 3: محاسبه اثر توربولانس با مدل Kolmogorov
def turbulence_effects(params, distance):
    """شبیه‌سازی توربولانس با استفاده از مدل Kolmogorov"""
    cn2 = params["refractive_index_structure"]
    fading = np.random.lognormal(mean=0, sigma=np.sqrt(cn2 * distance ** (7 / 6)))
    return fading


# گام 4: محاسبه توان دریافتی
def received_power(params, distance, wavelength):
    """محاسبه توان دریافتی نوری"""
    power_transmitted = params["power_transmitted"]
    aperture_diameter = params["aperture_diameter"]
    receiver_diameter = params["receiver_diameter"]

    geometric_loss = (aperture_diameter * receiver_diameter) / (distance ** 2)
    atmospheric_attenuation = atmospheric_loss(params, distance, wavelength)
    turbulence = turbulence_effects(params, distance)

    power_received = power_transmitted * geometric_loss * atmospheric_attenuation * turbulence
    return power_received


# گام 5: تحلیل نرخ خطا (BER)
def bit_error_rate(received_power, params):
    """محاسبه نرخ خطا با استفاده از نویز"""
    noise = params["receiver_noise"]
    snr = received_power / noise
    ber = 0.5 * erfc(np.sqrt(snr))  # فرمول BPSK
    return ber


# گام 6: شبیه‌سازی و رسم نمودار
def simulate():
    params = initialize_parameters()
    wavelengths = params["wavelengths"]
    distances = params["distances"]

    # آماده‌سازی ماتریس نتایج
    ber_matrix = np.zeros((len(wavelengths), len(distances)))

    # محاسبات برای هر طول موج و فاصله
    for i, wavelength in enumerate(wavelengths):
        for j, distance in enumerate(distances):
            power = received_power(params, distance, wavelength)
            ber_matrix[i, j] = bit_error_rate(power, params)

    # رسم نمودار سه‌بعدی
    X, Y = np.meshgrid(distances / 1e3, wavelengths * 1e9)
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, ber_matrix, cmap='viridis', edgecolor='k')
    ax.set_xlabel("Distance (km)")
    ax.set_ylabel("Wavelength (nm)")
    ax.set_zlabel("Bit Error Rate")
    ax.set_title("BER vs Distance and Wavelength")
    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.show()


# گام 7: نقطه ورود اصلی
if __name__ == "__main__":
    simulate()
