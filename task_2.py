def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

        return cats

    except FileNotFoundError:
        print("File not found.")
        return []
    except ValueError:
        print("Incorrect data format.")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)