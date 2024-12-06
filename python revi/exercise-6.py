import os





def organiseFolder(folder,fileType):
    files = os.listdir(folder)

    i = 0
    for file in files:
        i += 1
        # Check if the file ends with filetype eg (.pdf , .py . js and any other)
        if file.endswith(fileType):
            # Build full file path
            old_file = os.path.join(folder, file)
            new_file = os.path.join(folder, f"previousYear-paper-{i}{fileType}")
        
            # Rename the file
            os.rename(old_file, new_file)

            print(f"Renamed: {old_file} to {new_file}")

organiseFolder("New folder", ".pdf")