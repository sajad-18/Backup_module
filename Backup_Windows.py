import os
import shutil


def backup():
    base_path = os.path.expanduser("~")

    user_input = input('📥 Enter the folders you want to backup(example: Pictures, Videos, etc): ')
    user_dirs = [i.strip() for i in user_input.split(",") if i.strip()]

    ask = input('⚠️ Do you want to backup from the important folders(Desktop, Downloads, Documents, etc)?(y/n) ')

    important_option = []
    if ask.lower() == 'y':
        important_input = input('📥 Which one?(just enter the name like Desktop, Pictures, etc) ')
        important_option = [i.strip() for i in important_input.split(',') if i.strip()]

    all_target = user_dirs + important_option
    valid_dirs = []

    for folder in all_target:
        full_path = os.path.join(base_path, folder)

        if not os.path.exists(full_path):
            one_drive_path = os.path.join(base_path, "OneDrive", folder)
            if os.path.exists(one_drive_path):
                full_path = one_drive_path
            else:
                print(f'❌ folder "{folder}" doesn\'t exist! skip...')
                continue

        valid_dirs.append(full_path)

    print('\n📦 final paths for backup: ')
    for v in valid_dirs:
        print(f'✅ {v}')

    goal_dir = input('\n🎯 Please enter your goal path(if your folder exists pls right click on it & click "copy as path" & paste there): ').strip('"')
    if not os.path.exists(goal_dir):
        make = input('⚠️ Destination folder does not exist. Do you want to create it? (y/n): ')
        if make.lower() == 'y':
            os.makedirs(goal_dir, exist_ok=True)
        else:
            print('❌ Backup canceled.')
            return

    total_size = 0
    total_files = 0
    for folder in valid_dirs:
        for root, dirs, files in os.walk(folder):
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    total_size += os.path.getsize(fp)
                    total_files += 1
                except:
                    continue

    drive, _ = os.path.splitdrive(goal_dir)
    usage = shutil.disk_usage(goal_dir)

    print("\n🧾 Backup Summary:")
    print(f"📁 Total files to backup: {total_files:,}")
    print(f"💾 Total size needed: {total_size / (1024**3):.2f} GB")
    print(f"🗃 Drive: {drive or goal_dir}")
    print(f"📂 Total space: {usage.total / (1024**3):.2f} GB")
    print(f"📂 Free space: {usage.free / (1024**3):.2f} GB")

    if usage.free > total_size:
        confirm = input("✅ Sufficient space! Do you want to continue with the backup? (y/n): ")
        if confirm.lower() != 'y':
            print("🛑 Backup canceled by user.")
            return
    else:
        short = total_size - usage.free
        print(f"\n❌ Not enough space. You're short of {short / (1024**3):.2f} GB.")
        return


backup()


