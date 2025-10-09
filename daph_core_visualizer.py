
# Author: Daphne Castellow | MIT License
# Run:  pip install pygame
# Start this file first, then send JSON messages to UDP port 5005

import pygame, math, json, socket, time

# --- configuration toggle ---
RIPPLE_MATCH_HUE = True   # True = ripple uses orb color, False = white shimmer

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

COLORS = {
    "Bytey":  (255, 215,   0),   # gold
    "Mendry": (135, 206, 250),   # light blue
    "Remy":   (138,  43, 226),   # violet
    "Liora":  ((255, 215, 0), (138, 43, 226))  # gold → violet gradient
}

state = "Mendry"
pulse_t = 0
ripple_t = None   # timestamp of last message

# --- UDP listener ---
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5005))
sock.setblocking(False)

def blend(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def draw_light(color, t, ripple):
    screen.fill((10, 10, 25))
    brightness = 0.5 + 0.5 * math.sin(t * 2)

    # base color and gradient
    if state == "Liora":
        phase = 0.5 + 0.5 * math.sin(t)
        base_color = blend(*color, phase)
    else:
        base_color = color
    c = tuple(int(brightness * v) for v in base_color)

    # main orb
    pygame.draw.circle(screen, c, (300, 300), 150)

    # ripple effect
    if ripple is not None:
        age = time.time() - ripple
        if age < 1.0:
            radius = 150 + int(age * 200)
            alpha = max(0, 255 - int(age * 255))
            ripple_surface = pygame.Surface((600, 600), pygame.SRCALPHA)

            rc = (*c, alpha) if RIPPLE_MATCH_HUE else (255, 255, 255, alpha)
            pygame.draw.circle(ripple_surface, rc, (300, 300), radius, width=3)
            screen.blit(ripple_surface, (0, 0))

    pygame.display.flip()

# --- main loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # receive and parse message
    try:
        data, _ = sock.recvfrom(1024)
        msg = json.loads(data.decode())
        if "state" in msg and msg["state"] in COLORS:
            state = msg["state"]
            ripple_t = time.time()
            print("Received:", msg)
    except Exception:
        pass

    pulse_t += clock.get_time() / 1000
    draw_light(COLORS[state], pulse_t, ripple_t)
    clock.tick(60)

pygame.quit()
