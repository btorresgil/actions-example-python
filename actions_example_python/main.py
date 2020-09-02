import defusedxml.ElementTree as ET
from panos.firewall import Firewall


def main() -> None:
    fw = Firewall("10.0.1.25", "admin", "Pal0Alt0!")
    result = fw.op("show system info")
    print(ET.tostring(result))


if __name__ == "__main__":
    main()
