.PHONY: book serve

book:
	cd book && uv run jupyter book clean --all --yes && uv run jupyter book build --html

serve:
	cd book && uv run jupyter book clean --all --yes && uv run jupyter book build --site && uv run jupyter book start
