import json

json_path = r"D:\prj_wsl\coco\annotations\captions_train2017.json"
out_path = r"D:\prj_wsl\coco\captions.txt"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

id_to_file = {
    img["id"]: img["file_name"]
    for img in data["images"]
}

with open(out_path, "w", encoding="utf-8") as f:
    for ann in data["annotations"]:
        img_name = id_to_file[ann["image_id"]]
        caption = ann["caption"].replace("\n", " ").replace(", ", " ")
        f.write(f"{img_name},{caption}\n")

print("done")