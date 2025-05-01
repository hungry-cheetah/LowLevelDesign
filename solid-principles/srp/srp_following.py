class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class ReportPrinter:
    @staticmethod
    def generate_report(report: Report):
        return f"Report: {report.title}\n{report.content}"

class ReportSaver:
    @staticmethod
    def save_to_file(report: Report, filename):
        with open(filename, 'w') as file:
            file.write(ReportPrinter.generate_report(report))
        print(f"Report saved to {filename}")

# Usage
if __name__ == "__main__":
    report = Report("Monthly Sales", "Sales increased by 10%")
    print(ReportPrinter.generate_report(report))
    ReportSaver.save_to_file(report, "sales_report.txt")
