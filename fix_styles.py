import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

bad_user = """msg.innerHTML = `<div class="tw-flex tw-items-start tw-gap-3 tw-max-w-85"><div class="tw-p-4 tw-rounded-2xl tw-text-sm tw-leading-relaxed tw-shadow-sm tw-whitespace-pre-line tw-bg-slate-100-80 tw-text-slate-800 tw-rounded-tr-none" style="background: rgba(241, 245, 249, 0.8);">${text}</div></div>`;"""

good_user = """msg.innerHTML = `
                <div style="display: flex; align-items: flex-start; gap: 12px; max-width: 85%;">
                    <div style="padding: 16px; border-radius: 16px; border-top-right-radius: 0; font-size: 14px; line-height: 1.6; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); white-space: pre-line; background: rgba(241, 245, 249, 0.8); color: #1e293b;">${text}</div>
                </div>
            `;"""

bad_ai = """msg.innerHTML = `<div class="tw-flex tw-items-start tw-gap-3 tw-max-w-95"><div class="tw-w-8 tw-h-8 tw-rounded-full tw-bg-gradient tw-shadow-lg tw-flex-shrink-0 tw-mt-1 tw-border tw-border-white" style="border-width: 2px; border-color: white;"></div><div class="tw-p-4 tw-rounded-2xl tw-text-sm tw-leading-relaxed tw-shadow-sm tw-whitespace-pre-line tw-bg-white tw-border tw-border-gray-100 tw-text-slate-700 tw-rounded-tl-none">${text}</div></div>`;"""

good_ai = """msg.innerHTML = `
                <div style="display: flex; align-items: flex-start; gap: 12px; max-width: 95%;">
                    <div style="width: 32px; height: 32px; border-radius: 50%; background-image: linear-gradient(to top right, #60a5fa, #6366f1, #a855f7); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); flex-shrink: 0; margin-top: 4px; border: 2px solid white;"></div>
                    <div style="padding: 16px; border-radius: 16px; border-top-left-radius: 0; font-size: 14px; line-height: 1.6; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); white-space: pre-line; background: white; border: 1px solid #f3f4f6; color: #334155;">${text}</div>
                </div>
            `;"""

content = content.replace(bad_user, good_user)
content = content.replace(bad_ai, good_ai)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Styles fixed")
