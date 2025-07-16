from agent import plan_task, generate_final_answer
from retriever import retrieve_relevant_docs
from tools import call_tools

def run_agent():
    query = input("Your question: ")

    # PLAN
    plan_json = plan_task(query)
    print("\n[PLAN]:", plan_json)

    # PARSE
    retrieve = '"retrieve_needed": true' in plan_json
    tool_names = []
    if '"tools_to_call": [' in plan_json:
        try:
            raw = plan_json.split('"tools_to_call": [')[1].split("]")[0]
            tool_names = [x.strip().strip('"') for x in raw.split(",")]
        except:
            pass

    # RETRIEVE
    docs = retrieve_relevant_docs(query) if retrieve else []

    # TOOLS
    tool_results = call_tools(tool_names, query)

    # FINAL
    final = generate_final_answer(query, docs, tool_results)
    print("\n[ANSWER]:", final)

if __name__ == "__main__":
    run_agent()