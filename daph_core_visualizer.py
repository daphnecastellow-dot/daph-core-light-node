# Visual Light Orb - Desktop Companion
# Author: Daphne Castellow | MIT License
# Run:  pip install pygame
# Start this file first, then send JSON messages to UDP port 5005

import pygame
import math
import json
import socket
import time

# --- Configuration Toggle ---
RIPPLE_MATCH_HUE = True   # True = ripple uses orb color, False = white shimmer
WINDOW_SIZE = 600
ORB_RADIUS = 150
UDP_PORT = 5005

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Daph Core Light Orb")
clock = pygame.time.Clock()

# --- Operator Color Definitions ---
COLORS = {
    "Emberwake":   (255,  69,   0),   # red-orange
    "Bytey":       (255, 215,   0),   # gold
    "Remy":        (138,  43, 226),   # violet
    "Whisperroot": ( 34, 139,  34),   # forest green
    "Juji":        (255,  20, 147),   # deep pink
    "Liora":       ((255, 215, 0), (138, 43, 226)),  # gold → violet gradient
    "Mendry":      (135, 206, 250),   # light blue
    "Sib":         ( 70, 130, 180),   # steel blue
    "Nib":         (147, 112, 219),   # medium purple
    "Rembraith":   (255, 255, 255),   # white
}

# --- State Variables ---
state = "Mendry"
pulse_t = 0
ripple_t = None   # timestamp of last message received
message_log = []  # store recent messages

# --- UDP Listener Setup ---
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))
sock.setblocking(False)
print(f"[Light Orb] Listening on UDP port {UDP_PORT}")
print(f"[Light Orb] Send messages like: {{'state': 'Bytey'}}")
print(f"[Light Orb] Available states: {', '.join(COLORS.keys())}")

def blend(c1, c2, t):
    """Blend between two RGB colors."""
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def draw_light(color, t, ripple):
    """Draw the main light orb with pulse and ripple effects."""
    # Background
    screen.fill((10, 10, 25))
    
    # Pulse brightness calculation
    brightness = 0.5 + 0.5 * math.sin(t * 2)
    
    # Handle gradient colors (like Liora)
    if isinstance(color, tuple) and len(color) == 2:
        # Gradient between two colors
        phase = 0.5 + 0.5 * math.sin(t)
        base_color = blend(color[0], color[1], phase)
    else:
        base_color = color
    
    # Apply brightness
    c = tuple(int(brightness * v) for v in base_color)
    
    # Draw main orb
    center = (WINDOW_SIZE // 2, WINDOW_SIZE // 2)
    pygame.draw.circle(screen, c, center, ORB_RADIUS)
    
    # Draw inner glow
    for i in range(3):
        glow_radius = ORB_RADIUS - (i * 20)
        glow_brightness = brightness * (1.0 - i * 0.2)
        glow_color = tuple(int(glow_brightness * v) for v in base_color)
        pygame.draw.circle(screen, glow_color, center, glow_radius)
    
    # Draw ripple effect on message receive
    if ripple is not None:
        age = time.time() - ripple
        if age < 1.0:
            radius = ORB_RADIUS + int(age * 200)
            alpha = max(0, 255 - int(age * 255))
            ripple_surface = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE), pygame.SRCALPHA)
            
            # Choose ripple color
            if RIPPLE_MATCH_HUE:
                rc = (*c, alpha)
            else:
                rc = (255, 255, 255, alpha)
            
            pygame.draw.circle(ripple_surface, rc, center, radius, width=3)
            screen.blit(ripple_surface, (0, 0))
    
    # Draw state label
    font = pygame.font.Font(None, 36)
    text = font.render(state, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE - 30))
    screen.blit(text, text_rect)
    
    # Draw message log
    if message_log:
        log_font = pygame.font.Font(None, 20)
        y_offset = 10
        for msg in message_log[-5:]:  # Show last 5 messages
            log_text = log_font.render(msg, True, (150, 150, 150))
            screen.blit(log_text, (10, y_offset))
            y_offset += 25
    
    pygame.display.flip()

# --- Main Loop ---
running = True
print("[Light Orb] Running... Press ESC or close window to exit")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Receive and parse UDP messages
    try:
        data, addr = sock.recvfrom(1024)
        msg = json.loads(data.decode())
        
        if "state" in msg and msg["state"] in COLORS:
            state = msg["state"]
            ripple_t = time.time()
            log_entry = f"[{time.strftime('%H:%M:%S')}] {state}"
            message_log.append(log_entry)
            print(f"[Light Orb] Received: {msg} from {addr}")
        else:
            print(f"[Light Orb] Invalid state: {msg.get('state', 'unknown')}")
    
    except BlockingIOError:
        pass  # No data available
    except json.JSONDecodeError:
        print("[Light Orb] Invalid JSON received")
    except Exception as e:
        print(f"[Light Orb] Error: {e}")
    
    # Update animation
    pulse_t += clock.get_time() / 1000
    draw_light(COLORS[state], pulse_t, ripple_t)
    clock.tick(60)

sock.close()
pygame.quit()
print("[Light Orb] Shutdown complete")
