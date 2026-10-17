import json

with open('filtered_tasks.json', 'r') as f:
    tasks = json.load(f)

subagents = []
batch_size = 5
for i in range(0, len(tasks), batch_size):
    batch = tasks[i:i+batch_size]
    prompt = "Process these tasks:\n" + json.dumps(batch, ensure_ascii=False, indent=2)
    subagents.append({
        "TypeName": "poster_generator",
        "Role": f"Poster Batch {i//batch_size + 1}",
        "Prompt": prompt,
        "Model": "pro" # using pro as per instructions for complex tasks, though this is simple
    })

tool_call = {
    "Subagents": subagents,
    "toolSummary": "Invoke poster subagents",
    "toolAction": "Invoking subagents"
}
with open('invoke_tool.json', 'w') as f:
    json.dump(tool_call, f, ensure_ascii=False, indent=2)
print("Tool call args written to invoke_tool.json")
