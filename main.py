import argparse
from services.finance_service import add_expense, list_expenses, summary

parser = argparse.ArgumentParser(description="Controle financeiro")

parser.add_argument("action", choices=["add", "list", "summary"])
parser.add_argument("value", nargs="?", type=float)
parser.add_argument("category", nargs="?")

args = parser.parse_args()

if args.action == "add":
    add_expense(args.value, args.category)

elif args.action == "list":
    list_expenses()

elif args.action == "summary":
    summary()