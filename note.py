import os
from datetime import datetime

def add_daily_note():
    # تنظیمات ریپازیتوری
    repo_path = "/path/to/your/my-note-repo"  # مسیر ریپازیتوری خود را جایگزین کنید
    notes_dir = os.path.join(repo_path, "daily_notes")
    
    # ایجاد دایرکتوری اگر وجود نداشته باشد
    os.makedirs(notes_dir, exist_ok=True)
    
    # تاریخ امروز برای نام فایل
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(notes_dir, f"{today}.md")
    
    # دریافت یادداشت از کاربر
    print("یادداشت امروز خود را وارد کنید (برای پایان، یک خط خالی بگذارید):")
    print("(می‌توانید جملات انگیزشی، افکار یا هر چیزی که می‌خواهید بنویسید)")
    print("----------------------------------------")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    # اگر کاربر متنی وارد کرده باشد، ذخیره می‌کنیم
    if lines:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# یادداشت روزانه - {today}\n\n")
            f.write("\n".join(lines))
        
        print(f"\nیادداشت شما در {file_path} ذخیره شد.")
    else:
        print("هیچ متنی وارد نشد، فایلی ایجاد نشد.")

if __name__ == "__main__":
    add_daily_note()
