# Autonomous Fraud Investigator (ReACT Agent)

This project implements an autonomous AI agent capable of investigating financial transactions. 

---

## 🏛️ Architecture
The system operates on a continuous 3-step loop:

1. **THOUGHT (Reasoning):** The model breaks down the investigation goal into logical steps.
2. **ACTION (Acting):** The agent identifies and executes specific tools to fetch real-time data.
3. **OBSERVATION:** The agent evaluates the data returned by the tools to decide if more information is needed.

---

## 🛠️ Investigation Tools (`investigation_tools.py`)

This module provides the functional interface between the AI agent and the financial data.

### Available Tools

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| `get_transaction_history` | `account_id`, `days` | Retrieves transaction logs. |
| `get_customer_profile` | `customer_id` | Fetches risk scores and profile data. |
| `check_regulatory_thresholds` | `amount`, `type` | Validates compliance thresholds. |

### Integration Notes
* **Parameter Validation:** Includes internal casting (e.g., `int(amount)`).
* **Error Handling:** Returns structured error messages for agent self-correction.
* **Data Consistency:** Every tool returns a dictionary.

---

## ⚙️ Troubleshooting & Development Lessons

### 1. Hot-Reloading Modules
Because Colab caches imports, changes to your `.py` files aren't automatically reflected.

**Solution:** Use `importlib` to force a reload.

```
import importlib
import tools.investigation_tools as inv
importlib.reload(inv)
```

### 2. Parameter Name Mismatches
When an LLM generates JSON, its keys might not match your function’s argument names.

**Solution:** Use a Mapping Layer in your `execute_tool` function to translate keys.



### 3. Solving "Read-Only" File System Issues
Colab/Drive sometimes locks files as "Read-only."

**Solution:** Use the `%%writefile` magic command to overwrite your code.

```python
%%writefile /content/drive/MyDrive/path/to/tools/investigation_tools.py
# Paste your code here and run the cell to save
```
### 4. Parsing Logic Debugging
If your agent fails to execute tools (often due to regex or JSON formatting), add a debug print at the start of your parsing function to verify the content being processed.

```python
def parse_tool_calls(text):
    print(f"DEBUG: Parsing text length: {len(text)}")
    # ... rest of your logic
```

## 🚀 Features
* **Autonomous Reasoning:** Uses Chain of Thought (CoT).
* **Dynamic Tool Use:** Interfaces via a robust parsing layer.
* **Self-Correction:** Implements parameter mapping and type casting.

## 🏁 Getting Started
1. **Mount Drive:** Ensure your working directory is mounted.
2. **Setup:** Place your `investigation_tools.py` in the directory.
3. **Iterate:** Use `importlib.reload()` in your test cells.


