# Autonomous Fraud Investigator (ReACT Agent)

This project implements an autonomous AI agent capable of investigating financial transactions. Unlike static LLMs, this agent uses the **ReACT (Reasoning and Acting)** framework to iteratively think, act, and observe, allowing it to perform complex multi-step investigations.

## Architecture

The system operates on a continuous 3-step loop:

1. **THOUGHT (Reasoning):** The model breaks down the investigation goal into logical steps.

2. **ACTION (Acting):** The agent identifies and executes specific tools to fetch real-time data.

3. **OBSERVATION:** The agent evaluates the data returned by the tools to decide if more information is needed or if a conclusion can be reached.

## Features

* **Autonomous Reasoning:** Uses Chain of Thought (CoT) to ensure logical consistency.

* **Dynamic Tool Use:** Interfaces with external databases via a structured parsing layer.

* **Self-Correction:** The agent can parse tool errors (e.g., type mismatches) and adjust its parameters in subsequent rounds.

## Getting Started
Ensure you have the required API keys set up, then run the primary investigation script.
