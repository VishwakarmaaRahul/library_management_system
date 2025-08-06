import subprocess

output = subprocess.run(
    ['python', 'manage.py', 'inspectdb'],
    capture_output=True
)

text = output.stdout.decode('utf-8', errors='ignore')
clean = text.replace('\x00', '')

with open('models.py', 'w', encoding='utf-8') as f:
    f.write(clean)

print("Clean models.py generated")
