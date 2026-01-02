"""
Trust Decay Agent – Annotated Pseudocode
PoC for eRaksha Hackathon 2026

Goal:
Continuously evaluate IoT device trust and trigger
graduated autonomous responses at the edge.
"""

# Initial trust score for a device
trust_score = 100   # range: 0 (untrusted) to 100 (fully trusted)

# Thresholds for response escalation
THRESHOLDS = {
    "TRUSTED": 80,
    "WATCH": 60,
    "RESTRICTED": 30,
    "ISOLATED": 0
}

def observe(device_telemetry):
    """
    OBSERVE:
    Collect lightweight behavioural signals from the IoT device.
    Example signals:
    - packet_rate
    - destination_ip_entropy
    - authentication_failures
    """
    return extract_features(device_telemetry)


def reason(features, trust_score):
    """
    REASON:
    Update trust score based on anomalies.
    Small anomalies reduce trust gradually.
    Repeated anomalies compound trust decay.
    """
    anomaly_score = compute_anomaly(features)

    # Trust decay is proportional 
    trust_score -= anomaly_score

    # Trust naturally recovers slowly if behaviour is normal
    if anomaly_score == 0:
        trust_score += 1

 
    trust_score = max(0, min(100, trust_score))
    return trust_score


def act(trust_score):
    """
    ACT:
    Decide autonomous response based on current trust level.
    """
    if trust_score >= THRESHOLDS["TRUSTED"]:
        return "NORMAL_MONITORING"

    elif trust_score >= THRESHOLDS["WATCH"]:
        return "ENHANCED_MONITORING"

    elif trust_score >= THRESHOLDS["RESTRICTED"]:
        return "TRAFFIC_SHAPING"

    else:
        return "DEVICE_ISOLATION"


def trust_decay_agent(device_telemetry):
    """
    Continuous Observe → Reason → Act loop running at the edge.
    """
    global trust_score

    features = observe(device_telemetry)
    trust_score = reason(features, trust_score)
    response = act(trust_score)

    return trust_score, response
