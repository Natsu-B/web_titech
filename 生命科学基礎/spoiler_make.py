##同じdirにあるmarkdownfileのうち、_spoilerがファイル名に含まれてないのを探し、赤文字をspoilerにしたものを(filename)_spoiler.mdとして返す
import os

path = os.getcwd()
files = os.listdir()
files_in = [s for s in files if 'md' in s and '_spoiler' not in s]
print(files_in)
str_plus = '<style>\r\n   .spoiler { padding: 0 4px; color: #333; background: #333; border-radius: 4px; }\r\n  .spoiler:hover,\r\n  .spoiler:active { color: red; background: none; }\r\n</style>'
for s in files_in:
    file_path = path + '\\' + s
    file_name = os.path.splitext(s)[0]
    print(file_name)
    file_path_spoiler = path + '\\' + file_name + '_spoiler.md'
    with open(file_path,'r',encoding="utf-8_sig") as f:
        string_oldpart = f.read()
    string_spoiler = string_oldpart.replace('style="color: red; "', 'class="spoiler" ontouchstart')
    string_all_spoiler = str_plus + string_spoiler
    with open(file_path_spoiler,'w') as f:
        f.write(string_all_spoiler)
    print("finish "+file_name+ '.md')