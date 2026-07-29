file = None

try:
    file = open("sample.txt", "w")
    file.write("Hello from Python!\n")
except Exception as e:
    print("An error occurred:", e)
else:
    print("File written successfully.")
finally:
    if file is not None:
        file.close()
    print("Cleanup complete.")
