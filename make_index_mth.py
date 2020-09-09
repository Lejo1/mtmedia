import os

data = b"\x4d\x54\x48\x53\x00\x01"
count = 0
print("Reading and converting media files...")
for filename in os.listdir("m"):
    if filename != "index.mth":
        data += filename.decode("hex")
        count += 1

print("Writing to file...")
file = open("m/index.mth", "w")
file.write(data)
file.close()
print("Wrote " + str(count) + " medias to file.")
