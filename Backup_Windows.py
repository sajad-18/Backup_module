import os
import shutil


def get_valid_dirs():
    base_path = os.path.expanduser("~")

    user_input = input('📥 Enter the folders you want to back up (e.g., Pictures, Videos): ')
    user_dirs = [i.strip() for i in user_input.split(",") if i.strip()]

    important_option = []
    ask = input('⚠️ Do you want to include common folders (Desktop, Documents, etc)? (y/n): ').strip().lower()
    while ask not in ('y', 'n'):
        ask = input('❓ Please enter only "y" or "n": ').strip().lower()

    if ask == 'y':
        important_input = input('📥 Which ones? (comma-separated, e.g., Desktop, Downloads): ')
        important_option = [i.strip() for i in important_input.split(',') if i.strip()]

    all_targets = user_dirs + important_option
    valid_dirs = []

    for folder in all_targets:
        full_path = os.path.join(base_path, folder)

        if not os.path.exists(full_path):
            one_drive_path = os.path.join(base_path, "OneDrive", folder)
            if os.path.exists(one_drive_path):
                full_path = one_drive_path
            else:
                print(f'❌ Folder "{folder}" not found. Skipping...')
                continue

        valid_dirs.append(full_path)

    print('\n📦 Final paths for backup:')
    for v in valid_dirs:
        print(f'✅ {v}')

    return valid_dirs


def get_goal_dir():
    while True:
        goal_dir = input('\n🎯 Enter your destination path (tip: right-click folder > "Copy as path"): ').strip('"')
        if not os.path.exists(goal_dir):
            make = input('⚠️ Destination folder does not exist. Do you want to create it? (y/n): ').strip().lower()
            while make not in ('y', 'n'):
                make = input('❓ Please enter only "y" or "n": ').strip().lower()

            if make == 'y':
                os.makedirs(goal_dir, exist_ok=True)
                return goal_dir
            else:
                print('❌ Backup canceled.')
                return None
        else:
            return goal_dir


def get_folder_size_and_count(folders):
    total_size = 0
    total_files = 0
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    total_size += os.path.getsize(fp)
                    total_files += 1
                except:
                    continue
    return total_size, total_files


def check_space_and_confirm(valid_dirs, goal_dir):
    total_size, total_files = get_folder_size_and_count(valid_dirs)

    drive, _ = os.path.splitdrive(goal_dir)
    usage = shutil.disk_usage(drive or goal_dir)

    print("\n📊 Backup Info:")
    print(f"  📁 Total files: {total_files:,}")
    print(f"  📦 Total size: {total_size / (1024**3):.2f} GB")
    print(f"💽 To Drive: {drive or goal_dir}")
    print(f"   • Total space: {usage.total / (1024**3):.2f} GB")
    print(f"   • Free space : {usage.free / (1024**3):.2f} GB")
    print(f"⭕ Free space after copy backup: {(usage.free - total_size) / (1024**3):.2f} GB")

    if usage.free < total_size:
        short = total_size - usage.free
        print(f"\n❌ Not enough space! You need {short / (1024**3):.2f} GB more.")
        return False
    else:
        confirm = input("\n✅ Sufficient space! Do you want to continue with the backup? (y/n): ").strip().lower()
        while confirm not in ('y', 'n'):
            confirm = input('❓ Please enter only "y" or "n": ').strip().lower()
        return confirm == 'y'


def backup():
    valid_dirs = get_valid_dirs()
    if not valid_dirs:
        print("❌ No valid folders to back up. Exiting.")
        return

    goal_dir = get_goal_dir()
    if not goal_dir:
        return

    if not check_space_and_confirm(valid_dirs, goal_dir):
        print("⚠️ Backup was canceled by user or due to insufficient space.")
        return

    print("\n🚀 Proceeding with backup... (not implemented in this part)")


backup()
