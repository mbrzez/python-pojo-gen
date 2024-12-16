from java_generator import process_xsd_directory
from config_loader import config

def main():
    process_xsd_directory(config["xsd_dir"], config["output_dir"], config["package"])


if __name__ == "__main__":
    main()
