import json

class JsonOutputFile:
    def output(self, title: str, description: str):
        self.title = title
        self.description = description

        output = {
            'title': self.title,
            'description': self.description
        }
        with open('output.json', 'w') as f:
            json.dump(output, f, indent=4)

class Report:
    def __init__(self, title, description):
        self.title = title
        self.description = description

        self.output_obj = JsonOutputFile()
    
    def output_file(self):
        self.output_obj.output(self.title, self.description)

title = 'Title'
description = 'sample description'
report = Report(title, description)
report.output_file()