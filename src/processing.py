from typing import Dict, List


def filter_by_state(transactions, state="EXECUTED"):
    """    Фильтрует список словарей по значению ключа state    """
    return [
        transaction for transaction in transactions if transaction.get("state") == state
    ]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """    Сортирует список словарей по дате    """
    return sorted(transactions, key=lambda x: x["date"], reverse=descending)
