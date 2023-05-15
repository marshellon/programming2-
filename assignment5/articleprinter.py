import xml.etree.ElementTree as ET

class ArticlePrinter:
    def printer(self, information_dict: dict):
        """
        Use:
            Write the dictionary data as XML files.

        Returns:
            None
        """
        for article_id, xml_content in information_dict.items():
            # Parse the XML content
            root = ET.fromstring(xml_content)

            # Create an ElementTree object
            tree = ET.ElementTree(root)

            # Write the ElementTree to an XML file
            tree.write(f"{article_id}.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    printer = ArticlePrinter()
    information_dict = {
        "article1": "<xml>...</xml>",
        "article2": "<xml>...</xml>",
        "article3": "<xml>...</xml>",
    }
    printer.printer(information_dict)