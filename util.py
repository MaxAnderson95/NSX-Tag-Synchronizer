def compare_tags(tags1, tags2):
    missing_tags = []
    for item in tags1:
        if item not in tags2:
            missing_tags.append(item)
    return missing_tags

def concat_tag(tag):
    if tag["scope"] != "":
        return f'{tag["tag"]}:{tag["scope"]}'
    else:
        return f'{tag["tag"]}'

def concat_tags(tags):
    return "\n".join([concat_tag(tag) for tag in tags])