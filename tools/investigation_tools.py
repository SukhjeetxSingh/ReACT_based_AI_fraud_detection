"""
Financial Investigation Tools for ReACT Framework

This module provides pre-defined tools for financial compliance investigations
that can be used with the ReACT (Reasoning and Acting) framework.
"""

import json
import re
from datetime import datetime, timedelta


# Tool 1: Transaction History Lookup
def get_transaction_history(account_id, days=30):
    """Retrieve transaction history for an account (simulated data)"""

    # TODO: Implement different transaction patterns based on account_id
    # Hint: Use if/elif statements to return different data for:
    # - "high_risk" accounts: Multiple cash deposits just under $10K
    # - "business" accounts: Large wire transfers
    # - Other accounts: Normal transactions
    if ("high_risk") in account_id.lower():
        transactions = [
            {"date":"18-05-2026", "amount":9860, "type":"cash_deposit", "location":"branch_A"},
            {"date":"17-05-2026", "amount":9800, "type":"cash_deposit", "location":"branch_B"},
            {"date":"16-05-2026", "amount":9560, "type":"cash_deposit", "location":"branch_A"},
            {"date":"15-05-2026", "amount":9990, "type":"cash_deposit", "location":"branch_C"},
            {"date":"14-05-2026", "amount":8860, "type":"cash_deposit", "location":"branch_A"},
            {"date":"13-05-2026", "amount":8910, "type":"cash_deposit", "location":"branch_A"},
        ]
    elif ("other") in account_id.lower():
        transactions = [
            {"date":"18-05-2026", "amount":50000, "type":"wire_transfer", "location":"singapore_bank_A"},
            {"date":"19-05-2026", "amount":-59000, "type":"wire_transfer", "location":"singapore_bank_B"},
            {"date":"20-05-2026", "amount":-80880, "type":"wire_transfer", "location":"singapore_bank_C"},
            {"date":"21-05-2026", "amount":90900, "type":"wire_transfer", "location":"singapore_bank_A"},
            {"date":"22-05-2026", "amount":-99900, "type":"wire_transfer", "location":"singapore_bank_C"},
            {"date":"23-05-2026", "amount":80900, "type":"wire_transfer", "location":"singapore_bank_D"},
            ]
    else:
        transactions = [
            {"date":"18-05-2026", "amount":3200, "type":"payroll_deposit", "location":"ACH"},
            {"date":"19-05-2026", "amount":-900, "type":"rent", "location":"interact"},
            {"date":"20-05-2026", "amount":-270, "type":"grocery", "location":"Online"},
            ]
        

    return {
        "account_id": account_id,
        "period_days": days,
        "transaction_count": len(transactions),
        "transactions": transactions
    }


# Tool 2: Customer Profile Lookup
def get_customer_profile(customer_id):
    """Retrieve customer profile and risk information (simulated data)"""

    # TODO: Create profiles dictionary with customer data
    # Include: name, occupation, income, account_age, risk_score, etc.
    profiles = {
        # TODO: Add CUST_001, CUST_002, CUST_003 profiles
        "CUST_001":{
            "name": "Maria Santos",
            "occupation": "Restaurant Manager",
            "annual_income": 80000,
            "account_age_year": 4,
            "previous_sar": 0,
            "risk_score": 6.8,
            "address": "Local Resident"
        },
        "CUST_002":{
            "name": "Robert Chen",
            "occupation": "Business Owner",
            "annual_income": 140000,
            "account_age_year": 0.5,
            "previous_sar": 0,
            "risk_score": 8.7,
            "address": "Multiple Jurisdictions"
        },
        "CUST_003":{
            "name": "Sarah Johnson",
            "occupation": "Software Engineer",
            "annual_income": 85000,
            "account_age_year": 5,
            "previous_sar": 0,
            "risk_score": 2.1,
            "address": "Local Resident"
        },
    }

    return profiles.get(customer_id, {"error": "Customer not found"})


# Tool 3: Regulatory Threshold Check
def check_regulatory_thresholds(amount, type):
    """Check transaction against regulatory reporting thresholds"""

    amount = float(amount)
    # TODO: Define regulatory thresholds
    thresholds = {
        "CTR_threshold": 10000,  # Currency Transaction Report
        "SAR_threshold": 5000,   # Suspicious Activity Report
        "wire_threshold": 3000,  # Enhanced monitoring for wires
    }

    # TODO: Calculate compliance requirements
    results = {
        "amount": amount,
        "type": type,
        "ctr_required": amount >= thresholds["CTR_threshold"],
        "below_ctr_requried": 8000 <= amount <= thresholds["CTR_threshold"],
        "wire_monitoring":  type == "wire_transfer" and amount >= thresholds["wire_threshold"],
        "potential_strcuturing": amount >= 8000 and amount < thresholds["CTR_threshold"]
    }

    return results


# Tool Registry
INVESTIGATION_TOOLS = {
    "get_transaction_history": get_transaction_history,
    "get_customer_profile": get_customer_profile,
    "check_regulatory_thresholds": check_regulatory_thresholds
}


# Tool Execution Functions
def parse_tool_calls(text):
    """Parse JSON tool calls from LLM response"""
    # Use a regex that specifically looks for JSON blocks
    # Added 're.DOTALL' so the regex can span multiple lines
    json_pattern = r'```json\s*(.*?)\s*```'
    
    # Ensure 'matches' is defined even if nothing is found
    matches = re.findall(json_pattern, text, re.DOTALL)
    
    tool_calls = []
    
    # Safety check: if no matches were found, just return the empty list
    if not matches:
        return tool_calls

    for match in matches:
        try:
            # Parse the JSON string
            tool_call = json.loads(match)
            # Validate structure
            if "tool" in tool_call and "parameters" in tool_call:
                tool_calls.append(tool_call)
        except json.JSONDecodeError:
            continue
            
    return tool_calls


def execute_tool(tool_name, parameters):
    """Execute a tool with given parameters"""
    # TODO: Check if tool exists and execute
    if tool_name not in INVESTIGATION_TOOLS:
        return {"error": f"Tool {tool_name} not found"}

    try:
        # TODO: Execute tool function
        tool_function = INVESTIGATION_TOOLS[tool_name]
        result = tool_function(**parameters)
        return result
    except Exception as e:
        return {"error": f"Tool execution failed: {str(e)}"}


def process_tool_calls(llm_response):
    """Process all tool calls in LLM response and return results"""
    # TODO: Parse tool calls and execute them
    tool_calls = parse_tool_calls(llm_response) 
    results = []

    # TODO: Print execution details
    for tool_call in tool_calls:
      tool_name = tool_call["tool"]
      tool_parameters = tool_call["parameters"]

      print(f"\nExecuting: {tool_name}")
      print(f"\nParameters: {tool_parameters}")

      result = execute_tool(tool_name, tool_parameters)
      results.append({
            "tool": tool_name,
            "parameters": tool_parameters,
            "result": result
        })

      print(f"Result: {json.dumps(results, indent=2)}")
      print("-"*40)
    # TODO: Return results
    return results

