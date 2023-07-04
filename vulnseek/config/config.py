from configparser import ConfigParser


def config_parse(filename, section):
    parser = ConfigParser()
    parser.read(filename)

    parsed_dict = {}
    if parser.has_section(section):
        pairs = parser.items(section)
        for part in pairs:
            parsed_dict[part[0]] = part[1]
    else:
        raise Exception(f"Section {section} not found in {filename} file")

    return parsed_dict
