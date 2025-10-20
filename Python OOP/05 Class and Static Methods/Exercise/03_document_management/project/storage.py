from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self) -> None:
        self.categories: Category(list) = []
        self.topics: Topic(list) = []
        self.documents: Document(list) = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self,category_id: int, new_name: str) -> None:
        try:
            category = self.categories[category_id - 1]
            category.edit(new_name)
        except IndexError: pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        try:
            topic = self.topics[topic_id -1]
            topic.edit(new_topic, new_storage_folder)
        except IndexError: pass

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        try:
            document = self.documents[document_id - 1]
            document.edit(new_file_name)
        except IndexError: pass

    def delete_category(self, category_id: int) -> None:
        try:
            category = self.categories[category_id - 1]
            self.categories.remove(category)
        except IndexError: pass

    def delete_topic(self, topic_id: int) -> None:
        try:
            topic = self.topics[topic_id - 1]
            self.topics.remove(topic)
        except IndexError: pass

    def delete_document(self, document_id: int) -> None:
        try:
            document = self.documents[document_id - 1]
            self.documents.remove(document)
        except IndexError: pass

    def get_document(self, document_id: int) -> Document:
        try:
            document = self.documents[document_id - 1]
            return document.__repr__()
        except IndexError: pass

    def __repr__(self):
        result = ''
        for document in self.documents:
            result += document.__repr__() + '\n'
        return result