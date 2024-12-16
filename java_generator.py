import os
import subprocess


def generate_pojo(xsd_file_path: str, output_dir: str, package_name: str):
    """
    Generates a Java POJO from a single XSD file using xjc.bat.

    :param xsd_file_path: The path to the XSD file.
    :param output_dir: The output directory for generated POJOs
    :param package_name: The Java package name for the generated POJO.
    """

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    xjc_bat_path = os.path.join('tools', 'jaxb-ri', 'bin', 'xjc.bat')

    # Run the xjc.bat command to generate the POJO
    try:
        # Create the xjc command
        xjc_command = [
            xjc_bat_path,  # Path to the xjc.bat script (ensure this is in the PATH or provide the full path)
            '-d', output_dir,  # Destination directory for the generated POJOs
            '-p', package_name,  # Java package name
            xsd_file_path  # The XSD file to process
        ]

        # Execute the command
        subprocess.run(xjc_command, check=True)
        print(f'POJO generated for {xsd_file_path} in package {package_name}')

    except subprocess.CalledProcessError as e:
        print(f'Error generating POJO for {xsd_file_path}: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')


def process_xsd_directory(xsd_directory: str, output_dir: str, base_package_name: str):
    """
    Traverses the XSD directory and generates POJOs for each XSD file.

    :param xsd_directory: The base directory containing XSD files (including subdirectories).
    :param output_dir: The output directory for generated POJOs
    :param base_package_name: The base package name for the generated POJOs.
    """

    # Traverse the directory recursively to find all XSD files
    for root, dirs, files in os.walk(xsd_directory):
        for file in files:
            if file.endswith('.xsd'):
                # Full path to the XSD file
                xsd_file_path = os.path.join(root, file)

                # Generate the schema name from the file name (remove .xsd extension)
                schema_name = os.path.splitext(file)[0]

                # Build the package name based on the base package and schema file name
                package_name = f'{base_package_name}.{schema_name}'

                # Generate the POJO for this XSD file
                generate_pojo(xsd_file_path, output_dir, package_name)