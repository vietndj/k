import sys

with open("/Users/vietmac/Documents/CODE/k/nhac.html", "r") as f:
    content = f.read()

# The incorrect injection looks like:
#                 <div class="bg-slate-50 rounded-xl border border-slate-200 p-4"><div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden mb-6">
# ... and ends before ...
#                 <div class="bg-slate-50 rounded-xl border border-slate-200 p-4">                <div class="bg-slate-50 rounded-xl border border-slate-200 p-4">

# We can find this exact block because we know the text inside it
start_marker = '<div class="bg-slate-50 rounded-xl border border-slate-200 p-4"><div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden mb-6">'
end_marker = '<div class="bg-slate-50 rounded-xl border border-slate-200 p-4">                <div class="bg-slate-50 rounded-xl border border-slate-200 p-4">'

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker) + len('<div class="bg-slate-50 rounded-xl border border-slate-200 p-4">')
    
    # Replace that entire block with just one original div:
    correct = '                <div class="bg-slate-50 rounded-xl border border-slate-200 p-4">'
    
    new_content = content[:start_idx] + correct + content[end_idx:]
    
    with open("/Users/vietmac/Documents/CODE/k/nhac.html", "w") as f:
        f.write(new_content)
    print("Fixed duplicates!")
else:
    print("Could not find markers")
