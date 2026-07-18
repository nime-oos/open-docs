import json

log_path = '/home/sysadmin/snap/antigravity/5/.gemini/antigravity/brain/66e16026-8330-43ce-8055-3ff641f6026e/.system_generated/logs/transcript_full.jsonl'
contents = []

with open(log_path, 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            if 'tool_calls' in data:
                for tc in data['tool_calls']:
                    if tc['name'] == 'write_to_file':
                        if tc['args'].get('TargetFile', '').endswith('build.py'):
                            contents.append(tc['args'].get('CodeContent', ''))
                    elif tc['name'] == 'replace_file_content' or tc['name'] == 'multi_replace_file_content':
                        if tc['args'].get('TargetFile', '').endswith('build.py'):
                            contents.append("MODIFIED")
        except:
            pass

print(f"Found {len(contents)} writes/modifications to build.py")
if len(contents) >= 1:
    with open('recovered_build.py', 'w') as f:
        # We need the most recent FULL write before the last one.
        for c in reversed(contents):
            if c != "MODIFIED" and len(c) > 10000: # The massive one with 30 exercises is very large
                f.write(c)
                print(f"Recovered a file of size {len(c)}")
                break
