# [OBIAKA UDOM] - Assignment 3
def format_alert(severity, source_ip, alert_message):
    # Return a formatted string in the pattern: [SEVERITY] - IP: Message
    # Note: Look closely at the starter code below-something about the spacing or
    # punctuation might need adjustment!
    return f"[{severity}] - {source_ip}: {alert_message}"