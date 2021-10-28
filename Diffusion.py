__author__ = 'myles'

HOT = 4
AMBIENT=0
COLD = 0


def diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    return(1-8*diffusionRate)*site + diffusionRate*(N + NE + E +  SE + S + SW + W + NW)

def apply_hot_cold(bar, hot_sites, cold_sites):
    new_bar = bar
    for site in hot_sites:
        new_bar[site[1]][site[0]] = HOT
    for site in cold_sites:
        new_bar[site[1]][site[0]] = COLD
    return new_bar
        