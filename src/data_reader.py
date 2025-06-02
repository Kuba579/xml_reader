import xml.etree.ElementTree as ET

def get_base64_data(path: str):
    tree = ET.parse(path)
    root = tree.getroot()

    namespaces = {'mstns': root.tag.split("}")[0][1:]}

    file_type = root.findall('.//mstns:RodzajDoreczenie', namespaces)
    if not file_type:
        file_type = root.findall('.//mstns:Rodzaj', namespaces)

    if file_type:
        file_type = file_type[0].text
    
    if file_type == "DORECZENIE":
        pass
    
    base64_data = root.findall('.//mstns:PodpisObraz', namespaces)
    if not base64_data:
        base64_data = root.findall('.//mstns:Podpis', namespaces)

    if base64_data:
        base64_data = base64_data[0].text
    else:
        raise ValueError("Base64 data not found in the XML.")
    
    return base64_data

