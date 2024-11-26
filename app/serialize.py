import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerialize(SerializeStrategy):
    def serialize(self, book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
