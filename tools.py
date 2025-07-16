import datetime

def calculator(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid calculation."

def get_date():
    return str(datetime.datetime.now().date())

def call_tools(tool_names, query):
    results = {}
    for tool in tool_names:
        if tool == "calculator":
            results["calculator"] = calculator(query)
        elif tool == "date":
            results["date"] = get_date()
        else:
            results[tool] = "Unknown tool"
    return results