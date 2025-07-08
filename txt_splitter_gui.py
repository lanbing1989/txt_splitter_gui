import tkinter as tk
from tkinter import filedialog, messagebox
import os

def split_txt_file(filepath, lines_per_file):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    total_lines = len(lines)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    dirname = os.path.dirname(filepath)
    out_files = []
    for i in range(0, total_lines, lines_per_file):
        out_path = os.path.join(dirname, f"{filename}_part{i//lines_per_file + 1}.txt")
        with open(out_path, 'w', encoding='utf-8') as fout:
            fout.writelines(lines[i:i+lines_per_file])
        out_files.append(out_path)
    return out_files

def select_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_path_var.set(path)

def split_action():
    filepath = file_path_var.get()
    try:
        lines_per_file = int(lines_per_file_var.get())
        if lines_per_file <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("参数错误", "请输入有效的正整数（每文件行数）")
        return
    if not os.path.isfile(filepath):
        messagebox.showerror("文件错误", "请选择有效的txt文件")
        return
    try:
        out_files = split_txt_file(filepath, lines_per_file)
        messagebox.showinfo("分割完成", f"分割完成，共生成 {len(out_files)} 个文件。")
    except Exception as e:
        messagebox.showerror("分割失败", str(e))

root = tk.Tk()
root.title("TXT文本分割工具")

tk.Label(root, text="选择txt文件:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
file_path_var = tk.StringVar()
tk.Entry(root, textvariable=file_path_var, width=40).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="浏览", command=select_file).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="每个文件的行数:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
lines_per_file_var = tk.StringVar(value="1000")
tk.Entry(root, textvariable=lines_per_file_var, width=10).grid(row=1, column=1, padx=5, pady=5, sticky='w')

tk.Button(root, text="开始分割", command=split_action, width=20).grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()