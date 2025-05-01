# A class should have a single responsibility


class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Report: {self.title}\n{self.content}"

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.generate_report())
        print(f"Report saved to {filename}")

# Usage
if __name__ == "__main__":
    report = Report("Monthly Sales", "Sales increased by 10%")
    print(report.generate_report())
    report.save_to_file("sales_report.txt")


# In this version, the Report class handles multiple responsibilities:

# Managing report data
# Generating reports
# Saving reports to a file


# Violation:
# Handles both report generation & file saving.
# If we change how reports are stored (e.g., database instead of file), we must modify the class.
# Breaks SRP because it has two responsibilities.
