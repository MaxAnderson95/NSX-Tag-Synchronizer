def compare_tags(tags1, tags2):
    missing_tags = []
    for item in tags1:
        if item not in tags2:
            missing_tags.append(item)
    return missing_tags

def concat_tag(tag):
    return f'{tag["tag"]}:{tag["scope"]}'

def concat_tags(tags):
    return "\n".join([concat_tag(tag) for tag in tags])