# Investigation Tools (`investigation_tools.py`)

This module provides the functional interface between the AI agent and the financial data.

## Available Tools

- `get_transaction_history(account_id, days)`: Retrieves transaction logs for a specific account over a set period.
- `get_customer_profile(customer_id)`: Fetches risk scores, occupation, and jurisdictional data for customers.
- `check_regulatory_thresholds(amount, type)`: Validates transactions against defined compliance thresholds (e.g., CTR, wire transfer limits).

## Integration Notes

- **Parameter Validation:** All tools include internal casting (e.g., `int(amount)`) to ensure robustness against various LLM output formats.
- **Error Handling:** The tool registry is designed to return structured error messages, which are fed back to the agent as "Observations," enabling the agent to self-correct during the ReACT loop.

## Developer Guidelines

When adding new tools:
1. Define the function signature clearly.
2. Ensure the parameter names match the JSON keys expected by the agent's parsing logic.
3. Return a dictionary object to maintain consistency with the agent's observation pipeline.
