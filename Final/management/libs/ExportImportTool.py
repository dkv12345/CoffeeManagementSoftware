from Final.management.models.Product import Product


def load_workbook(filename):
    pass


class ExportImportTool:
    def export_products_excel(self, products, filename, xr=None):
        workbook = xr.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # Modify column width
        worksheet.set_column('A:A', 5)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 10)
        worksheet.set_column('D:D', 10)
        bold = workbook.add_format({'bold': True})

        # Add header
        worksheet.write('A1', 'Product Id', bold)
        worksheet.write('B1', 'Product Name', bold)
        worksheet.write('C1', 'Unit Price', bold)
        worksheet.write('D1', 'Quantity', bold)

        for i in range(len(products)):
            index = i + 2
            p = products[i]
            worksheet.write(f'A{index}', p.proid)
            worksheet.write(f'B{index}', p.proname)
            worksheet.write(f'C{index}', p.price)
            worksheet.write(f'D{index}', p.quantity)
        workbook.close()
    def import_products_excel(self,filename):
        wb = load_workbook(filename)
        ws = wb[wb.sheetnames[0]]
        self.list = []
        is_header=True
        for row in ws.values:
            if is_header==True:
                is_header=False
                continue
            id = row[0]
            name = row[1]
            price =float(row[2])
            quantity = int(row[3])
            p = Product(id, name,price,quantity)
            self.list.append(p)
        wb.close()
        return self.list
