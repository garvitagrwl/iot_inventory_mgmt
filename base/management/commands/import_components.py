from django.core.management.base import BaseCommand
from base.models import Component
import pandas as pd

class Command(BaseCommand):
    help = 'Import components from Excel file'

    def handle(self, *args, **kwargs):
        try:
            # Load the Excel file
            df = pd.read_excel('base/components.xlsx', skiprows=1)
            print(df.columns.tolist())  # Optional, just to verify

            df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names

            # Print column names for debugging
            self.stdout.write(f"📄 Columns found in Excel: {list(df.columns)}")

            # Try to match expected columns
            expected_columns = {
                'Name of Equipment': None,
                'Category': None,
                'Quantity': None
            }

            for col in df.columns:
                col_clean = col.strip().lower()
                if 'name' in col_clean and 'equip' in col_clean:
                    expected_columns['Name of Equipment'] = col
                elif 'category' in col_clean:
                    expected_columns['Category'] = col
                elif 'quantity' in col_clean:
                    expected_columns['Quantity'] = col

            # Ensure all expected columns were found
            if None in expected_columns.values():
                raise Exception(f"❌ Could not find all expected columns. Detected: {expected_columns}")

            # Subset and rename
            df = df[[expected_columns['Name of Equipment'], expected_columns['Category'], expected_columns['Quantity']]]
            df.rename(columns={
                expected_columns['Name of Equipment']: 'name_comp',
                expected_columns['Category']: 'category',
                expected_columns['Quantity']: 'quantity'
            }, inplace=True)

            # Save to DB
            for _, row in df.iterrows():
                try:
                    Component.objects.create(
                        name_comp=row['name_comp'],
                        quantity=int(row['quantity']),
                        category=row['category']
                    )
                except Exception as inner_error:
                    self.stderr.write(f"⚠️ Skipping row: {inner_error}")

            self.stdout.write(self.style.SUCCESS('✅ Components imported successfully!'))

        except Exception as e:
            self.stderr.write(f"❌ Error importing components: {e}")
