import sys

def split_full_script(text):
    return text.split("\n\n")

def get_init_timestamp(snpt):
    return snpt.split("\n")[1].split(" -->")[0]

timestamp_content={}
for srt_file in sys.argv[1:]:
    inp = open(srt_file, 'r')
    script = split_full_script(inp.read())
    for snpt in script:
        timestamp_content[get_init_timestamp(snpt)]=snpt
    inp.close()

for time_init in sorted(timestamp_content.keys()):
    print(timestamp_content[time_init])
