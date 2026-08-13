from __future__ import annotations

import numpy as np


def shape(s):
    s = np.asarray(s)
    return np.where(s <= 1, 1 - 10*s**3 + 15*s**4 - 6*s**5, 0.0)


def shape_d(s):
    s = np.asarray(s)
    return np.where(s <= 1, -30*s**2 + 60*s**3 - 30*s**4, 0.0)


def shape_dd(s):
    s = np.asarray(s)
    return np.where(s <= 1, -60*s + 180*s**2 - 120*s**3, 0.0)


def schedule(t, rho0, rhoinf, T):
    s = t / T
    gap = rho0 - rhoinf
    return rhoinf + gap*shape(s), gap*shape_d(s)/T, gap*shape_dd(s)/(T*T)


def coordinates(t, e0, channel, params):
    p = params["ppc"]
    rho0 = np.asarray(p[f"rho0_{channel}"], dtype=float)
    rhoi = np.asarray(p[f"rhoinf_{channel}"], dtype=float)
    T = float(p[f"T_{'omega' if channel == 'omega' else 'V'}"])
    rho, drho, ddrho = schedule(t, rho0, rhoi, T)
    sigma = e0/rho
    if np.any(np.abs(sigma) >= 1):
        raise FloatingPointError("PPC coordinate evaluated outside strict funnel")
    zeta = np.arctanh(sigma)
    h = 1.0/(rho*(1-sigma**2))
    return rho, drho, ddrho, sigma, zeta, h


def voltage_alpha(t, e0, Vdot, params):
    rho, drho, ddrho, sigma, zeta, h = coordinates(t, e0, "V", params)
    k1 = float(params["controller"]["k1_V"])
    alpha = sigma*drho-k1*rho*(1-sigma**2)*zeta
    chi = Vdot-alpha
    dsigma = (chi-k1*rho*(1-sigma**2)*zeta)/rho
    dzeta = dsigma/(1-sigma**2)
    dalpha = (dsigma*drho+sigma*ddrho-k1*(drho*(1-sigma**2)*zeta
              -2*rho*sigma*dsigma*zeta+rho*(1-sigma**2)*dzeta))
    return alpha, dalpha, chi, (rho, drho, sigma, zeta, h)


def frequency_alpha(t, e0, params):
    rho, drho, _, sigma, zeta, h = coordinates(t, e0, "omega", params)
    k1 = float(params["controller"]["k1_omega"])
    alpha = sigma*drho-k1*rho*(1-sigma**2)*zeta
    return alpha, (rho, drho, sigma, zeta, h)
