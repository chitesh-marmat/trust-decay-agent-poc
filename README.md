# Trust Decay Agent – Proof of Concept

This repository contains an annotated pseudocode proof of concept
for the Trust Decay Agent proposed for the eRaksha Hackathon 2026.

## Core Idea
Instead of binary alerts, the system maintains a continuous trust score
for each IoT device. Trust decays gradually based on behavioural anomalies
and recovers slowly during normal operation.

## Architecture
The agent operates in a continuous loop:
Observe → Reason → Act

- Observe: Collect lightweight behavioural signals
- Reason: Apply trust decay logic based on anomalies
- Act: Trigger graduated autonomous responses

## Key Properties
- Edge-native and lightweight
- No cloud dependency
- Explainable decision logic
- Designed for IoT constraints

This PoC demonstrates the feasibility of autonomous,
trust-based IoT security without requiring heavy computation.
