from services.report_service import ReportService

class StockReportController:
    def __init__(self, db_session):
        self.db_session = db_session
    def generate_stock_report(self):
        report_service = ReportService()
        stock_report = report_service.generate_stock_report()
        print("Báo cáo tồn kho:", stock_report)
