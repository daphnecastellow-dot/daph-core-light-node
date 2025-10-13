# wifi_helper.py
# Wi-Fi signal strength helper for Daph Core Light Node
# Author: Daphne Castellow
# License: MIT

import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# --- Core WiFi Functions ---

def get_strength():
    """
    Return the RSSI (dBm) of the connected Wi-Fi network or None.
    
    Returns:
        int: RSSI in dBm (-90 to -30 typical range)
        None: If not connected or scan fails
    """
    if not wlan.isconnected():
        return None
    
    current = wlan.config('essid')
    
    try:
        nets = wlan.scan()
        for n in nets:
            if n[0].decode() == current:
                return n[3]  # RSSI value
    except Exception as e:
        print(f"[WiFi] Scan error: {e}")
    
    return None

def get_signal_quality():
    """
    Get signal quality as percentage (0-100%).
    
    Returns:
        int: Signal quality percentage
        None: If not connected
    """
    rssi = get_strength()
    if rssi is None:
        return None
    
    # Convert RSSI to quality percentage
    # -30 dBm = 100%, -90 dBm = 0%
    quality = min(100, max(0, 2 * (rssi + 100)))
    return quality

def get_signal_bars():
    """
    Get signal strength as 0-5 bars (like phone display).
    
    Returns:
        int: Number of bars (0-5)
        None: If not connected
    """
    rssi = get_strength()
    if rssi is None:
        return None
    
    # Signal bars based on typical RSSI ranges
    if rssi >= -50:
        return 5  # Excellent
    elif rssi >= -60:
        return 4  # Very Good
    elif rssi >= -70:
        return 3  # Good
    elif rssi >= -80:
        return 2  # Fair
    elif rssi >= -90:
        return 1  # Poor
    else:
        return 0  # Very Poor

def strength_to_brightness(rssi):
    """
    Convert RSSI (-90 to -30 dBm) into brightness 0.1–1.0.
    
    Args:
        rssi: Signal strength in dBm
    
    Returns:
        float: Brightness value (0.1 to 1.0)
    """
    if rssi is None:
        return 0.1
    
    # Linear mapping: -90 dBm = 0.1, -30 dBm = 1.0
    brightness = (rssi + 90) / 60
    return max(0.1, min(1.0, brightness))

def strength_to_color(rssi):
    """
    Convert RSSI to color (red=poor, yellow=ok, green=good).
    
    Args:
        rssi: Signal strength in dBm
    
    Returns:
        tuple: RGB color (red, green, blue)
    """
    if rssi is None:
        return (100, 100, 100)  # Gray for disconnected
    
    if rssi >= -60:
        # Excellent: Green
        return (0, 255, 0)
    elif rssi >= -70:
        # Good: Yellow-green
        return (150, 255, 0)
    elif rssi >= -80:
        # Fair: Yellow
        return (255, 255, 0)
    elif rssi >= -85:
        # Poor: Orange
        return (255, 150, 0)
    else:
        # Very Poor: Red
        return (255, 0, 0)

def get_connection_info():
    """
    Get comprehensive connection information.
    
    Returns:
        dict: Connection details or None if not connected
    """
    if not wlan.isconnected():
        return None
    
    rssi = get_strength()
    
    return {
        'connected': True,
        'ssid': wlan.config('essid'),
        'rssi': rssi,
        'quality': get_signal_quality(),
        'bars': get_signal_bars(),
        'ip': wlan.ifconfig()[0],
        'mac': ':'.join(['%02x' % b for b in wlan.config('mac')]),
        'channel': wlan.config('channel') if hasattr(wlan, 'channel') else None
    }

def print_signal_info():
    """Print formatted signal information to console."""
    info = get_connection_info()
    
    if info is None:
        print("[WiFi] Not connected")
        return
    
    bars = '█' * info['bars'] + '░' * (5 - info['bars'])
    quality_desc = get_quality_description(info['rssi'])
    
    print(f"[WiFi] {info['ssid']}")
    print(f"       Signal: {bars} ({info['rssi']} dBm)")
    print(f"       Quality: {info['quality']}% - {quality_desc}")
    print(f"       IP: {info['ip']}")

def get_quality_description(rssi):
    """
    Get human-readable quality description.
    
    Args:
        rssi: Signal strength in dBm
    
    Returns:
        str: Quality description
    """
    if rssi is None:
        return "Disconnected"
    elif rssi >= -50:
        return "Excellent"
    elif rssi >= -60:
        return "Very Good"
    elif rssi >= -70:
        return "Good"
    elif rssi >= -80:
        return "Fair"
    elif rssi >= -90:
        return "Poor"
    else:
        return "Very Poor"

# --- WiFi Monitoring Functions ---

def monitor_signal(duration_seconds=60, interval_seconds=5):
    """
    Monitor WiFi signal strength over time.
    
    Args:
        duration_seconds: How long to monitor (default: 60)
        interval_seconds: Time between checks (default: 5)
    """
    print(f"[WiFi Monitor] Monitoring signal for {duration_seconds} seconds")
    print("Time | RSSI  | Quality | Bars | Status")
    print("-----|-------|---------|------|--------")
    
    elapsed = 0
    readings = []
    
    while elapsed < duration_seconds:
        rssi = get_strength()
        quality = get_signal_quality()
        bars = get_signal_bars()
        status = get_quality_description(rssi)
        
        if rssi is not None:
            readings.append(rssi)
            bars_display = '█' * bars + '░' * (5 - bars)
            print(f"{elapsed:4d}s | {rssi:4d} | {quality:6d}% | {bars_display} | {status}")
        else:
            print(f"{elapsed:4d}s | N/A   | N/A     | ░░░░░ | Disconnected")
        
        time.sleep(interval_seconds)
        elapsed += interval_seconds
    
    # Summary
    if readings:
        avg_rssi = sum(readings) / len(readings)
        min_rssi = min(readings)
        max_rssi = max(readings)
        print(f"\n[Summary] Avg: {avg_rssi:.1f} dBm | Min: {min_rssi} | Max: {max_rssi}")

def signal_stability_check(samples=10, interval_seconds=2):
    """
    Check signal stability by taking multiple samples.
    
    Args:
        samples: Number of samples to take (default: 10)
        interval_seconds: Time between samples (default: 2)
    
    Returns:
        dict: Stability metrics
    """
    print(f"[Stability Check] Taking {samples} samples...")
    
    readings = []
    
    for i in range(samples):
        rssi = get_strength()
        if rssi is not None:
            readings.append(rssi)
            print(f"  Sample {i+1}/{samples}: {rssi} dBm")
        time.sleep(interval_seconds)
    
    if not readings:
        print("[Stability Check] No valid readings")
        return None
    
    avg = sum(readings) / len(readings)
    min_val = min(readings)
    max_val = max(readings)
    variance = max_val - min_val
    
    # Determine stability
    if variance <= 5:
        stability = "Excellent"
    elif variance <= 10:
        stability = "Good"
    elif variance <= 15:
        stability = "Fair"
    else:
        stability = "Unstable"
    
    result = {
        'average': avg,
        'min': min_val,
        'max': max_val,
        'variance': variance,
        'stability': stability
    }
    
    print(f"\n[Results]")
    print(f"  Average: {avg:.1f} dBm")
    print(f"  Range: {min_val} to {max_val} dBm")
    print(f"  Variance: {variance} dB")
    print(f"  Stability: {stability}")
    
    return result

def scan_networks():
    """
    Scan for available WiFi networks.
    
    Returns:
        list: Available networks with details
    """
    print("[WiFi Scan] Scanning for networks...")
    
    try:
        nets = wlan.scan()
        networks = []
        
        print(f"\nFound {len(nets)} networks:")
        print("SSID                    | RSSI  | Channel | Security")
        print("------------------------|-------|---------|----------")
        
        for net in nets:
            ssid = net[0].decode()
            bssid = ':'.join(['%02x' % b for b in net[1]])
            channel = net[2]
            rssi = net[3]
            security = net[4]
            hidden = net[5]
            
            # Determine security type
            if security == 0:
                sec_type = "Open"
            elif security == 1:
                sec_type = "WEP"
            elif security == 2:
                sec_type = "WPA-PSK"
            elif security == 3:
                sec_type = "WPA2-PSK"
            elif security == 4:
                sec_type = "WPA/WPA2-PSK"
            else:
                sec_type = f"Type {security}"
            
            networks.append({
                'ssid': ssid,
                'bssid': bssid,
                'channel': channel,
                'rssi': rssi,
                'security': sec_type,
                'hidden': hidden
            })
            
            # Print network info
            quality = get_quality_description(rssi)
            ssid_display = ssid[:23] if len(ssid) <= 23 else ssid[:20] + "..."
            print(f"{ssid_display:23} | {rssi:4d}  | {channel:7d} | {sec_type}")
        
        return networks
        
    except Exception as e:
        print(f"[WiFi Scan] Error: {e}")
        return []

# --- Connection Helpers ---

def wait_for_connection(timeout_seconds=30):
    """
    Wait for WiFi connection with timeout.
    
    Args:
        timeout_seconds: Maximum wait time (default: 30)
    
    Returns:
        bool: True if connected, False if timeout
    """
    print("[WiFi] Waiting for connection...")
    
    elapsed = 0
    while elapsed < timeout_seconds:
        if wlan.isconnected():
            info = get_connection_info()
            print(f"[WiFi] Connected to {info['ssid']}")
            print(f"       IP: {info['ip']}")
            print(f"       Signal: {info['rssi']} dBm ({get_quality_description(info['rssi'])})")
            return True
        
        time.sleep(1)
        elapsed += 1
        
        if elapsed % 5 == 0:
            print(f"[WiFi] Still waiting... ({elapsed}s)")
    
    print("[WiFi] Connection timeout")
    return False

def is_signal_adequate(min_rssi=-80):
    """
    Check if signal strength is adequate for operation.
    
    Args:
        min_rssi: Minimum acceptable RSSI (default: -80 dBm)
    
    Returns:
        bool: True if signal is adequate
    """
    rssi = get_strength()
    
    if rssi is None:
        return False
    
    return rssi >= min_rssi

# --- Demo & Testing ---

def demo():
    """Demonstrate WiFi helper functions."""
    print("\n" + "="*50)
    print("WiFi Helper Demo")
    print("="*50 + "\n")
    
    # Connection info
    print("1. Connection Information:")
    print_signal_info()
    
    time.sleep(2)
    
    # Signal quality
    print("\n2. Signal Quality:")
    rssi = get_strength()
    if rssi:
        print(f"   RSSI: {rssi} dBm")
        print(f"   Quality: {get_signal_quality()}%")
        print(f"   Bars: {'█' * get_signal_bars()}")
        print(f"   Color: {strength_to_color(rssi)}")
        print(f"   Brightness: {strength_to_brightness(rssi):.2f}")
    
    time.sleep(2)
    
    # Available networks
    print("\n3. Available Networks:")
    scan_networks()
    
    print("\n" + "="*50)
    print("Demo Complete")
    print("="*50)

if __name__ == "__main__":
    demo()
