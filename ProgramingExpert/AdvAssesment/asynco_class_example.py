import asyncio
class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.database = database

    # Write your code here.

    async def fetch_records(self, record_ids):
        records =[]
        for record_id in record_ids:
            records.append(self.database.async_fetch(record_id))

        return_records = await asyncio.gather(*records) 
        return return_records 