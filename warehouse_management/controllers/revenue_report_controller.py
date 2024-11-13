from services.report_service import ReportService

class RevenueReportController:
    def __init__(self, db_session):
        self.db_session = db_session
    def generate_revenue_report(self, start_date, end_date):
        report_service = ReportService()
        revenue_report = report_service.generate_revenue_report(start_date, end_date)
        print("Báo cáo doanh thu:", revenue_report)
