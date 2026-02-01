import numpy as np
import matplotlib.pyplot as plt

# --- PARAMETER DER ROHLING-HIGGS-SYMMETRIE (v11) ---
L_R, L_H = 1.0, 1.0       # Selbstkopplung
BETA = 0.4774             # Die 'magische' Kopplung (CERN 2026 Match)
GRID_SIZE = 100           # Raumgitter 100x100
DT = 0.02                 # Zeitschritt
STEPS = 500               # Simulationsdauer

# Initialisierung der Felder (Zufällige Quantenfluktuationen)
R = np.random.normal(0, 0.1, (GRID_SIZE, GRID_SIZE))
H = np.random.normal(0, 0.1, (GRID_SIZE, GRID_SIZE))
vR = np.zeros_like(R)
vH = np.zeros_like(H)

def laplace(Z):
    """Berechnet den diskreten Laplace-Operator (Raumkrümmung)"""
    return (np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0) +
            np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1) - 4 * Z)

print("Starte Simulation der Rohling-Higgs-Kopplung...")

# --- SIMULATIONS-LOOP ---
for t in range(STEPS):
    force_R = - (L_R * R**3 + BETA * R * H**2) + 0.1 * laplace(R)
    force_H = - (L_H * H**3 + BETA * H * R**2) + 0.1 * laplace(H)
    
    # Update der Impulse (Energieerhaltung als Motor)
    vR += force_R * DT
    vH += force_H * DT
    
    # Update der Feldstärken
    R += vR * DT
    H += vH * DT

print("Simulation abgeschlossen. Erzeuge Visualisierung...")

# Visualisierung der Kopplung
plt.figure(figsize=(12, 5))
plt.subplot(121)
plt.title("Rohling-Feld (R) Struktur")
plt.imshow(R, cmap='magma')
plt.colorbar()

plt.subplot(122)
plt.title("Higgs-Feld (H) Struktur")
plt.imshow(H, cmap='viridis')
plt.colorbar()

plt.tight_layout()
plt.show()
