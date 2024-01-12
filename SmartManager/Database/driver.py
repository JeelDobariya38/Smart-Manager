from typing import Protocol


class Driver(Protocol):
    def execute_sql(self, sql_query) -> None:
        ...
