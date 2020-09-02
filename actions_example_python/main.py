"""My cool new python script."""

import defusedxml.ElementTree as ET
from panos.firewall import Firewall
from panos.objects import AddressObject


def inc(num: int) -> int:
    return num + 1


def main() -> None:
    fw = Firewall("10.0.1.25", "admin", "Pal0Alt0!")
    for index in range(1, 5):
        addobj = fw.add(AddressObject(f"My-new-object-{index}", "1.1.1.1"))
        addobj.create()
    result = fw.op("show system info")
    print(ET.tostring(result))


if __name__ == "__main__":
    main()
